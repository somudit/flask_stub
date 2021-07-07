from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
