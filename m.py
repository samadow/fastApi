from fastapi import FastAPI,Query, Path,HTTPException

app = FastAPI(title="my FIrst API")
version="1.0.0"
next_id = 1

student_list = [
    {
    "id":next_id,
     "name":"ali",
     "surname":"surname",
     "age":"age"
     },
]
@app.get("/")
def hello():
    return {"message": "privet"}



@app.get("/users/{user_id}")
def get_user(user_id: int = Path(gt=0)):
    return {"user_id": user_id}


@app.get("/products")
def list_products(
    search: str | None = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return {"search": search, "limit": limit, "offset": offset}



@app.post("/post_p")
async def create_student(name: str, surname: str, age: int = 20):
    global next_id
    
    student = {
        "id": next_id,
        "name": name,
        "surname": surname,
        "age": age
    }

    student_list.append(student)
    next_id += 1
    return student



@app.delete("/delete/{name_id}")
async def delete_student(name_id: str):
    if name_id not in student_list:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student_list.remove(name_id)
    return {"message": f"Student {name_id} deleted successfully"}
    
    
   
    