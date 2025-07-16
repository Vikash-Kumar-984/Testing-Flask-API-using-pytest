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

# HTTP Response Status Code

# Successful Responses:

**200 OK:**

The request was successful, and the server returned the requested data. This is the standard response for a successful API call. 


**201 Created:**

The request was successful, and a new resource was created on the server (e.g., after a POST request). 


**204 No Content:**

The request was successful, but there is no content to send back in the response body. 


# Client Error Responses (4xx):

**400 Bad Request:**

The server could not understand the request due to invalid syntax or missing parameters.

**401 Unauthorized:**

The request requires authentication, but the provided credentials are not valid or missing. This often means the user is not logged in or their session has expired.

**403 Forbidden:**

The server understands the request, but it's refusing to authorize it. This usually means the user is authenticated but lacks the necessary permissions to access the resource.

**404 Not Found:**

The requested resource could not be found on the server.

**405 Method Not Allowed:**

The HTTP method used (e.g., POST, GET, PUT) is not supported for the requested resource.

**429 Too Many Requests:**

The client has sent too many requests in a given amount of time and has been rate-limited. 

# Server Error Responses (5xx):

**500 Internal Server Error:**

 An unexpected error occurred on the server while processing the request.

**503 Service Unavailable:**

 The server is currently unavailable, possibly due to maintenance or overload. 


# Authentication-Specific Considerations:

**401 Unauthorized:**

This is the most direct response for authentication failures. If a user attempts to access a protected resource without providing valid credentials, they will receive a 401.

**403 Forbidden:**
If a user is authenticated but does not have the necessary permissions to access a particular resource, the server will typically return a 403.

**401 vs 403:**

The distinction between 401 and 403 can be subtle. Generally, 401 indicates a lack of authentication credentials, while 403 indicates a lack of authorization, even with valid credentials. 

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
