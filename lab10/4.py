import psycopg2
from config import config




def insert_contact():
    sql = """
    INSERT INTO contacts(name, number )
    VALUES(%s, %s)  ;
    """
    nam, num = input().split()
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (nam, num))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()


def update_contact():
    sql = """
    update contacts
    set number = %s
    where name = %s;
    """
    nam, num = input().split()
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (nam, num))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()


def delete_contact():
    nam = input()
    sql = """
    delete from contacts
    where name = %s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, [nam])
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()


delete_contact()
