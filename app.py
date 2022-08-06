from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get our database connection string from an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("SQLALCHEMY_DATABASE_URI") 
app.config['SECRET_KEY'] = "shhh it's a secret"

print("Database used : " + app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

db.create_all()

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')