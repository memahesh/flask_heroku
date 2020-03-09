from flask_sqlalchemy import SQLAlchemy



from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://memahesh:123qweasd@db4free.net:3306/docreferral'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
