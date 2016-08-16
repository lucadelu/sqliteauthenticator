from jupyterhub.auth import Authenticator

from tornado import gen
from traitlets import Unicode
import re

import sqlite3

class SqliteAuthenticator(Authenticator):
    db_path = Unicode(
        config = True,
        help = 'Path to SQLite database'
    )

    db_table = Unicode(
        config = True,
        help = 'SQLite table containing user and password'
    )

    db_name = Unicode(
        config = True,
        help = 'Column name containing users'
    )

    db_passwd = Unicode(
        config = True,
        help = 'Column name containing passwords'
    )

    valid_username_regex = Unicode(
        r'^[a-z][.a-z0-9_-]*$',
        config=True,
        help="""Regex to use to validate usernames before sending to SQLite
        """
    )

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        password = data['password']

        # Protect against invalid usernames as well as LDAP injection attacks
        if not re.match(self.valid_username_regex, username):
            self.log.warn('Invalid username')
            return None

        # No empty passwords!
        if password is None or password.strip() == '':
            self.log.warn('Empty password')
            return None

        conn = sqlite3.connect(self.db_path)
        curs = conn.cursor()
        curs.execute()
