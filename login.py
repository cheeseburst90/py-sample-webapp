from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace with a proper authentication mechanism)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def home():
    return 'Welcome to the login page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return f'Login successful, welcome {username}!'
        else:
            return 'Login failed. Please check your username and password.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
