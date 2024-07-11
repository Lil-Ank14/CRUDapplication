import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Lilank1314$#',
                             database='To_Do',
                             charset='utf8mb4')



#Reading all items from items table in To_Do db
def read_items(): 
    with connection.cursor() as cursor: 

        read_table = """SELECT * FROM To_Do.items;"""

        cursor.execute(read_table)
        items = cursor.fetchall()
        
    return items


#Reading specific item from table
def read_item(id):
    with connection.cursor() as cursor:

        read_element = """SELECT content FROM To_Do.items WHERE id = %s;"""

        cursor.execute(read_element, (id,))
        item = cursor.fetchone()

        return item


#Creating new item and inserting into items table
def create_item(content):
    with connection.cursor() as cursor: 

        insert_content = """INSERT INTO To_Do.items (content) VALUES (%s);"""
        cursor.execute(insert_content, (content,))

        connection.commit()


#Updating specific item from table
def update_item(id, content):
    with connection.cursor() as cursor:

        update_content = """UPDATE To_Do.items SET content = %s WHERE id = %s"""
        cursor.execute(update_content, (content, id))

        connection.commit()


#Deleting specific item from table
def delete_item(id):
    with connection.cursor() as cursor:

        delete_content = """DELETE FROM To_Do.items WHERE id = %s;"""
        cursor.execute(delete_content, (id,))
        
        connection.commit()


