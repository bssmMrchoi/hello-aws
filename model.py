import pymysql
from config import Config

con = Config()

db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS guestbook (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(50)  NOT NULL,
    message    VARCHAR(500) NOT NULL,
    created_at DATETIME     DEFAULT CURRENT_TIMESTAMP
) DEFAULT CHARSET = utf8mb4
            """)

def add(item):
    cur.execute("INSERT INTO guestbook (name, message) VALUES (%s, %s)", (item.name, item.message))
    db.commit()
    return cur.lastrowid
