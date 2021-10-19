import sys
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymysql import connect, cursors, Error


class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    completed: Optional[bool] = False


config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'todo',
    'cursorclass': cursors.DictCursor
}

try:
    cnx = connect(**config)
    cur = cnx.cursor()
except Error as e:
    print(e)
    sys.exit()

app = FastAPI()


@app.get("/api/todos", status_code=200)
def get_all_todos():
    sql = '''SELECT * FROM todolist'''

    cur.execute(sql)
    todos = cur.fetchall()
    return todos


@app.post("/api/todos", status_code=201)
def create_todo(todo: Todo):
    sql = '''INSERT INTO todolist (title) VALUES (%s)'''

    cur.execute(sql, todo.title)
    cnx.commit()

    id = cur.lastrowid
    todo.id = id
    return todo


@app.put("/api/todos/{id}", status_code=200)
def update_todo(id: int, todo: Todo):
    sql = f'''
    UPDATE todolist
    SET title = %(title)s,
        completed = %(completed)s
    WHERE id = {id}
    '''

    cur.execute(sql, dict(todo))
    cnx.commit()

    todo.id = id
    return todo


@app.delete("/api/todos/{id}", status_code=200)
def delete_todo(id):
    sql = f'''DELETE FROM todolist WHERE id = {id}'''

    cur.execute(sql)
    cnx.commit()
    return
