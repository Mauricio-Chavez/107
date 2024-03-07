from flask import Flask

app = Flask(__name__)#__name__ this is using for the name of the folder.

@app.get('/')
def home():
    return "Hello from flask"

app.run(debug=True)









