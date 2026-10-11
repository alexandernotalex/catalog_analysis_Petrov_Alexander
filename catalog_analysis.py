import math

def average_rating(movies) -> float:
    total_sum = 0
    for i in range(len(movies)):
        total_sum += movies[i]["rating"]
    return round(total_sum / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    max_year = current_year - movies[0]["year"]
    min_year = current_year - movies[0]["year"]
    sum_years = 0
    for i in range(len(movies)):
        sum_years += current_year - movies[i]["year"]
        if current_year - movies[i]["year"] > max_year:
            max_year = current_year - movies[i]["year"]
        if current_year - movies[i]["year"] < min_year:
            min_year = current_year - movies[i]["year"]
    return (max_year, min_year, math.ceil(sum_years / len(movies)))


def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    remain_minutes = minutes % 60
    return f"{hours}ч {remain_minutes}м"


def rating_tier(rating: int) -> str:
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "хорошо" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    match year:
        case year if year > 2020:
            return "новые"
        case year if 2015 <= year <= 2020:
            return "недавние"
        case year if year < 2015:
            return "старые"



def count_long_movies(movies, threshold=120):
    counter = 0
    for i in range(len(movies)):
        if movies[i]["duration_min"] > threshold:
            counter += 1
    return counter


def normalize_title(title):
    words = title.split()
    normalized_title = ""
    for word in words:
        normalized_title += word[0].upper() + word[1:] + " "
    normalized_title = normalized_title[:-1]
    return normalized_title


def make_slug(title):
    words = title.split()
    slug = []
    for word in words:
        slug.append(word.lower())
    return "-".join(slug)


def format_report_line(movie):
    genres_str = ", ".join(sorted(movie["genres"]))
    info = movie["title"]
    info += f" ({movie["year"]}) - {movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, жанры: {genres_str}"
    return info
    # выше работает и просто написать {sorted(movie["genres"])}, но я побоялся снятия баллов за фигурные скобки
    # и сделал через genres_str


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    movie_rating = [sorted_movies[i]["title"] for i in range(len(movies))]
    return movie_rating


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    top_n_films = [(sorted_movies[i]["title"], sorted_movies[i]["rating"]) for i in range(n)]
    return top_n_films


def count_by_genre(movies):
    movies_by_genre = {}
    for movie in movies:
        genres = movie.get("genres")
        for genre in genres:
            movies_by_genre[genre] = movies_by_genre.get(genre, 0) + 1
    return movies_by_genre


def actor_filmography(movies):
    movies_by_actor = {}
    for movie in movies:
        actors = movie.get("actors")
        for actor in actors:
            movies_by_actor[actor] = movies_by_actor.get(actor, [])
            movies_by_actor[actor].append(movie["title"])
    return movies_by_actor


def all_genres(movies):
    unique_genres = set()
    for movie in movies:
        unique_genres.update(movie["genres"])
    return unique_genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]}")
    print("Топ 3 фильма:")
    title_to_movie = {m["title"]: m for m in movies}
    for title, _ in top_n_by_rating(movies, 3):
        print(format_report_line(title_to_movie[title]))
    print("Фильмов по жанрам:")
    for genre, count in count_by_genre(movies).items():
        print(f"  {genre} — {count}")
    print(f"Все жанры каталога:{", ".join(all_genres(movies))}")


def main():
    movies = [
        {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
        "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
        {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
        "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
        {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
        "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
        {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
        "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
        {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
        "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
        {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
        "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
        {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
        "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
        {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
        "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
        {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
        "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
        {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
        "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
    ]
    print(average_rating(movies))
    print(catalog_age_stats(movies))
    print(duration_in_hours(movies[0]["duration_min"]))
    print(rating_tier(movies[6]["rating"]), rating_tier(movies[3]["rating"]))
    print(decade_label(movies[0]["year"]), decade_label(movies[5]["year"]))
    print(count_long_movies(movies, 130))
    print(normalize_title(movies[2]["title"]))
    print(make_slug(movies[0]["title"]))
    print(format_report_line(movies[0]))
    print(titles_sorted_by_rating(movies))
    print(top_n_by_rating(movies, 6))
    print(count_by_genre(movies))
    print(actor_filmography(movies))
    print(all_genres(movies))
    print(common_actors(movies[1], movies[4]))
    print(genres_only_in_one(movies[5:6], movies[:5]))
    print("-"*30)
    build_report(movies)
    print("-"*30)
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    print("Суммарная длительность (рейтинг > 7):", total_duration, "мин")

    for i in range(len(movies)):
        if "comedy" in movies[i]["genres"]:
            continue
        else:
            print(movies[i]["title"])

    idx = 0
    while idx < len(movies):
        if movies[idx]["rating"] > 9:
            print(movies[idx]["title"])
            break
        idx += 1
    else:
        print("Шедевров не найдено")

    top_filmes = {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average_rating(movies)}
    print(top_filmes)
    



if __name__ == "__main__":
    main()
