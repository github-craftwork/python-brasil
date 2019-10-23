
# Part 1: Hello World

Start by creating a [new sandbox repository] (https://github.com/organizations/github-craftwork/repositories/new) in the github-craftwork org to keep everything organized. 

! [] (https://paper-attachments.dropbox.com/s_CDDCC4EC3C7C8C14E8A73684CA9909721C965A1258B4380D90B28E1A4E030470_1570058137257_Screenshot+2019-10-02+16.12.56.png)


_Please add your name to the repository, eg: ** bdougie-sandbox ** _

Your initialized repository already has an action triggered. Click on the Actions tab to see what happens.

! [] (https://paper-attachments.dropbox.com/s_CDDCC4EC3C7C8C14E8A73684CA9909721C965A1258B4380D90B28E1A4E030470_1568391143385_Screenshot+2019-09-13+09.12.12.png)


In the Actions tab, you will have a workflow execution for your new ** hello-world action **. Go ahead and click on your workflow to see the logs.

_Note: These logs are produced by GitHub's [Checks API] (https://developer.github.com/v3/checks/)

! [] (https://paper-attachments.dropbox.com/s_CDDCC4EC3C7C8C14E8A73684CA9909721C965A1258B4380D90B28E1A4E030470_1570058201382_Screenshot+2019-10-02+16.16.33.png)


In the logs, notice that your hello-world action prints - "hello world."


! [] (https://paper-attachments.dropbox.com/s_CDDCC4EC3C7C8C14E8A73684CA9909721C965A1258B4380D90B28E1A4E030470_1568391516459_Screenshot+2019-09-13+09.18.30.png)


Congratulations! You created your first Action, and all you had to do was pop up and click a few buttons 😉.

This workflow was started from the `hello.yml` file. 

The workflow name is important and will be used to identify your Action in the logs.


    # .github / workflows / hello.yml
    on: push # runs when ever there is a push to any branch of the repo
    name: A workflow for my Hello World Action
    jobs:
      build:
        name: Hello world action
        runs-on: ubuntu-latest # useful environment so we can run a simple bash    
        steps:
        - name: hello-world
          run: |
            echo "hello"

** About workflows ** 
You can create a workflow file configured to run on specific events. For more information, see "[Setting Up a Workflow] (https://help.github.com/en/articles/configuring-a-workflow)" and "[Workflow Syntax for GitHub Actions] (https: // help. github.com/en/articles/workflow-syntax-for-github-actions) ".

The basics you need to know is that there is an Action ready for you in the `.github / workflows` folder. Inside you will see that the `hello.yml` file defines a workflow of a Softwarea Software Development Lifecycle (CVDS).

See more about the key concepts of [GitHub Actions] (https://help.github.com/en/articles/about-github-actions#core-concepts-for-github-actions).

One thing to watch for workflows is the ** jobs **.

A `job` is a task composed of steps. Each job is run on a virtual environment instance created from scratch. You can define dependency rules for how jobs are executed in a workflow file. Jobs may run in parallel or be dependent on the status of a previous job and run in sequence. For example, a workflow might have two sequential jobs that build and test code, where the test job is dependent on the status of the build job. If the build fails, the test job will not run.

** runs-on **

GitHub hosts virtual machines with Linux, macOS, and Windows environments. Each job in a workflow runs on a new instance of the virtual environment. All steps in the job execute on the same instance of the virtual environment, allowing actions in that job to share information using the filesystem.

You can specify the vital environment for each job in a workflow. You can configure each job in different virtual environments or run all jobs in the same environment.

** Steps **

A step is a set of activities performed by a job. Each step in a job runs in the same virtual environment, allowing actions in that job to share information using the filesystem. Steps can run commands or actions.

## Part 1a: Environment Variables

Next, let's make our little action a little more advanced by adding a name to the environment variables.

        - name: hello-world
          run: |
            echo "hello $ NAME"
          env:
            NAME: Mary


Committing this change will also trigger the action and you should see the output of your variable in the action logs as `hello Mary`. 

Now let's use existing environment variables to add your name. e.g. GITHUB_ACTOR.


        - name: hello-world
          run: |
            echo "hello $ GITHUB_ACTOR"

See more about the [default environment variables] (https://help.github.com/en/articles/virtual-environments-for-github-actions#default-environment-variables) available for your use. 

You will find in the documentation, in addition to the `GITHUB_ACTOR` variable, the` GITHUB_TOKEN` access variable so that we can perform actions in our own repositories. variables are available for us to perform Actions on our own repos.

[Continue to Part 2] (parte2-issues.md)
