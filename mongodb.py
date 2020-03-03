from flask import Flask, jsonify, render_template, url_for, redirect, request
from flask_pymongo import PyMongo

app = Flask(__name__)
# Mongodb connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/user"
mongo = PyMongo(app)


@app.route('/')
def index():
    try:
        all_students = mongo.db.students.find({})
    except Exception as connection_error:
        return '{}'.format(connection_error)
    return render_template('index.html', students=all_students)


@app.route('/insert', methods=['GET'])
def insert():
    # localhost:5000/insert?name=name&lastname=lastname
    name = request.args.get('name')
    lname = request.args.get('lastname')
    new_user = {"name": name, "lname": lname}
    try:
        mongo.db.students.insert(new_user)
    except Exception as insert_error:
        return '{}'.format(insert_error)
    return redirect(url_for('index'))


@app.route('/update')
def update():
    # localhost:5000/update?oname=oldName&nname=newName
    old_name = request.args.get('oname')
    new_name = request.args.get('nname')
    try:
        o_name = {"name": old_name}
        n_name = {"$set": {"name": new_name}}
        mongo.db.students.update(o_name, n_name)
    except Exception as update_error:
        return '{}'.format(update_error)
    return redirect(url_for('index'))


@app.route('/delete/<string:lname>')
def delete(lname):
    # localhost:5000/delete/lastName
    try:
        delete_user = {"lname": lname}
        mongo.db.students.remove(delete_user)
    except Exception as delete_error:
        return '{}'.format(delete_error)
    return redirect(url_for('index'))


@app.route("/find/<name>")
def find(name):
    # http://localhost:5000/find/name
    student = mongo.db.students.find_one_or_404({"name": name})
    return render_template('find.html', student=student)


if __name__ == '__main__':
    app.run(debug=True)
