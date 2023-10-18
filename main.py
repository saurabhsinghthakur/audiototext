"""
Author: Saurabh Singh
Date: 2023-10-11
"""
from fastapi.middleware.cors import CORSMiddleware
from app.libraries.common_libraries import LoadModule
from fastapi import FastAPI, File, Depends, Body, HTTPException, status, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Secret key to sign JWT
SECRET_KEY = "xpIj45gybDP9zbR8NIxl2KYzYSMRi6mQ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2PasswordBearer for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a function to create JWT tokens
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Create a function to verify the password
def verify_password(plain_password, hashed_password):
    """ """
    # You can use a proper hashing algorithm for MongoDB
    # For simplicity, we use passlib here, but consider using a different approach
    return pwd_context.verify(plain_password, hashed_password)

# Route to create a new user
@app.post("/register")
async def register(body:dict):    
    pass

# Route to generate an access token
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.users.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await db.users.find_one({"username": username})
    if user is None:
        raise credentials_exception

    return user


@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"username": current_user["username"], "id": current_user["_id"]}




@app.post("/api/{version}/audiototext")
async def process_audio(version: str, audio_file: UploadFile = File(...)):
    """process_audio"""
    my_instance = LoadModule('audiototext', version).load_module()
    recognized_text = my_instance(audio_file).post()
    return {"recognized_text": recognized_text}

@app.post("/api/{version}/{product}")
async def post(version: str, product: str, input_data: dict = Body(...)):
    """Post"""
    my_instance = LoadModule(product, version).load_module()
    response = my_instance(input_data).post()
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)
