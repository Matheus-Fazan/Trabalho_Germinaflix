from html.parser import HTMLParser
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)|@import\s+(['\"])(.*?)\3", re.I)
erros = []
verificados = 0


def verificar(origem, referencia):
    global verificados
    referencia = referencia.strip()
    url = urlsplit(referencia)
    if url.scheme or url.netloc or not url.path:
        return
    verificados += 1
    caminho = unquote(url.path)
    if caminho.startswith('/') or '\\' in caminho:
        erros.append((origem, referencia, 'use um caminho relativo com /'))
        return
    destino = Path(os.path.abspath(origem.parent / caminho))
    if not destino.is_relative_to(ROOT) or not destino.resolve().is_relative_to(ROOT):
        erros.append((origem, referencia, 'caminho fora do projeto'))
        return
    atual = ROOT
    for parte in destino.relative_to(ROOT).parts:
        if not atual.is_dir() or parte not in {p.name for p in atual.iterdir()}:
            erros.append((origem, referencia, 'recurso ausente ou nome com capitalização incorreta'))
            return
        atual = atual / parte
    if destino.is_dir() and not (destino / 'index.html').is_file():
        erros.append((origem, referencia, 'diretório sem index.html'))


def verificar_css(origem, texto):
    for match in CSS_URL.finditer(re.sub(r'/\*.*?\*/', '', texto, flags=re.S)):
        verificar(origem, match.group(2) if match.group(2) is not None else match.group(4))


class HTMLRecursos(HTMLParser):
    def __init__(self, origem):
        super().__init__()
        self.origem = origem
        self.em_style = False

    def handle_starttag(self, tag, attrs):
        self.em_style = self.em_style or tag == 'style'
        for nome, valor in attrs:
            if valor and nome in ('src', 'href', 'poster'):
                verificar(self.origem, valor)
            elif valor and nome == 'style':
                verificar_css(self.origem, valor)

    def handle_endtag(self, tag):
        if tag == 'style':
            self.em_style = False

    def handle_data(self, data):
        if self.em_style:
            verificar_css(self.origem, data)


if not (ROOT / 'index.html').is_file():
    erros.append((ROOT / 'index.html', 'index.html', 'arquivo inicial ausente'))

for arquivo in sorted(ROOT.rglob('*')):
    if '.git' in arquivo.parts or not arquivo.is_file():
        continue
    if arquivo.suffix.lower() == '.html':
        parser = HTMLRecursos(arquivo)
        parser.feed(arquivo.read_text(encoding='utf-8'))
    elif arquivo.suffix.lower() == '.css':
        verificar_css(arquivo, arquivo.read_text(encoding='utf-8'))

for origem, referencia, motivo in erros:
    print(f'{origem.relative_to(ROOT)}: {referencia} — {motivo}')
print(f'{verificados} referências locais verificadas; {len(erros)} erro(s).')
sys.exit(bool(erros))
