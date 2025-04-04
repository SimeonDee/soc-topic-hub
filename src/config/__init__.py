import os

# [database Config]
DBMS_NAME = "mysql"
DB_USERNAME = "user"
DB_PASSWORD = "PASS"
DB_HOST = "http://127.0.0.1"
DB_NAME = "soc_topic_hub_db"
SQLALCHEMY_DATABASE_URI = (
    f"{DBMS_NAME}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# [secrets]
SECRET_KEY = "secretxyz"
