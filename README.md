# User Management System

Backend for web application "User Management Syatem".
With this app users can register, log in, view/update their profiles, 
and perform basic CRUD operations on user accounts. User can view, update and delete only his own account.
Authorisation and authentication by JWT token. 
Password are hashed and safely stored in database.
<br>
<br>
### Stack: Python, Django, DRF, Django ORM, PostgreSQL, Pytest
<br>

### Dependencies:


<table>
    <tr>
        <th>python</th>
        <th>3.11</th>
    </tr>
    <tr>
        <th>django</th>
        <th>4.2.4</th>
    </tr>
    <tr>
        <th>djangorestframework</th>
        <th>3.14.0</th>
    </tr>
    <tr>
        <th>psycopg2-binary</th>
        <th>2.9.6</th>
    </tr>
    <tr>
        <th>djangorestframework-simplejwt</th>
        <th>5.2.2</th>
    </tr>
    <tr>
        <th>python-dotenv</th>
        <th>1.0.0</th>
    </tr>
    <tr>
        <th>pytest</th>
        <th>7.4.0</th>
    </tr>    <tr>
        <th>pytest-django</th>
        <th>4.5.2</th>
    </tr>
</table>
<br>

## Installation:

### Clone repository:
```git clone git@github.com:Dm1triiSmirnov/user_management_system.git```
<br><br>

### Create & setup database:

- Connect to PostgreSQL: <br>
```sudo postgres psql``` <br>
 <br>

- Create DB:<br>
```CREATE DATABASE user_management_system_db;```<br>
 <br>
-  Create user & set password:<br>
CREATE USER username WITH PASSWORD 'password';<br>
 <br>
-  Set encoding UTF-8:<br>
```ALTER ROLE username SET client_encoding TO 'utf8';```<br>
 <br>
-  Set isolation level: <br>
```ALTER ROLE username SET default_transaction_isolation TO 'read committed';```<br>
 <br>
-  Set time zone UTC: <br>
```ALTER ROLE username SET timezone TO 'UTC';```<br>
 <br>
-  Grant permissions for user: <br>
```GRANT ALL PRIVILEGES ON DATABASE user_management_system_db TO username;```<br>
 <br><br>

### Set environment variables in .env as following:
SECRET_KEY='secret key for your ptoject'<br>
DB_NAME='user_management_system_db'<br>
DB_USER='username'<br>
DB_PASSWORD='password'<br>
DB_HOST=localhost<br>
DB_PORT='5432'<br><br>


### Create superuser for your project:
```python3 manage.py createsuperuser --email example@example.com --username user```
<br><br>

### Create & apply migrations:<br>
```make migrations```
<br><br>

### Run server:
```make run```

### Now you can use following Endpoints:
1. User register: <br>
```POST /auth/register/```
<br><br>
Request Body:
<br>
{<br>
    "email": "your email",<br>
    "username": "your username",<br>
    "password": "your password",<br>
    "password2": "repeate password" <br>
}
<br><br>
2. User login & obtain tokens for authentication: <br>
```POST /auth/token/```
<br><br>
Request Body:
<br>
{<br>
    "username": "your email or username",<br>
    "password": "your password",<br>
}
<br><br>
3. Retrieve the profile information of a user: <br>
```GET /user/profile/{username}/```
<br><br>
Add header to your request: 
<br>
"Authorization: Bearer your_access_token"
<br><br>
4. Update the profile information: <br>
```PATCH /user/profile/{username}/```
<br><br>
Add header to your request: 
<br>
"Authorization: Bearer your_access_token"
<br><br>
Request Body (add any information that you want to update):
<br>
{<br>
    "first_name": "John",<br>
    "last_name": "Smith",<br>
}
<br><br>
5. Delete the user account: <br>
```DELETE /user/profile/{username}/```
<br><br>
Add header to your request: 
<br>
"Authorization: Bearer your_access_token"
<br><br>
