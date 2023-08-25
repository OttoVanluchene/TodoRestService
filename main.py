from fastapi import FastAPI
import database
import todo_orm
import todo_sql

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(todo_orm.router, prefix="/orm")
app.include_router(todo_sql.router, prefix="/sql")

@app.get("/")
def root():
    return "TODO App running"


