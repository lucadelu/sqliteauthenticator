# sqliteauthenticator
Simple SQLite Authenticator Plugin for JupyterHub

## Installation ##

## Usage ##

You can enable this authenticator with the folling lines in your
`jupyter_config.py`:

```python
c.JupyterHub.authenticator_class = 'sqliteauthenticator.SQLiteAuthenticator'
```

### Required configuration ###
All the following option must be set before the SQLite Authenticator can be used:

#### SQLiteAuthenticator.db_path ####
The full path to the SQLite database

#### SQLiteAuthenticator.db_table ####
The name of the table containing information about user and password

#### SQLiteAuthenticator.db_name ####
The name of column containing the users

#### SQLiteAuthenticator.db_passwd ####
The name of column containing the passwords

