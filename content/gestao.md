Title: Git Flow - Como organizar o seu projeto e ter branchs e commits com significado
Date: 2020-05-03 11:01
Category: Boas práticas
O que é o GitFlow?
Um framework que descreve como criar e gerenciar branches em projetos de TI.

Develop e Master Branches
Ao invés de apenas uma branch, o workflow utiliza duas branches para salvar o histórico do projeto. A master armazena o histórico oficial das releases e a develop realiza as integrações com as novas features que são implementadas.

A branch master armazena o histórico de releases e tem a versão final de produção. Nunca devemos desenvolver diretamente na master.

A branch develop é usada para integrar com as novas features/bugs. Todo o histórico de commits ficam armazenados na develop. 

Por padrão os projetos do Git já possuem uma branch Master, então nós só precisamos adicionar a branch developer. Para fazer isso execute o comando abaixo:

git checkout -b develop

Feature/Bug Branches

Para cada nova feature/bug se deve criar uma nova branch. Quando o desenvolvimento da feature está completo, fazer merge com a branch develop.
features/bugs nunca devem ser mergeadas diretamente na master.

Como criar uma nova branch
git checkout develop
git checkout –b feature/new_feature

Quando concluir o desenvolvimento, copiar a branch para a branch develop
git checkout develop
git merge feature/new_feature

Release Branches
Uma feature já é suficiente para criar uma release, mas nada impede de unir várias features em uma.
Release é um “pacote fechado” que já pode ser levado para produção. 

Como criar uma nova branch
git checkout develop
git checkout –b release/new_release

Quando concluir a validação do release, copiar a branch para a branch master
git checkout master
git merge release/new_release

Hotfix Branches
São alterações que devido a sua criticidade são realizadas diretamente na master.  
As alterações da hotfix devem ser propagadas para a master e para a develop.

Criando uma branch hotfix copiando as informações da Master
git checkout master
git checkout –b hotfix_branch

Quando concluir o desenvolvimento, realizar merge das alterações com Develop e Master. Após isso deletar a branch hotfix.
git checkout master
git merge hotfix_branch
git checkout develop
git merge hotfix_branch
git branch -d hotfix_branch

GitFlow Commands
Para facilitar a implantação do GitFlow existe uma biblioteca para o git que facilita a criação e a manutenção da infraestrutura.  Vamos passar aqui pelos principais comandos dessa biblioteca.
git flow init – Inicializa o projeto git e já cria todas as branches necessárias. Master, development etc.
git flow feature start new_feature – Cria uma nova branch chamada new_feature copiando as informações da branch develop e a coloca dentro do grupo de features/. Além disso ele faz checkout e coloca a new_feature como branch atual.
git flow feature finish new_feature – Copia as informações da new_feature para develop e apaga a branch new_feature. Esse comando já realiza o merge e estando tudo ok já faz checkout devolta para a branch develop
git flow release start 1.0 – ler as informações atuais da branch develop e cria uma branch de release e faz chechout para essa nova branch.
git flow release finish 1.0 – Copia as informações da branch 1.0 para a master e para develop  e apaga a branch 1.0. Esse comando já realiza o merge e estando tudo ok já faz checkout para a branch master.
git flow hotfix start hotfix_branch – Copia as informações que estão em produção e cria uma nova branch. Após isso faz checkout para a nova branch criada
git flow hotfix finish hotfix_branch - Copia as informações da branch 1.0 para a master e para develop  e apaga a branch 1.0. Esse comando já realiza o merge e estando tudo ok já faz checkout para a branch develop.


Git Commit Message
Abaixo boas práticas na hora de definir os commits
Commits atômicos – Aplique as mudanças assim que você as fizer. Cada commit deve estar relacionado a uma única alteração/correção. Se você tiver que adicionar um “e” a sua mensagem de commit provavelmente você não está realizando um commit atômico.
Referencie os chamados nos commits – É importante que a cada commit você referencie qual chamado ele está relacionado(quando isso é possível). Para os repositórios do redmine basta adicionar uma # e o número do chamado que automaticamente ele vinculará o commite. Exemplo:   refs #51398
Utilize o padrão Git Karma – É uma forma de escrever mensagens de commit utilizando o seguinte template: 

<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
  
<type> - Valor sempre em minúsculo que pode ser uma das seguintes opções: 
feat (nova feature)
fix (resolução de algum bug)
docs (mudança ou adição de documentação)
style (alterações na formatação do projeto)
refactor (refatorando um Código em produção, ex. renomear uma variável)
test (adição de testes, correção nos testes)
chore (Eliminando lixos do código, trechos de códigos não usados etc.)
<optional scope>: 
init
runner
watcher
config
web-server
proxy
etc.
É possível não colocar scope, caso a mudança seja algo global ou tenha dificuldade em escolher apenas um componente.
<description> Breve resumo das alterações do código. Exemplo: fix: Correção de parsing em array, quando tinhamos vários espaços na string .

<body>: longos bodys devem vir depois de descrições pequenas dando uma contexto maior para o commit. O body deve começar com uma linha branca logo após a descrição.  

<footer>: O footer deve começar com uma linha branca logo após o body. No footer adicionamos a referência ao chamado/tarefa relacionada(Caso exista). Em caso de mais de um chamado referenciado separar por virgulas. 
Exemplo: Close #432, #443

 Breaking changes: alteração que inclui uma modificação que quebra a compatibilidade com versões anteriores. Importante salientar a forma que devemos agir para corrigir a incompatibilidade. Exemplo: 
BREAKING CHANGE:

`port-runner` linha de comando foi alterada para `runner-port`.

Para migrar o projeto, altere todos os commandos, onde você usa `--port-runner`
para `--runner-port`.

Exemplo de commit:
fix(middleware): garante que o cabeçalho atende ao RFC 2616

Adiciona uma nova dependência, use `range-parser`. Adapta os testes das dependências anteriores para esse caso.

Fixes #2310

FAQ
Por que utilizar esse padrão de git flow?
Ajudará as pessoas de fora do projeto a identificar onde está a versão atual de produção e também quais as features e bugs estão sendo desenvolvidas no momento.
Facilitará a criação de scripts automatizados para realizar deploy, testes etc, contribuindo assim para a implantação de uma cultura mais Devops na empresa.
Em que momento fazer a homologação?
O padrão não define em que momento exato devemos fazer a homologação das alterações, mas nós acreditamos que existem dois momentos que são bons para isso, ou quando a alteração está na branch release ou quando está na branch de feature/bug.
Quando sei se é um Hotfix ou é um bug?
Qualquer melhoria/fix/bug urgente que não pode esperar para que façamos todo o processo do flow deve ser tratado como hotfix. Importante que a hotfix está uma exceção e não pode ser a regra do projeto.
Caso surjam ajustes na branch de release onde fazer os ajustes?
A ideia é que na release não aconteçam grandes alterações, se espera que o código já esteja bem maduro nesse momento, mas caso ocorram, as alterações na própria branch não sendo necessário criar outras.

Quando duplicar uma branch de feature em duas?
Surgiu uma demanda em quanto estava fazendo o desenvolvimento, as demandas são complementares ? Elas devem subir juntas? É preciso analisar caso a caso, mas em geral se a nova demanda possui um tamanho significativo é recomendado criar uma nova branch para ela.

Referências

