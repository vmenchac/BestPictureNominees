"""
Best Picture Nominees
- Minari
- Sound of Metal
- Mank
- Promising Young Woman
- The Father
- Judas and the Black Messiah
- The Trial of the Chigago 7
- Nomadland
For each movie, obtain:
- Year
- Rating
- Director(s)
- Plot
- Cast (top 5)
- Genre
Create a pretty table and store the output in a file called output.txt
Post the source code and the output file in your github.
Share the link with sarifern@cisco.com
The first submission of each category (begineer, intermediate, advanced) will get a price.
"""
from imdb import IMDb
from prettytable import PrettyTable

table = PrettyTable()
table.field_names=["Tittle","Year","Rating","Director","Plot","Cast (Top 5)","Genre"]

ia = IMDb()
movie_list = ["Minari","Sound of Metal","Mank","Promising Young Woman","The Father","Judas and the Black Messiah","The Trial of the Chigago 7","Nomadland"]

file = open("movies.txt","w")

for movie in movie_list:
    movie0 = ia.search_movie(movie)[0]
    movie = ia.get_movie(movie0.movieID)

    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    directors = movie["director"]
    list_directors = []
    for i in range(len(directors)):
        list_directors.append(directors[i]["name"])
    list_directors = ", ".join(list_directors)
    plot = movie["plot"][0]
    list_cast = []
    for cast in movie["cast"][:5]:
        list_cast.append(cast["name"])
    list_cast = ", ".join(list_cast)
    genre = ", ".join(movie["genre"])

    table.add_row([title,year,rating,list_directors,plot,list_cast,genre])

file.writelines(table.get_string())
file.close()
