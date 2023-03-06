"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect, url_for
from model import connect_to_db, db, User
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.jinja_env.undefined = StrictUndefined



# Replace this with routes and view functions!
@app.route("/")
def homepage():

    return render_template('homepage.html')

@app.route("/movies")
def all_movies():

    movies= crud.get_movies()

    return render_template('all_movies.html', movies = movies)

@app.route("/users")
def users():

    users = crud.get_users()

    return render_template('users.html', users = users)

@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie = movie)

@app.route("/users/<user_id>")
def user(user_id):
    user = crud.get_user_by_id(2)

    return render_template('user.html', user = user)

@app.route("/users", methods=["POST"])
def register_user():
    
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the user credentials are valid
        email = request.form['email']
        password = request.form['password']

        if email == 'your_email' and password == 'your_password':
            session['email'] = email
            return redirect(url_for('/homepage'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('homepage.html')

@app.route("/logout")
def logout():
   del session["username"]
   flash("Logged out.")
   return redirect("/login")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, port=8000, host="localhost")

# host="0.0.0.0",
