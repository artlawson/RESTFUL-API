#config .py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQUALCHEMY_DATABASE_URI = 'sqlite:///' + os.join(basedir, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

