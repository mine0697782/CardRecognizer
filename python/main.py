from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import uuid
import os
from CardRecognizer import recognize

app = FastAPI()

UPLOAD_DIR = "./images"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.get("/hi")
def say_hi():
    return {"message": "hi"}

@app.post("/upload")
async def upload_card(file: UploadFile):
    try:
        # 파일 내용 읽기
        content = await file.read()
        # 파일 이름 생성
        filename = f"{str(uuid.uuid4())}.jpg"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # 파일 저장
        with open(file_path, 'wb') as fp:
            fp.write(content)

        # 이미지 경로로 recognize 함수 호출
        response = recognize(file_path)

        # 응답 반환
        return {"data": response}
    except Exception as e:
        # 예외 처리
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "hello"}
