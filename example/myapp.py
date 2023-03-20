from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <html>
            <head>
                <title>Homepage</title>
            </head>
            <body>
                <h1>Welcome to the homepage!</h1>
                <p>Here's some content for the homepage.</p>
            </body>
        </html>
    """

@app.get("/my_page_505", response_class=HTMLResponse)
async def return_html_page1(request: Request):
    html_content = """
        <html>
            <head>
                <title>My Page 505 status</title>
            </head>
            <body>
                <h1>Server Error 505</h1>
                <p>There was a problem with the server 505.</p>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=505)

@app.get("/my_page_404", response_class=HTMLResponse)
async def return_html_page2(request: Request):
    html_content = """
        <html>
            <head>
                <title>My Page 404 status</title>
            </head>
            <body>
                <h1>Server Error 404</h1>
                <p>There was a problem with the server 404.</p>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=404)