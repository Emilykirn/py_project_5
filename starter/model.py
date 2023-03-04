"""Models for movie ratings app."""
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


# Replace this with your code!
class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column (db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    # ratings = a list of Rating objects
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):

    __tablename__ = "movies"

    movie_id = db.Column (db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    # ratings = a list of Rating objects

    def __repr__(self):
      return f'<Movie movie_id={self.movie_id} movie_name={self.title}>'

class Rating(db.Model):

    __tablename__ = "ratings"

    rating_id = db.Column (db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Integer)
    movie_rating = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")
    
    def __repr__(self):
      return f'<Rating rating_id={self.rating_id} score={self.score}>'

# def test_func(app):
#     with app.app_context():
#         test_user = User.query.get(1)
#         movies = Movie.query.all()
#         rat = Rating(score=5, movie=movies[0])
#         test_user.ratings.append(rat)
#         db.session.commit()

# def create_mov(app):
#     with app.app_context():
#         new_user = User(email='admin@website.com', password="admin")
#         db.session.add(new_user)
#         db.session.commit()
#         new_movie = Movie(title='a great movie', overview='the best movie', release_date=datetime(2020, 1, 10), poster_path='/static/placeholder.png')
#         db.session.add(new_movie)
#         db.session.commit()
#         new_rating = Rating(user = new_user, movie = new_movie, score=4)
#         db.session.add(new_rating)
#         db.session.commit()

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False) 
