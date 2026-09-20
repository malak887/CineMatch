
import pandas as pd


def load_and_preprocess_data():
    movies = pd.read_csv(
        "data/raw/movies.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["movie_id", "title", "genres"]
    )

    ratings = pd.read_csv(
        "data/raw/ratings.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )

    users = pd.read_csv(
        "data/raw/users.dat",
        sep="::",
        engine="python",
        encoding="latin-1",
        names=["user_id", "gender", "age", "occupation", "zip_code"]
    )

    # Validate
    assert movies["movie_id"].is_unique
    assert users["user_id"].is_unique

    assert ratings["rating"].between(1, 5).all()

    assert not ratings.duplicated(
        subset=["user_id", "movie_id"]
    ).any()

    assert ratings["movie_id"].isin(
        movies["movie_id"]
    ).all()

    assert ratings["user_id"].isin(
        users["user_id"]
    ).all()

    # Extract year
    movies["year"] = movies["title"].str.extract(
        r"\((\d{4})\)"
    )

    return movies, ratings, users