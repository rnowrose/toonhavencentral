import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.core import TORTOISE_ORM

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # Automatically generate database schemas
    add_exception_handlers=True,
)

@app.get("/")
async def root():
    return {"message": "Hello World"}



# Entry point for running the application with Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)