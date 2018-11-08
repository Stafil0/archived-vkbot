from flask_sqlalchemy import SQLAlchemy
from app.app_start import app

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
