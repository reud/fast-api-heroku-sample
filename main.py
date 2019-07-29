from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/fizz_buzz/{num}")
def read_item(num: int):
    # https: // ja.wikipedia.org / wiki / Fizz_Buzz
    if not num % 15:
        return {num: "Fizz Buzz"}
    elif not num % 5 or not num % 3:
        return {num: 'Fizz' if not num % 3 else 'Buzz'}
    else:
        return {num: 'Stay Silent'}
