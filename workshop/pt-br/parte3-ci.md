
# Parte 3: Integração Contínua (Continuous Integration - CI) 

_Nota: A seção a seguir necessita que você tenha criado um repositório na sua própria conta. Você precisa garantir que tenha acesso a página do Github [Actions](https://github.com/features/actions)._

A seguir vamos iniciar um novo projeto nos seus repositórios pessoais (**não os da organização github-craftwork**) usando o template [github-craftwork/ci-template](https://github.com/github-craftwork/ci-template/generate). Os conteúdos do projeto foram obtidos da introdução Plurasight, que descobre qual o número da semana atual é hoje. 

![](https://user-images.githubusercontent.com/5713670/67403798-fb875180-f5a1-11e9-8989-2650dcbb20fd.png)


**Criar CIs pull requests**

Para desenvolver um processo de Workflow no GitHub que aplica Actions para automatizar o processo de integração contínua, você pode começar adicionando um arquivo de workflow inicial no diretório `.github`. Na tela inicial do seu repositório, encontre e navegue até a aba **Actions**.


![](https://user-images.githubusercontent.com/5713670/67405421-41ddb000-f5a4-11e9-8cb4-94f22aed4296.png)


Na página de Actions você deve ver 3 opções de workflow Python. Encontre a opção Python Application workflow e clique no botão `Set up this workflow`.

_Nota: O repositório [actions/starter-workflows](https://github.com/actions/starter-workflows) contém muitos arquivos workflow de amostras._

O assistente de Workflow Actions irá instalar a amostra do workflow selecionado no seu repositório, dentro do diretório `.github`. Você pode editar o nome do arquivo e o seu conteúdo na tela fornecida.

![Screenshot 2019-10-09 17 02 03](https://user-images.githubusercontent.com/5713670/67406658-e01e4580-f5a5-11e9-8d8c-6749ae6f9720.png)

Faça commit do arquivo `pythonpackage.yml` para o branch master para completar este processo de criação do nosso primeiro workflow de CI. 

O diretório `.github/workflows/` irá incluir o conteúdo abaixo:

name: Python application

```
on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        pip install flake8
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pip install pytest
        pytest
```

_Observe que o nosso workflow está rodando com uma estratégia de 3 versões de python. Será importante saber isso posteriormente._ 

Devido ao fato da nova Action de CI estar rodando a cada push, você já deve ter um workflow rodando.

![python package workflow](https://user-images.githubusercontent.com/5713670/67407777-8d458d80-f5a7-11e9-8827-40d19dde78ad.png)


Perceba que precisaremos escrever um teste para rodar como parte do nosso CI. Encontre o arquivo `00_empty_test.py` com o conteúdo abaixo:

```py
# tests/00_empty_test.py
def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)

    It looks for them in modules whose name contains "test"
    (by default)
    """
    pass

```

O resultado do último push para o branch master deve ser parecido com o desta imagem:

![](https://user-images.githubusercontent.com/4427768/67440385-8599df00-f5cf-11e9-9152-e0f19a5e8527.png)


Adicione o teste acima utilizando a UI, mas ao invés de commitar diretamente no branch master, abra um pull request para disparar o workflow de CI novamente. 

Nós não criamos um pull request até agora, então por favor perceba que você pode ver todos os workflows sendo disparados pelo GitHub [Check Suite](https://developer.github.com/v3/checks/). Todas as Action dos Workflows estão sendo alimentadas pela API desta funcionalidade. E como estamos falando do assunto, o bot do GitHub Actions é construído usando o framework [GitHub App](https://developer.github.com/apps/), que já ficou popular entre um grande número do nosso [Marketplace](https://github.com/marketplace) e ecossistema de parceiros.

![CI pass](https://user-images.githubusercontent.com/5713670/67408875-3b9e0280-f5a9-11e9-8751-da299236cbbb.png)

Assim que todos os testes tiverem passado, faça merge do pull request e vamos seguir em frente para completar o próximo passo. 
    
## Parte 3b: Rascunho e Auto publicar uma versão release
CI é frequentemente acoplada com a ideia de Entrega contínua (do inglês Continuous Delivery - CD). As próximas duas seções cobrirão automatizar seus projetos com gerenciamento de versões release.

**Adicione seu workflow de release**
Você pode usar a [Action do Github para gerar rascunhos de Releases](https://github.com/marketplace/actions/release-drafter) em um [Workflow de Actions](https://help.github.com/en/articles/about-github-actions) através da configuração de um arquivo YAML para workflow, ex: `.github/workflows/release-management.yml`, com o seguinte conteúdo:


    name: Release Management
    
    on:
      push:
        # branches to consider in the event; optional, defaults to all
        branches:
          - master
    
    jobs:
      update_draft_release:
        runs-on: ubuntu-latest
        steps:
          # Drafts your next Release notes as Pull Requests are merged into "master"
          - uses: toolmantim/release-drafter@v5.2.0
            env:
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

Uma vez que você tenha adicionado o Rascunho para Releases ao seu repositório, ele deve ser habilitado adicionando um arquivo de configuração `.github/release-drafter.yml` para cara repositório.

**Adicione o template de release**
Crie o seguinte arquivo `.github/release-drafter.yml` em um repositório e faça commit na sua branch master:

    template: |
      ## What’s Changed
    
      $CHANGES

**Faça uma mudança**
Navegue até qualquer arquivo no repositório and mude o conteúdo para algo direrente. 

Conforme os pull requests são mergeados, um rascunho da release é mantido atualizado com as mudanças, pronto para ser publicado quando você estiver pronto:

![Screenshot of generated draft release](https://github.com/toolmantim/release-drafter/raw/master/design/screenshot.png)


Para testar este workflow, edite o seu rascunho usando a tag existente que foi criada para ele. Uma vez concnluído, siga em frente para o próximo passo no projeto para concluir esta etapa.

![](https://paper-attachments.dropbox.com/s_CDDCC4EC3C7C8C14E8A73684CA9909721C965A1258B4380D90B28E1A4E030470_1569513609522_Screenshot+2019-09-26+08.59.53.png)


**Publicar o seu pacote python**
Você pode publicar seu pacote python usando o iniciador de templates no assistente de Actions.

![python package workflow ](https://user-images.githubusercontent.com/5713670/67405981-fb3c8580-f5a4-11e9-8dbe-4318cf7a4e9b.png)


[Continue para a Parte 4](part4-bonus.md)
