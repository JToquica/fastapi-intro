from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get('/')
def home():
    return {"Hello": "World"}

@app.post('/person/new')
def createPerson(person: Person = Body(...)):
    return person

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
    ),
    age: int = Query(...)
):
    return {"age": age}

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(..., gt=0)
):
    return {"id": person_id}

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...)
):
    return person