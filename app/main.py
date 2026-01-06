from db.mysql_connection import DBConnection


db = DBConnection()
conn = db.get_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("select * from people") 
    people = cursor.fetchall()

    for p in people:
        print(p)
