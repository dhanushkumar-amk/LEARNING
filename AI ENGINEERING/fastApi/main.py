from fastapi import FastAPI

app = FastAPI()

emp = [
    {'name' : "dhanushlumar", "id" : 1, "place": "USA"},
    {"name" : "sanjay", "id" : 2, "place" : "Canada"}
]

@app.get("/display/{id}")
def viewforPath(id : int):
    for e in emp:
        if e['id'] == id:
            return e

@app.get("/display")
def viewForQuery(id : int):
    for e in emp:
        if e['id']==id:
            return e

