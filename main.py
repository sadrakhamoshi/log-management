import uvicorn
from example.myapp import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)