from flask import Flask
from routes import create_routes

app = Flask(__name__)
   
if __name__ == "__main__":
    create_routes( app )
    app.run(host="0.0.0.0", port=8080)