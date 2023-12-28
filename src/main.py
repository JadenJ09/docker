from fastapi import FastAPI
import uvicorn
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379, db=0)

import debugpy
debugpy.listen(("0.0.0.0", 5679))
# debuggy.wait_for_client()

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"hits": r.get("hits")}

# # %%
# uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



