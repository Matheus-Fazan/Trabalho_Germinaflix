# Registro de uso de IA

Ferramenta: Codex (OpenAI). Este registro começa com a preparação do site; houve interações anteriores de planejamento nesta conversa. A validação e revisão pelo aluno ainda precisam ser realizadas.

| Interação | Prompt exato | Resultado da IA | Problema ou avaliação | Alteração feita e por quem | Evidência |
| --- | --- | --- | --- | --- | --- |
| Preparação do site | Ver prompt completo abaixo. | Caminhos corrigidos e verificador de recursos criado. | Dois caminhos de fundo no CSS não existiam; havia favicons absolutos e barras invertidas. Uma substituição inicial afetou cinco caminhos de logo, identificados e corrigidos pela verificação. | Codex alterou caminhos e criou `scripts/verificar_recursos.py`. Nenhuma alteração manual pelo aluno foi observada nesta etapa. | Verificação final: 168 referências locais e 0 erros. Teste temporário: referência `imagem-inexistente-para-teste.png` identificada em `teste-recurso-temporario.html`, 169 referências, 1 erro e saída 1; arquivo removido e verificação novamente aprovada. Resultados locais, sem comprovação de publicação. |

## Prompt completo — preparação do site

> Analise o estado atual do repositório Cayres Flix e crie uma branch para preparar o site para o GitHub Pages.
>
> Revise os caminhos locais de HTML, CSS, imagens e vídeos. Corrija os caminhos absolutos que possam falhar quando o site estiver publicado em uma URL com o nome do repositório e padronize barras invertidas usadas em URLs. Preserve a aparência e o conteúdo do site.
>
> Crie uma verificação automatizada que confirme a existência do `index.html` e dos recursos locais referenciados em HTML e CSS. Ela deve indicar o arquivo e a referência com problema e retornar falha se encontrar um recurso ausente.
>
> Execute a verificação e faça um teste temporário de falha com uma referência inexistente. Depois, remova a alteração de teste e confirme que a validação passa.
>
> Registre este prompt, os resultados reais, os problemas, as alterações, quem as realizou e as evidências em uma tabela de uso de IA. Não invente informações.
