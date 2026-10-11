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
    



if __name__ == "__main__":
    main()
