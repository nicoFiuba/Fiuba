from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    howiam = url_for(filename="./howiam.html")
    return f'Hello, World! {howiam}'

if __name__ == '__main__':
    app.run("localhost", port=8081, debug=True) # esto solo funca usando python3 app.py
