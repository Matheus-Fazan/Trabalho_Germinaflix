# Cayres Flix

Site estático com informações sobre filmes e séries.

## Executar localmente

Na raiz do projeto, inicie um servidor com Python 3.9 ou superior:

```sh
python -m http.server 8000
```

Abra `http://localhost:8000/`. Para interromper o servidor, pressione Ctrl+C.

## Validar recursos

```sh
python scripts/verificar_recursos.py
```

O script usa somente a biblioteca padrão do Python e verifica o `index.html` e referências locais em HTML e CSS, inclusive a capitalização dos nomes. O comando retorna erro se encontrar um recurso ausente ou um caminho incompatível com o projeto. Referências externas não são verificadas.

## CI/CD e GitHub Pages

O workflow `.github/workflows/ci-cd.yml` executa a validação em pushes para `main` e pull requests direcionados a `main`. O job de publicação depende da CI e só executa em um push para `main`. Não há publicação no evento de pull request.

Em **Settings → Pages**, selecione **GitHub Actions** como fonte de publicação. Confira se o Pages e o GitHub Actions estão disponíveis para o repositório e se o ambiente `github-pages` permite o deploy. Depois de um push aprovado para `main`, acompanhe a execução em **Actions** e consulte o endereço publicado nas configurações do Pages ou no job de deploy.

Exigir a aprovação da CI antes do merge depende de uma regra de proteção de branch ou ruleset configurada no GitHub; o workflow sozinho não bloqueia merges.
