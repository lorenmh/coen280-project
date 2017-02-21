import os
import sqlalchemy

DB_HOST = os.getenv('DB_HOST', '')
DB_PORT = os.getenv('DB_PORT', '')
DB_USER = os.getenv('DB_USER', '')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', '')

DB_URI = 'postgresql://%s:%s@%s:%s/%s' % (DB_USER, DB_PASSWORD,
                                          DB_HOST, DB_PORT, DB_NAME)

engine = sqlalchemy.create_engine(DB_URI, echo=True)
