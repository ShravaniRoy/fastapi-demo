from fastapi import FastAPI
from models import Todo

app = FastAPI()

#all the below code is plain python
#data validation is in built with fastapi, at pydantic
#fastAPI is typed Python
@app.get("/")
async def root():
    return {"message": "Hello World"}


todos = []
# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo
@app.get("/todos/{id}")
async def get_todos(id: int):
    for todo in todos:
        if todo.id == id:
            return {"todo": todo}
    return {"message": "todo not found"}

# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo item is added"}

# Update a todo

# Delete a todo