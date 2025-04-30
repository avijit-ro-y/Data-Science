from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
class Item(BaseModel):
    id:int
    title:str
    status:str
    
app = FastAPI()

Todo=[Item(id=0,title="task1",status="pending")]
@app.get("/todo")
def root():
    return {"Todo list": Todo}

@app.get("/todo/{todo_id}")
def get_todo_items(todo_id:int):
    for item in Todo:
        if (item.id==todo_id):
            return item
    return {"Todo list": "Not found"}

@app.post("/add")
def adding_data(todoitem:Item):
    Todo.append(todoitem)
    return{'message':'item added'}

@app.put("/update-todo/{todo_id}")
def update_todo(todo_id:int,updated_data:Item):
    for item in Todo:
        if (item.id==todo_id):
            item.status=updated_data.status
            return item
    return {"Todo list": "Not found"}

@app.delete("/delete/{todo_id}")
def delete_item(todo_id:int):
    for index,item in enumerate(Todo):
        if (item.id==todo_id):
            item.status=updated_data.status
            return Todo.pop(index)
    raise HTTPException(status_code=404,detail="Item not found")


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8080)