""""
git --version

git config --global user.name ""
git config --global user.mail ""

git config --list


git help config
git config --help

GETTING STARTED

git init
ls -la
rm -rf .git

git status

touch .gitingnore
(Add file that won't be added)
.DS_Store
.project
*.pyc

ADD FILES TO STAGING AREA

git add -A
git status
git add file

REMOVE FILES FROM STAGING AREA

git reset

git status

COMMITING FILES

git add -A
git commit -m ""
git status
git log

CLONING A REMOTE REPO

git clone <url> <where to clone>

git clone ../remove_repo.git

VIEWING INFORMATION ABOUT THE REMOTE REPOSITORY

git remote -v
git branch -a

PUSHING CHANGES

git diff
git status
git add -A
git commit -m "Modified"

git pull origin master
git push origin master

git remote add origin url
git push -u origin master

COMMON WORKFLOW

git branch name
git checkout name

PUSH BRANCH TO REMOTE AFTER COMMIT

git push -u origin branchname
git branch -a

git pull
git push

MERGE A BRANCH

git checkout master
git pull origin master
git branch --merged
git merge branchname
git push origin master

DELETING A BRANCH

git branch --merged
git branch -d branchname
git branch -a
git push origin --delete branchname

""""
