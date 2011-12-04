# Piloto de Sistema para Controle De Requisitos de Software

**Autor**: Cássio Rogério Eskelsen
Disciplina Engenharia de Software 1
 
## Objetivo

O objetivo dessa ferramenta é ser um piloto de ferramenta de Controle de Requisitos de Software com o  diferencial de armazenar os requisitos junto ao código fonte do sistema final.

## Motivação

Uma das principais dificuldades que pode ser percebida na Gestão de Requisitos é a dificuldade de consultá-los rapidamente durante o desenvolvimento, bem como mantê-los atualizados.
A ferramenta proposta armazena, além de no banco de dados interno, o conteúdo do requisito junto ao repositório do código fonte, utilizando para isso ferramenta de controle de versão.

## Funcionamento

O sistema permite cadastrar vários projetos de software. No cadastro do projeto é apontado em qual diretório está ou estará o código fonte do sistema. Se esse diretório ainda não for controlado via ferramenta de controle de versão, um “repositório” é automaticamente inicializado. Também é criada um subdiretório de nome “requisities”
Nesta versão piloto está sendo utilizando o sistema de controle de versão distribuído GIT[1] .
O cadastro de projeto permite ainda o cadastro dos atores envolvidos com o projeto.

Os tipos de requisito (Funcional, Não Funcional, Regra de Negócio, etc) podem ser livremente cadastro.

Ao cadastrar um Requisito é criado automaticamente um arquivo texto no diretório “requisities” com o seguinte padrão de nomes: Sigla do Tipo de Requisito + Número do Requisito + extensão fixa “.md”. Ou seja, o requisito funcional 001 irá, por exemplo, criar um arquivo “RF001.md”.

Após a criação do arquivo com o requisito o sistema faz automaticamente um “commit” no no GIT com a mensagem “Criação .....” ou “Alteração .....” dependendo da situação.

Ao consultar um requisito no sistema são listadas rodas as revisões do requisito, permitindo visualizar rapidamente um instantâneo do requisito naquela versão.

## Ferramentas Utilizadas

Para o desenvolvimento foi utilizada a Linguagem Python versão 2.7[2]  juntamente com o framework web Django[3].  Para a interação com o GIT foi utilizada a biblioteca “GitPython”[4]. Os dados ficam armazenados uma base de dados SQLITE, cujo engine já está incorporado ao Python.

## Código Fonte

Todo código fonte do projeto está disponibilizado no repositório comunitário GitHub[5]

## Instalação

1. **Instalar as dependências básicas**: Python e GIT
2. **Instalar a biblioteca GitPython** conforme instruções encontradas no link https://github.com/gitpython-developers/GitPython/blob/master/README.rst
3. **Instalar o Django** conforme instruções encontradas em https://docs.djangoproject.com/en/1.3/intro/install/
4. **Efetuar o download do código** através da instrução:
got clone git://github.com/cassioeskelsen/GerenciaDeRequisitos.git

## Execução

Para executar usando o servidor de testes do projeto Django, siga os seguintes passos:

1. cd GerenciaDeRequisitos
2. python manage runserver . Isso irá iniciar um servidor em http://localhost:8000
3. Acesse o endereço http://localhost:8000 . O usuário e senha inicial são master / master

## Links

[1] http://git-scm.com/
[2] http://python.org/
[3] https://www.djangoproject.com/
[4] http://gitorious.org/git-python
[5] https://github.com/cassioeskelsen/GerenciaDeRequisitos

## Projetos com o mesmo propósito:

[1] GRINGS, Claiton Luís e Miriam Sayão. OpenReq: uma Ferramenta para Auxílio à Gerência de Requisitos, acessado em 04/12/2011, http://wer.inf.puc-rio.br/WERpapers/artigos/artigos_WER09/grings.pdf

[2] DE GRANDE, José Inácio e Luiz Eduardo G. Martins.SIGERAR: Uma Ferramenta para Gerenciamento de Requisitos, acessado em 04/12/2011, http://www.scribd.com/doc/55804055/Ferramentas-Gratuitas-para-Gerencia-de-Requisitos

[3] WILHELM, Ivan. Ferramenta Web de Apoiuo à Elicitação de Requisitos de Software, acessado em 01/12/2011, http://www.bc.furb.br/docs/MO/2010/341406_1_1.pdf
