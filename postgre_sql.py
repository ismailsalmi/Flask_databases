from flask import Flask, jsonify
import pg8000

app = Flask(__name__)
# Database connection
connection = pg8000.connect(
    database="postgres", user="postgres",
    password="1991", host="127.0.0.1", port=5432)
cur = connection.cursor()


@app.route('/')
def get():
    # Read data from table
    try:
        cur.execute('''SELECT id, title, author FROM books''')
        results = cur.fetchall()
    except Exception as data_not_exists:
        return '{}'.format(data_not_exists)
    return jsonify(results)


@app.route('/add_table')
def creat_Table():
    # Creat table on database
    try:
        cur.execute(
            '''CREATE TABLE books (id SERIAL PRIMARY KEY,
             title VARCHAR(100) NOT NULL, author VARCHAR(100) NULL,
              created_at TIMESTAMPTZ DEFAULT Now());''')
        connection.commit()
    except Exception as table_already_exists:
        return '{}'.format(table_already_exists)
    return 'Table is aded'


@app.route('/add')
def insert():
    try:
        # Insert values on table
        cur.execute('''INSERT INTO books VALUES (1,'book_title','author_name')''')
        connection.commit()
    except Exception as already_exists_error:
        return '{}'.format(already_exists_error)
    return 'Data is Inserted'


@app.route('/update')
def update():
    try:
        # Update data in table
        cur.execute('''UPDATE books SET id=2, title='Kotlin',
           author='kotlin in action' WHERE ID = 2''')
        connection.commit()
    except Exception as update_error:
        return '{}'.format(update_error)
    return 'Data is updated'


@app.route('/delete')
def delete():
    try:
        # Delete values from table
        row_id = 2
        cur.execute('''DELETE FROM books WHERE ID = {}'''.format(row_id))
        connection.commit()
    except Exception as delete_error:
        return '{}'.format(delete_error)
    return 'Data is deleted'


if __name__ == "__main__":
    app.run(debug=True)
