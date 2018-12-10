

from flask import (Flask, request, session, g,
                   redirect, url_for, abort, render_template, flash)
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('root'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)