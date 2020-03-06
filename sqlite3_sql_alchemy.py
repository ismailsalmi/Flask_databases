from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# database url connection
db_url = 'sqlite:///database.db'
# database configueration
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    lname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.now())

db.create_all()

# Reatrive data
@app.route('/')
def select():
    try:
        get_user_info = [details for details in db.session.query(
            User.id, User.name, User.lname, User.email, User.text,
            User.password, User.date).all()]

    except Exception as not_exists:
        return '{}'.format(not_exists)
    return jsonify(get_user_info[::-1])

# Add record
@app.route('/add')
def insert():
    try:
        user_information = User(name='zoheir', 
            lname='abdellah', email='zoheir@gmail.com', 
                text='Im a developer ', password='2004')
        db.session.add(user_information)
        db.session.commit()
    except Exception as already_exists:
        return '{}'.format(already_exists)
    return 'is added'

# Update anything on record
@app.route('/update')
def update():
    try:
        update_info = User.query.filter_by(id=1).first()
        update_info.name = 'ahmed'
        update_info.email = 'ahmed@gmail.com'
        db.session.commit()
    except Exception as update_error:
        return '{}'.format(update_error)
    return 'Updated'

# Delete record
@app.route('/delete')
def delete():
    try:
        delete = 1
        delete_user = User.query.filter_by(id=delete).first()
        db.session.delete(delete_user)
        db.session.commit()
    except Exception as delete_error:
        return '{}'.format(delete_error)
    return 'Deleted'


@app.route('/drop')
def drop_table():
    try:
        db.drop_all()
    except Exception as drop_error:
        return '{}'.format(drop_error)
    return 'Is droped'

if __name__ == "__main__":
    app.run(debug=True)
