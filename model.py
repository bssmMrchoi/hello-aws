import pymysql
import config as con


db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
cur = db.cursor()
#cur.execute("""





#            """)

def add(item):
    cur.execute("INSERT INTO guestbook (name, message) VALUES (%s, %s)", (item.name, item.message))
    db.commit()
    return cur.lastrowid


#def get_all():

