from flask import Blueprint, render_template, request
from app.database import Database

movies_bp = Blueprint("movies", __name__)


@movies_bp.route("/")
def view_all_movies():
    """Fetch and display all movies."""

    # ============================= README =============================
    #    This is an *example function* demonstrating how to retrieve 
    #    all movies from the `MotionPicture` table and display them.
    #
    #    Retrieved data is passed to the `movies.html` template for rendering.
    #
    # Implementation Steps:
    #    - Open a database connection using the `Database` context manager.
    #    - Execute the SQL query to retrieve movie data.
    #    - Pass the retrieved list to `index.html` for rendering.
    # ==================================================================
    #
    # >>>> No changes are expected in this function <<<<

    with Database() as db:
        movies = db.execute(
            "SELECT name, rating, production, budget FROM MotionPicture"
        )
    return render_template("movies.html", movies=movies)


@movies_bp.route("/like_movie", methods=["POST"])
def like_movie():
    """Allow a user to like a movie."""
    user_email = request.form["user_email"]
    movie_id = request.form["movie_id"]

    # >>>> TODO 2: Write a query to insert a like into the Likes table <<<<
    #              The query should insert `movie_id` and `user_email` into `Likes`.
    #
    # >>>> NOTE: Read the Database.execute function documentation to understand:
    #    - How `execute` handles SQL queries.
    #    - Why we pass `params` as a tuple (movie_id, user_email).
    #    - The role of `commit=True` in saving changes.

    query = "INSERT INTO LIKES (mpid, uemail) VALUES (%s, %s);"

    with Database() as db:
        try:
            db.execute(query, (movie_id, user_email), commit=True)
            message = "You have successfully liked the movie!"
        except Exception as e:
            message = f"An error occurred: {str(e)}"

    return render_template("liked_movie.html", message=message)
