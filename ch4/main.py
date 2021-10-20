from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")



@app.get("/order_food", response_class=HTMLResponse)
def order_food(request: Request):
    return templates.TemplateResponse("order_food.html", {"request": request})


from fastapi import Form


@app.post("/submit")
def submit_food(food: str = Form(...)):
    s = f"{food} 주문 완료"
    print(s)
    return s
