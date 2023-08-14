from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# importiruyem vse fuktsii iz faylov dlya db
from database.leaders_service import *
from database.questionservice import *
from database.registerservice import *

