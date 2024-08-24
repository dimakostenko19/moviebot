import mysql.connector
from config import host, user, password, database

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS films_data(
    films_code INT PRIMARY KEY,
    films_name VARCHAR(255)
)
""")

async def add_film(films_code, films_name):
    sql = "INSERT INTO films_data (films_code, films_name) VALUES (%s, %s)"
    cursor.execute(sql, (films_code, films_name))
    conn.commit()

async def get_Allfilms(type="*"):
    sql = f"SELECT {type} FROM films_data"
    cursor.execute(sql)
    return cursor.fetchall()

async def get_films(code):
    sql = f"SELECT * FROM films_data WHERE films_code = '{code}'"
    cursor.execute(sql)
    return cursor.fetchall()

async def delete_film(code):
    sql = f"DELETE FROM films_data WHERE films_code = '{code}'"
    cursor.execute(sql)
    conn.commit()

async def update_film(code, new_code, name):
    sql = f"UPDATE films_data SET films_code = '{new_code}', films_name = '{name}' WHERE films_code = '{code}'"
    cursor.execute(sql)
    conn.commit()