# Registro de uso de IA

Ferramenta: Codex (OpenAI). Este registro começa com a preparação do site; houve interações anteriores de planejamento nesta conversa. A validação e revisão pelo aluno ainda precisam ser realizadas.

| Interação | Prompt exato | Resultado da IA | Problema ou avaliação | Alteração feita e por quem | Evidência |
| --- | --- | --- | --- | --- | --- |
| Preparação do site | Ver prompt completo abaixo. | Caminhos corrigidos e verificador de recursos criado. | Dois caminhos de fundo no CSS não existiam; havia favicons absolutos e barras invertidas. Uma substituição inicial afetou cinco caminhos de logo, identificados e corrigidos pela verificação. | Codex alterou caminhos e criou `scripts/verificar_recursos.py`. Nenhuma alteração manual pelo aluno foi observada nesta etapa. | Verificação final: 168 referências locais e 0 erros. Teste temporário: referência `imagem-inexistente-para-teste.png` identificada em `teste-recurso-temporario.html`, 169 referências, 1 erro e saída 1; arquivo removido e verificação novamente aprovada. Resultados locais, sem comprovação de publicação. |
| Pipeline CI/CD | Ver prompt completo abaixo. | Codex criou o workflow e documentou seu uso no README. | Os históricos local e remoto divergiram; o conflito no registro foi resolvido preservando a versão local. | Codex configurou CI em pushes e PRs para `main` e CD após CI bem-sucedida em push para `main`. | `python scripts/verificar_recursos.py`: 168 referências locais, 0 erros. Execução remota e publicação ainda não comprovadas no momento do registro. |
| Proteção da main | Ver prompt completo abaixo. | Codex consultou os PRs, execuções, rulesets e configuração local. | A API retornou lista vazia de PRs e rulesets; a branch não estava no remoto após atualização das referências. A integração retornou 403 ao consultar branch protection e não oferece alteração de regras. Não foi possível observar uma execução da nova CI ou testar o bloqueio do merge. | Nenhuma regra foi configurada e nenhum teste de bloqueio foi feito; Codex registrou as verificações. | O workflow declara o job `Validar recursos`; o nome do check em execução ainda não foi confirmado. As execuções existentes eram da publicação antiga do Pages. Aplicação a administradores e bypass não puderam ser verificados. |

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

## Prompt completo — pipeline CI/CD

> Continue na branch existente `preparar-github-pages`. Antes de alterar arquivos, confira o estado do Git e o PR existente; preserve alterações que não sejam suas.
>
> Crie `.github/workflows/ci-cd.yml` para o Cayres Flix com estes requisitos:
>
> - Executar a CI em `push` para `main` e em `pull_request` direcionado a `main`.
> - Fazer checkout, configurar o ambiente necessário e instalar dependências apenas quando necessário.
> - Executar `scripts/verificar_recursos.py` e falhar se a verificação encontrar problemas.
> - Executar o CD somente após um `push` na `main` e somente se a CI tiver terminado com sucesso.
> - Publicar o site estático no GitHub Pages usando GitHub Actions e as permissões necessárias.
>
> Atualize o README com instruções de execução local, validação, funcionamento da pipeline e configuração necessária do Pages. Execute as verificações locais possíveis.
>
> Acrescente este prompt e os resultados reais ao registro de uso de IA. Faça commit na branch existente e envie-o ao GitHub, atualizando o mesmo PR. Acompanhe a CI do PR e confirme que o job de publicação não executou nesse evento. Se houver falha, investigue e corrija na mesma branch.
>
> Apresente os links e aguarde minha revisão. Não faça merge.

## Prompt completo — proteção da main

> Verifique o PR e a execução mais recente da CI na branch `preparar-github-pages`. Confirme qual é o nome exato do check que deve ser exigido para integrar o PR à `main`.
>
> Verifique se o repositório permite configurar uma regra de proteção ou ruleset para `main` exigindo esse check. Se eu tiver permissão e o recurso estiver disponível, configure a regra. Informe se ela se aplica a administradores e se há possibilidade de bypass.
>
> Caso seja possível demonstrar isso com segurança no PR existente, faça um teste controlado na mesma branch: introduza temporariamente uma referência local inexistente, envie o commit e confirme que a CI falha e que a regra impede o merge. Em seguida, corrija a referência, envie outro commit e confirme que a CI volta a passar.
>
> Se a configuração ou a demonstração não for possível, explique o bloqueio e o que falta fazer. Não afirme que o merge foi bloqueado sem comprovação.
>
> Registre este prompt, os problemas, as alterações e as evidências reais no arquivo de uso de IA. Envie os registros à mesma branch e confirme novamente o resultado da CI. Não faça merge.
