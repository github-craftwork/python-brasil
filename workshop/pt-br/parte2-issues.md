# Part 2 Issues 

## Part 2a: Madlibs with Issues 
Working with issues can be trivial, add the action below and ISSUE_TEMPLATE to your project for some fun with issues.

** Allow madlib.yml on master **
Create a `madlib.yml` file in your` .github / workflows` folder with the following content:


    # madlib.yml
    on: issues
    name: Create MadLibs in GitHub Issues
    jobs:
      madlib:
        runs-on: ubuntu-latest
        steps:
        - uses: actions / checkout @ master
        - uses: bdougie/variables-in-markdown@v0.1.4
          env:
            GITHUB_TOKEN: $ {{secrets.GITHUB_TOKEN}}

Now open an issue using the MadLib template to see this working. (If you are familiar with MadLibs, feel free to change some variables.)

Note: Depending on your features and WiFi, you may need to refresh the page to see the issue refresh. 

Once you have successfully created a MadLib, take a look at the [Markdown Variables] action page (https://github.com/marketplace/actions/variables-in-markdown) to learn more about this automation.

[Continue to Part 3] (parte3-ci.md)
