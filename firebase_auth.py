from flask import Flask, jsonify
from pyrebase import initialize_app

config = {
    "apiKey": "api key",
    "authDomain": "authDomain.firebaseapp.com",
    "databaseURL": "https://<Database>.firebaseio.com",
    "storageBucket": "storageBucket.appspot.com"
}

app = Flask(__name__)
firebase = initialize_app(config)
auth = firebase.auth()
db = firebase.database()


@app.route('/signin')
def sign_in():
    try:
        user = auth.sign_in_with_email_and_password(
            "email@gmial.com", 20203030)
        username = "jail"
        user_information = {"username": username,
                            "name": "yusuf", "lname": "salmi", "age": 26}
        results = db.child("users").child(username).set(
            user_information, user['idToken'])
    except Exception as sign_in_error:
        return '{}'.format(sign_in_error)
    return 'Is created'


@app.route('/signup')
def sign_up():
    try:
        auth.create_user_with_email_and_password("email@gmial.com", 20203030)
    except Exception as signup_error:
        return '{}'.format(signup_error)
    return 'Successfully'


@app.route('/accountinfo')
def account_info():
    try:
        user = auth.sign_in_with_email_and_password(
            'email@gmial.com', 20203030)
        acc_info = auth.get_account_info(user['idToken'])
    except Exception as account_info_error:
        return '{}'.format(account_info_error)
    return jsonify(acc_info)


@app.route('/resetpass')
def pass_reset():
    try:
        auth.send_password_reset_email("email@gmail.com")
    except Exception as password_reset_error:
        return '{}'.format(password_reset_error)
    return 'Go to a email box for reset your passord'


@app.route('/emailverification')
def email_verification():
    try:
        user = auth.sign_in_with_email_and_password(
            'email@gmail.com', 00000000)
        auth.send_email_verification(user['idToken'])
    except Exception as email_verification_error:
        return '{}'.format(email_verification_error)
    return 'We are send email verification'


if __name__ == "__main__":
    app.run(debug=True)
