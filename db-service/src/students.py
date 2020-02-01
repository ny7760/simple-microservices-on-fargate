import json
import mysql.connector as mydb
import os


def get_students():
    conn = mydb.connect(user=os.environ['DB_USER'], passwd=os.environ['DB_PASS'],
                        host=os.environ['DB_HOST'], port=os.environ['DB_PORT'])

    cur = conn.cursor()
    sql_qry = 'select id, name, score from DB01.students;'
    cur.execute(sql_qry)

    rows = cur.fetchall()

    results = [{"id": i[0], "name": i[1], "score": i[2]} for i in rows]
    return_json = json.dumps({"students": results})
    cur.close()
    conn.close()

    return return_json


if __name__ == '__main__':
    print(get_students())
