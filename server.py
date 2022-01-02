from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main():
    return {"status": "product successfully recieved."}
