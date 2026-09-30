# import boto3
from fastapi import FastAPI, Response, UploadFile, File
from pydantic import BaseModel
import pymysql
from config import Config
import model
 
app = FastAPI()
con = Config()
# s3 = boto3.client('s3',
#                   aws_access_key_id=con.AWS_ACCESS_KEY,
#                   aws_secret_access_key=con.AWS_SECRET_KEY)
 

@app.get('/')
def index():
    return 'hi AWS world / .env 테스트 : {}'.format(con.DB_SCHEMA)
 

@app.get('/health')
def health():
    return Response("Success Health Check", status_code=200)
 

# 파일 업로드를 쓰려면 requirements.txt 에 python-multipart 추가 필요
# @app.post('/upload')
# def upload_image(image: UploadFile = File(None)):
#     if image:
#         # upload_fileobj(파일자체, 버킷이름, s3키값)
#         s3.upload_fileobj(image.file, con.BUCKET_NAME, 'image/{}'.format(image.filename))
#         return Response("upload success", status_code=200)
#     return Response("No file", status_code=404)

class Item(BaseModel):
    name: str
    message: str


@app.post('/guestbook', status_code=201)
def create_guestbook(item: Item):
    new_id = model.add(item)
    return {"id": new_id, "name": item.name, "message": item.message}


if __name__ == '__main__':
    import uvicorn
    db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
    print("connect ok")
    db.close()
    uvicorn.run(app, host='0.0.0.0', port=5000)
