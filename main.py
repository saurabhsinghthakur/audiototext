"""
Author: Saurabh Singh
Date: 2023-10-11
"""
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Body
from app.libraries.common_libraries import LoadModule

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/{version}/audiototext")
async def process_audio(version: str, audio_file: UploadFile = File(...)):
    """process_audio"""
    my_instance = LoadModule('audiototext', version).load_module()
    recognized_text = my_instance(audio_file).post()
    return {"recognized_text": recognized_text}

@app.post("/api/{version}/summarizer")
async def summarizer(version: str, input_data: dict = Body(...)):
    """summarizer"""
    input_text = input_data.get("text", "")
    my_instance = LoadModule('summarizer', version).load_module()
    recognized_text = my_instance(input_text).post()
    return {"recognized_text": recognized_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
