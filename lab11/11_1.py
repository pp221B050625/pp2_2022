import psycopg2
from config import config


def return_by_pattern():
    conn = None
    try:
        names = "SELECT name, number from contacts;"
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(names)
        name_list = cur.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    pattern = input()
    for contact in name_list:
        if pattern in contact[0] or pattern in contact[1]:
            print(contact)


def add_new(name, number):
    conn = None
    # name_input, number_input = input().split()
    sql_exist = "select * from contacts where name = %s;"
    add = """
    INSERT INTO contacts(name, number)
    VALUES (%s, %s);
    """
    update = """
    UPDATE contacts
    set number = %s
    where name = %s;
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_exist, [name])
        name_exist = cur.fetchone()
        if name_exist is None:
            cur.execute(add, (name, number))
        else:
            cur.execute(update, (number, name))
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


def add_list():
    incorrect_list = []
    run = True
    while run:
        name, number = input().split()
        if name == '0' and number == '0':
            run = False

        if len(number) == 4:
            add_new(name, number)
        else:
            incorrect_list.append((name, number))
    return incorrect_list


# print("List of wrong numbers:", add_list())

def pagination():
    lim, offset = input().split()
    sql = """
    select * from contacts limit %s offset %s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (int(lim), int(offset)))
        print(cur.fetchall())
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


# pagination()

def delete():
    conn = None
    del_sql_name = """
    delete from contacts
    where name = %s;
    """
    del_sql_number = "delete from contacts where number = %s;"
    try:
        names = "SELECT name, number from contacts;"
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(names)
        name_list = cur.fetchall()
    except Exception as e:
        print(str(e))

    string = input()
    for contact in name_list:
        if string in contact[0]:
            try:
                print(contact[0])
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute(del_sql_name, [contact[0]])
                conn.commit()
            except Exception as e:
                print(str(e))
        if string in contact[1]:
            try:
                params = config()
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
                cur.execute(del_sql_number, [contact[1]])
                conn.commit()
            except Exception as e:
                print(str(e))
        if conn is not None:
            conn.close()


#delete()