## Git Workflow Guide

Git is a powerful version control system that helps you track changes in your code and collaborate with others. 

### Step 1: Initializing a Git Repository

To start tracking changes in your project with Git, you first need to initialize a Git repository. Open your terminal and navigate to the root directory of your project.

`git init` This command initializes a new Git repository in your project folder.

### Step 2: Adding Files to the Staging Area

`git add`  To add files to the staging area, use the git add command.

### Step 3: Committing Changes

`git commit -m ""` This allows you to commit changes to the Git repository with a  message describing the changes in the quotation marks.

### Step 4: Pushing to a Remote Repository

``` 
git remote add origin 'insert URL'
git push -u origin main
```
The -u flag sets up tracking, so in the future, you can simply use git push without specifying the remote and branch.

This is the basic workflow for using Git to manage your code projects. 

#### What is branching in GitHub?

Branching in GitHub is a way of creating a copy of the code to work on it separately from the main version. 