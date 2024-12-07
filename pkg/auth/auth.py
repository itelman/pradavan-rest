from datetime import datetime, timedelta

import jwt

# JWT Config
SECRET_KEY = "9b1c865c5082469b3a3fd3d5ae49d546baf3a2d7258cbe3f60503c8bc17d5e5b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600


def CreateAccessToken(data: dict, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS))
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def DecodeAccessToken(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception as e:
        raise e
