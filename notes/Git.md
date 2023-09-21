## What is Git?

Git is a tool that helps developers track changes in their code, collaborate with others, and manage different versions of their projects. It is the most widely used version control system.

#### It is used for:
- Tracking code changed
- Tracking who made changes
- Coding collaboration

#### What does Git do?

- Manage projects with repositories
- Clone a project to work on a local copy
- Control and track changes with staging and committing
- pull the latest version of the project to a local copy
- push local updates to the main project

![Alt Text](Day 2/image3.png)

Git can be used locally which means it can be used offline to track things within your own machine. This makes it very fast and also means you do not need to link to cloud or internet repository. 

#### The Three States
Git has 3 main states file can reside in; modified, staged, committed. Data in your files will always be in one of these stages.

- Modified - a change has been made to the file but not committed into your database.
- Staged - you have marked a modified file in the current version to go into your next commit snapshot.
- Committed -  data is stored safely in your local database

![Alt Text](Day 2/image1.png)

#### Using Git with Command Line

- `git config` allows Git to recognise who you are
- `cd` changes the current working directory
- `ls` will list the files in the directory
- `git status` shows the status of your working directory
- `git commit -m "commit message"` commits the staged changes