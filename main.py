from fastapi import FastAPI,Query, Path,HTTPException

app = FastAPI(title="My appi")
cate_id = 1
id_users = 1
pro_id = 1
order_id =1
login = None
category_list =[
    {"id":cate_id,
     "name" : "phone"
     },
]
cate_id += 1  # id=1 уже занят категорией "phone"
order_list = []

users_list = [
    {
    "id":id_users,
     "name":"ali",
     "age":20,
     "password":"1234"
     
     },
]

product_list = []

@app.get("/users")
async def gt_users():
    return users_list

@app.post("/register")
async def registers(name: str, password: str, age: int = 20):
    global id_users
    global users_list
    users={
        "id" : id_users,
        "name" : name,
        "age" : age,
        "password":password
    }
    users_list.append(users)
    id_users+=1
    return users_list
    
@app.get("/login")
async def login(name:str,password:str):
    global login
    print(users_list)
    for i in users_list:
        print(i['name'], name)
        print(i['password'], password)
        if  i["name"] == name and i["password"] == password:
            login=name
            return {"login":"logiin correcrt"}
    raise HTTPException(status_code=404, detail="user not found")
    
    
    
@app.delete("/logaut")
async def logaut(name:str):
    global login
    if login == name:
        login=None
        return "logined"
    return "name not found"

@app.post("/category_cr")
async def creat_c(name:str):
    global cate_id
    categroi = {
        "id" : cate_id,
        "name" : name
    }
    category_list.append(categroi)
    cate_id+=1
    return categroi

@app.get("/categories")
async def catefori():
    return category_list

@app.get("/categories/{category_id}/products")
async def category_products(category_id: int = Path(gt=0)):
    # 1. проверяем, что категория существует
    category = None
    for c in category_list:
        if c["id"] == category_id:
            category = c
            break
    if category is None:
        raise HTTPException(status_code=404, detail="category not found")

    # 2. собираем все товары этой категории
    result = []
    for p in product_list:
        if p["categori_id"] == category_id:
            result.append(p)
    return result

@app.post("/product_cr")
async def products_cr(name:str,price:int,quantiti:int,categori_id:int):
    global cate_id
    global pro_id
    products = {
        "id":pro_id,
        "name":name,
        "price":price,
        "categori_id":categori_id
    }
    product_list.append(products)
    pro_id += 1
    return products

@app.get("/get_products")
async def produucts():
    return product_list

@app.post("/order")
async def creat_order(user_id:int,product_id:int):
    global order_id
    global id_users
    global pro_id
    orders = {
        "id" : order_id,
        "user_id":user_id,
        "pro_id":pro_id
    }
    order_list.append(orders)
    order_id+=1
    return orders

@app.get("/get_products")
async def et_orders():
    return order_list




    
    
    
    
    
    
    
    
    




