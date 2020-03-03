from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)
# Connect to the database
connection = pymysql.connect(
    host='localhost', 
    user='username', 
    password='password',
    db='mydb', charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()


@app.route('/')
def get():
    # Reatrive data
    try:
        cur.execute('''SELECT id, name, lname FROM student''')
        results = cur.fetchall()
    except Exception as not_exists_error:
        return '{}'.format(not_exists_error)
    return jsonify(
        {
            'Id': results[0]['id'],
            'Name': results[0]['name'],
            'Last name': results[0]['lname']
        }
    )


@app.route('/creat_table')
def creatTable():
    # Creat table
    try:
        cur.execute('''CREATE TABLE student (
            id int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
             name VARCHAR(255) NOT NULL,
            lname VARCHAR(255) NOT NULL)''')
    except Exception as already_exists:
        return '{}'.format(already_exists)
    finally:
        connection.commit()
        connection.close()
    return 'Table is created'


@app.route('/add')
def add():
    # Insert values on table
    try:
        cur.execute('''INSERT INTO student VALUES (1,'samir', 'salmi')''')
    except Exception as record_exists:
        return '{}'.format(record_exists)
    finally:
        connection.commit()
        connection.close()
    return 'Data is aded'


@app.route('/update')
def update():
    # Update data in table
    try:
        cur.execute('''UPDATE student SET id=2, name='Yusuf',
          lname='salmi' WHERE ID = 2''')
    except Exception as update_error:
        return '{}'.format(update_error)
    finally:
        connection.commit()
        connection.close()
    return 'Data is updated'


@app.route('/delete')
def delete():
    # Delete values from table
    try:
        cur.execute('''DELETE FROM student WHERE ID = 2''')
    except Exception as delete_error:
        return '{}'.format(delete_error)
    finally:
        connection.commit()
        connection.close()
    return 'Data is deleted'


if __name__ == "__main__":
    app.run(debug=True)
