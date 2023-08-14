from flask import Flask
from database import db

app = Flask(__name__)

# Nastroyka bazi dannix
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"

# Podklyuchit SQLALCHEMY k nashemu flask
db.init_app(app)