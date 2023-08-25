from fastapi import FastAPI
import database_orm
import todo_orm
import todo_sql

# Create the database tables
database_orm.Base.metadata.create_all(bind=database_orm.engine)

app = FastAPI()

app.include_router(todo_orm.router, prefix="/orm")
app.include_router(todo_sql.router, prefix="/sql")

@app.get("/")
def root():
    return "TODO App running"

