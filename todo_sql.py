from typing import List
from fastapi import APIRouter
from database_sql import connection
from models_sql import Todo

router = APIRouter()

@router.get("/todo")
def read_todo_list():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM todos")
        results = cursor.fetchall() 

        todo_list = []
        for record in results:
            mapper = create_json_mapper(cursor, record)
            todo = Todo(**mapper) 
            todo_list.append(todo)

    return todo_list

@router.get("/todo/{todo_id}")
def read_todo_by_id(todo_id: int):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
        result = cursor.fetchone() 

        if result is None:
            return {"error": "Todo not found"}

        mapper = create_json_mapper(cursor, result) 
        return mapper 

@router.post("/todo")
def create_todo(todo: Todo):    
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO todos (task) VALUES (%s) RETURNING id", (todo.task,))
        connection.commit()

        todo_id = cursor.fetchone()[0]     
        return todo_id

# --- Helper functions ---

# This function creates a dictionary from the column names and the values in a record
# The cursor.description attribute contains the column names of the query
# Dict is a collection of key-value pairs
# The zip() combines column_names and record list into a list of tuples (key-value pairs) - easy
def create_json_mapper(cursor, record):
    column_names = [desc[0] for desc in cursor.description]
    mapper = dict(zip(column_names, record))
    return mapper