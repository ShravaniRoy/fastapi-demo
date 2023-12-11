from fastapi import FastAPI
from models import Todo

app = FastAPI()

#all the below code is plain python
#data validation is in built with fastapi, at pydantic
#fastAPI is typed Python
#unlike in Flask, the errors are in JSON and not in HTML
#Authentication is built in -OAuth, JWT, etc
#Swagger UI is in-built at endpoint /docs, Redoc is also available at the endpoint /redoc
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
async def get_todo(id: int):
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
@app.put("/todos/{id}")
async def update_todo(id: int, todo: Todo):
    for item in todos:
        if item.id == id:
            item.id = todo.id
            item.item = todo.item
            return {"message": "todo item is updated"}
    return {"message": "todo item not found"}

# Delete a todo
@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for item in todos:
        if item.id == id:
            todos.remove(item)
            return {"message": "todo item is removed"}
    return {"message": "todo item not found"}
