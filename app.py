from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return


if __name__ == "__main__":  #make sure the app will be run on it's own, not as API
    app.run()