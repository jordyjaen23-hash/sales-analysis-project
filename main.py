import requests
import pandas as pd

api_key = "17d5765afe04074ca1b93dc99b99b126"

url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=es-ES&page=1"

response = requests.get(url)
data = response.json()

movies_list = []

if "results" in data:
    for movie in data["results"]:
        movies_list.append({
            "titulo": movie["title"],
            "rating": movie["vote_average"]
        })
else:
    print("Error en la API")
    print(data)

df = pd.DataFrame(movies_list)

print(df)

df.to_csv("peliculas.csv", index=False)
top_movies = df[df["rating"] > 7]

print("\nPelículas con rating mayor a 7:\n")
print(top_movies)
import matplotlib.pyplot as plt

top_movies = df[df["rating"] > 7]

plt.figure()
plt.bar(top_movies["titulo"], top_movies["rating"])

plt.xticks(rotation=45, ha="right")
plt.title("Películas mejor valoradas")
plt.xlabel("Películas")
plt.ylabel("Rating")

plt.tight_layout()
plt.show()