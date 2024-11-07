from fastapi import FastAPI, Path, Query, Header
from datetime import datetime

now = datetime.now()

app = FastAPI()

timestamp = str(now.year) + "/" + str(now.month) + "/" + "/" + str(now.day)

@app.get('/user/{user_id}')
async def user(user_id: int = Path(..., title="ID користуваача"), timestamp: str = Query(timestamp, title="Дата створення акаунту"), x_client_version: str  =  Header(1)):
    if timestamp != None:
        return f"{user_id}: {timestamp}({x_client_version})"
    else:
        return f"{user_id}: {timestamp}({x_client_version})" 