import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Lilank1314$#',
                             database='To_Do',
                             charset='utf8mb4')




read_table = """SELECT content FROM To_Do.items;"""

def read_items(): 
    with connection.cursor() as cursor: 
        read_table = """SELECT content FROM To_Do.items;"""

        cursor.execute(read_table)
        items = cursor.fetchall()
        

    return items

def create_item(content):
    with connection.cursor() as cursor: 
        insert_table = """INSERT INTO To_Do.items (content) VALUES (%s);"""
        cursor.execute(insert_table, (content,))

        connection.commit()
        

def update_item(index, content):
    with connection.cursor() as cursor:
        id = index + 1
        update = """UPDATE To_Do.items SET content = %s WHERE id = %s"""
        cursor.execute(update, (content, id))

        connection.commit()
    

def delete_item(index):
    with connection.cursor() as cursor:

        id = index + 1
        delete = """DELETE FROM To_Do.items WHERE id = %s;"""
        cursor.execute(delete, (id,))
        reorder_items()
        reset_auto_increment()
        connection.commit()

def reorder_items():
    with connection.cursor() as cursor:
        
        cursor.execute("SELECT id FROM To_Do.items ORDER BY id;")
        items = cursor.fetchall()

        
        for index, item in enumerate(items):
            new_id = index + 1
            old_id = item[0]
            cursor.execute("UPDATE To_Do.items SET id = %s WHERE id = %s;", (new_id, old_id))
        
        connection.commit()

def reset_auto_increment():
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE To_Do.items AUTO_INCREMENT = 1;")
        connection.commit()
