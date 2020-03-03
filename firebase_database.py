from flask import Flask, jsonify
from pyrebase import initialize_app
# Firebase configueration
config = {
    "apiKey": "api key",
    "authDomain": "authDomain.firebaseapp.com",
    "databaseURL": "https://<Database>.firebaseio.com",
    "storageBucket": "storageBucket.appspot.com"
}
app = Flask(__name__)
db = initialize_app(config).database()
items_count = db.child("articles").get()
# Reatrive data
@app.route('/')
def read():
    result = db.child("articles").get()
    ls = list()
    for item in result.each():
        ls.append(item.val())
    return jsonify(sorted(ls[::-1]))  # Data reverse and sort
# Insert data
@app.route('/creat')
def creat():
    data_creat = {"name": "Ismail", "lname": "Salmi", "age": 25}
    db.child("articles").child(items_count.val().__len__()).set(data_creat)
    return 'Is inserted!'
# Update data
@app.route('/update')
def update():
    item_id = 4
    data_update = {"name": "Ismail", "lname": "Salmi", "age": 26}
    db.child("articles").child(item_id).update(data_update)
    return 'Is updated!'
# Delete data
@app.route('/delete')
def delete():
    remove_item = 12
    db.child("articles").child(remove_item).remove()
    return 'Is Deleted!'


if __name__ == "__main__":
    app.run(debug=True)
