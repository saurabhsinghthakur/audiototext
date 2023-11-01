"""
Author: Saurabh Singh
Date: 2023-10-11
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body
from app.libraries.common_libraries import LoadModule

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/{version}/{product}")
async def post(version: str, product: str, request_body: dict = Body(...)):
    """Commnucate All the Services"""
    my_instance = LoadModule(product, version).load_module()
    recognized_text = my_instance(request_body).post()
    return {"recognized_text": recognized_text}
