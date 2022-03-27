import sqlite3
from sqlite3 import Error


def create_table(conn, sql_to_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_to_create_table)
        return conn
    except Error as e:
        print(e)


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def add_product(conn, product):
    sql = '''INSERT INTO product (product_name, product_title, price, quantity) 
        VALUES (?, ?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)
    return None


def update_quantity_by_id(conn, product):
    sql = '''UPDATE product SET quantity = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_price_by_id(conn, product):
    sql = '''UPDATE product SET price = ? WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def print_table(conn, rows):
    sql = '''SELECT * FROM product '''
    try:
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_product_by_price_quantity(conn, limit, limit1):
    sql = '''SELECT * FROM product WHERE price <= ? and quantity <= ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (limit, limit1))
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


def delete_product_by_id(conn, id):
    sql = '''DELETE FROM product WHERE id = ?'''
    try:
        c = conn.cursor()
        c.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)

def search_func(conn, word):
    sql = '''SELECT * FROM product WHERE product_name like ? '''
    try:
        c = conn.cursor()
        c.execute(sql, [word])
        rows = c.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


database = r'hw.db'
conn = create_connection(database)
sql_create_table_product = '''
CREATE TABLE product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR (200) NOT NULL,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (8, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''
print_table(conn, database)
if conn is not None:
    print('Connected Successfully')
    # select_product_by_price_quantity(conn, 100, 5)
    search_func(conn, '%toy%' )
    # update_quantity_by_id(conn, (3, 10))
    # update_quantity_by_id(conn, (2, 5))
    # update_price_by_id(conn, (80, 3))
    # delete_product_by_id(conn, 1)

    # create_table(conn, sql_create_table_product)
    # add_product(conn, ('Apple', 'Juicy Fresh', 70, 50))
    # add_product(conn, ('Orange', 'FRESH', 120, 20))
    # add_product(conn, ('Banana', 'FRESH', 100, 45))
    # add_product(conn, ('WaterMelon', 'FRESH', 40, 70))
    # add_product(conn, ('Bread', 'FRESH', 25, 30))
    # add_product(conn, ('Energy Drink', 'Flash', 60, 50))
    # add_product(conn, ('Pie', 'PewDie', 450, 5))
    # add_product(conn, ('Chocolate Stick', 'Snickers', 50, 90))
    # add_product(conn, ('Chocolate Stick', 'Twix', 50, 88))
    # add_product(conn, ('Potato', 'FRESH', 20, 14))
    # add_product(conn,('Tomato', 'FRESH', 50, 75))
    # add_product(conn, ('Chemistry', 'MIF', 40, 15))
    # add_product(conn, ('Chemistry', 'AOS', 69, 12))
    # add_product(conn, ('Toy', 'Spider-Man', 780, 2))
    # add_product(conn, ('Toy', 'Super-Man', 780, 1))
    # add_product(conn, ('Toy', 'Iron-Man', 780, 3))
    # add_product(conn, ('Toy_Soft', 'Bad_Women', 600, 3))

