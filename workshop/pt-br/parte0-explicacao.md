<details> <summary> Explanation </summary>

Your account has been automatically added to the org in a few ways. Here is an explanation of how this happened.

The Actions workflow, auto-approve.yml, is triggered on all pull requests. During this workflow, 3 synchronous actions are triggered. They are synchronous due to the [`steps`] flag (https://help.github.com/en/articles/workflow-syntax-for-github-actions#jobsjob_idsteps) in the YAML file, which we will cover later.

1. hmarr/auto-approve-action@v2.0.0 - An action that automatically approves PRs
2. bdougie / label-when-approved-action @ master - An action that adds a specified label when approved. (puill-reminders / label-when-approved-action fork)
3. bdougie / automerge-action @ master - An action that merges pull requests with the label "automerge". (forked from pascalgn / automerge-action)

Click on the links to see the code, each one is worked differently, this is because the actions are virtual environments that run any specified and arbitrary code. 

</details>

Now that you have seen it in practice, let's implement our first Action. Proceed to [Part 1 of this workshop] (part1-hello-world.md).
