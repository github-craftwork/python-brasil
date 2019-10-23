<details> <summary> Explicação </summary>

Sua conta foi adicionada automaticamente a organização Craftwork. Aqui vai uma explicação sobre como isto aconteceu.

The Actions workflow, auto-approve.yml, é disparado em todos os pull requests. Durante esta oficina, 3 ações síncronas são disparadas. Elas são síncronas devido a flag [`steps`](https://help.github.com/en/articles/workflow-syntax-for-github-actions#jobsjob_idsteps) presente no arquivo YAML, que iremos explicar futuramente neste workshop.

1. hmarr/auto-approve-action@v2.0.0 - Uma ação que automaticamente aprova PRs
2. bdougie/label-when-approved-action@master - Uma ação que adiciona um rótulo específico quando o PR é aprovado. (forcado de puill-reminders/label-when-approved-action)
3. bdougie/automerge-action @ master - Uma ação que fundi pull requests com o rótulo "automerge". (forcado de pascalgn/automerge-action)

Clique nos links para ver o código, cada um trabalha de forma diferente, e isto acontece porque os ambientes virtuais que executam cada uma destas ações é bem específico e executa códigos diferentes. 

</details>

Agora que você viu e entendeu está Ação na prática, vamos implementar nossa primeira Ação. Vá para a [Part 1 desta oficina] (part1-hello-world.md).
