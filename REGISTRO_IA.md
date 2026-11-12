# Registro de uso de IA

Ferramenta: Codex (OpenAI).

| Interação | Prompt exato | Resultado da IA | Problema ou avaliação | Alteração feita e por quem | Evidência |
| --- | --- | --- | --- | --- | --- |
| Preparação do site | Ver prompt completo abaixo. | Caminhos corrigidos e verificador de recursos criado. | Caminhos incompatíveis com a publicação e referências de logo alteradas foram corrigidos. | Codex alterou caminhos e criou `scripts/verificar_recursos.py`. Nenhuma alteração manual pelo aluno foi observada nesta etapa. | Verificação final: 168 referências e 0 erros; o teste de recurso inexistente foi detectado corretamente. |
| Pipeline CI/CD | Ver prompt completo abaixo. | Codex criou o workflow e documentou seu uso no README. | Os históricos local e remoto divergiram; o conflito no registro foi resolvido preservando a versão local. | Codex configurou CI em pushes e PRs para `main` e CD após CI bem-sucedida em push para `main`. | `python scripts/verificar_recursos.py`: 168 referências locais, 0 erros. Execução remota e publicação ainda não comprovadas no momento do registro. |
| Testes locais | Solicitação de testes locais. | Codex testou o verificador em arquivos temporários e inspecionou o workflow localmente. | O teste revelou que o Windows aceitava um caminho com capitalização incorreta. | Nenhuma alteração no verificador ou workflow; Codex registrou o resultado. | Projeto: 168 referências e 0 erros; o teste de capitalização identificou a limitação. |
| Correção da capitalização | Ver prompt completo abaixo. | Codex analisou e testou a alteração já existente no verificador. | A alteração local preserva a grafia do caminho antes da comparação e passou nos testes no Windows. | A alteração do script já estava presente no início desta interação; sua autoria não foi determinada. Codex atualizou o README e registrou os testes. | Casos temporários: HTML e CSS válidos, recursos ausentes, index ausente, capitalização de arquivo e diretório, espaços e acentos, caminho absoluto e caminho externo passaram. Projeto: 168 referências e 0 erros. |
| Revisão local da pipeline | Ver prompt completo abaixo. | Codex comparou o workflow com o enunciado e simulou uma cópia local dos arquivos rastreados. | A revisão local não executa as ações nem reproduz o empacotamento real. | Nenhuma alteração no workflow ou README; Codex registrou a revisão. | Verificador: 168 referências e 0 erros no projeto e na cópia temporária com 101 arquivos; páginas principais, CSS e dois vídeos presentes. Gatilhos, dependência da CI, condição do CD e permissões conferidos no texto do workflow. |

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
> Acrescente este prompt e os resultados reais ao registro de uso de IA. Faça commit na branch existente e envie-o ao GitHub, atualizando o mesmo PR.

## Prompt completo — correção da capitalização

> Analise scripts/verificar_recursos.py e corrija o problema que faz o verificador aceitar, no Windows, um caminho cuja capitalização difere do nome real do arquivo.
> Preserve as demais verificações e use apenas a biblioteca padrão do Python. Antes de alterar qualquer arquivo, confira o estado local do Git e preserve as alterações existentes, inclusive as que já estão preparadas no índice.
> Execute testes locais em diretórios temporários para comprovar:
> - referências válidas em HTML e CSS;
> - recurso inexistente em HTML e em CSS;
> - ausência do index.html;
> - diferença de maiúsculas e minúsculas no nome de arquivo e de diretório;
> - caminhos com espaços e caracteres acentuados.
> Execute também o verificador no projeto completo. Atualize o README apenas se a correção mudar a limitação documentada. Acrescente ao registro de IA este prompt e os resultados reais, sem inventar informações.
> Não acesse o GitHub nem faça validações externas. Não faça commit, push, PR, merge ou alterações no índice do Git.

## Prompt completo — revisão local da pipeline

> Revise localmente `.github/workflows/ci-cd.yml` em comparação com o enunciado da atividade. Confira os gatilhos para `push` e `pull_request` na `main`, checkout, ambiente, dependências necessárias, execução do verificador e condição do CD após uma CI bem-sucedida em `push` na `main`.
>
> Verifique também se o artefato de publicação contém os arquivos necessários para o site. Execute apenas verificações disponíveis localmente e corrija problemas que puder comprovar. Preserve as alterações existentes do projeto e do índice do Git.
>
> Atualize o README e o registro de IA se necessário, descrevendo exatamente os testes realizados e suas limitações. Não diga que a pipeline executou ou que o site foi publicado sem evidência.
>
> Não acesse o GitHub nem faça validações externas. Não faça commit, push, PR, merge ou alterações no índice do Git.
