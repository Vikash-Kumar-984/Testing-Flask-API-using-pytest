# Testing-Flask-API-using-pytest

This repository contains the end to end project of frontend and backend for Machine Learning Model (APIs) on babies.csv dataset.

1 ounce = 28 grams

Gestation = 9 Months (280 Days)

Serialization: It converts the whole code into the binary format to the pickel file

pip freeze > requirements.txt : To import all the requirements(like pandas, scikit-learn, gunicorn,etc.) to requirements.txt file

model.pkl will be moved from model folder to home folder

# Uninstall Incompatible Packages

* pip uninstall numpy pandas matplotlib -y

# Reinstall Clean Versions

* pip install --upgrade pip setuptools wheel

* pip install numpy pandas matplotlib

# Restart VS Code

After installation:

  * Close all terminals

  * Restart VS Code

  * Open your project again

# Pro Tip: Use a Virtual Environment

To avoid these issues in the future, create a project-specific environment:

* python -m venv venv

* .\venv\Scripts\activate      <!--# Windows-->

* pip install numpy pandas matplotlib

Then in VS Code:

    * Open Command Palette (Ctrl+Shift+P)

    * Type Python: Select Interpreter

    * Choose your venv environment

# Other error (.\myvenv\Scripts\activate) Failed in terminal

If PowerShell is blocking script execution, which includes the activate.ps1 script used to activate Python virtual environments on Windows.

1. Open a new PowerShell terminal in VS Code as usual

2. Run this command in the terminal:

     * Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Type Y when prompted, then press Enter

4. Now try again:

    * .\myvenv\Scripts\activate

This will now work and allow script activation.





# Git Setup

git init

git status #to track untracked file to be commit

git add . #to add all the files from local to github cloud

git commit -m "first commit"

git branch -M main #Define main branch

git remote add origin https://github.com/Vikash-Kumar-984/Machine-Learning-Model-API-Frontend-and-Backend.git #to add particular code to given origin

git push -u origin main #just pushing the code

# Code Changes Commit

  * git status #After changing the code

  * git add .

  * git commit -m "Changes in code commit"

  * git push -u origin main
