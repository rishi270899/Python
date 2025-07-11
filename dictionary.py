# movies = {"Marvel":"Endgame", "DC" : "Justice League", "Disney":"Star Wars"}
# print(movies)
# print(movies["DC"])


# This loop only show dictionary keys
# for movie in movies:
#     print(movie)
 

# To show key value in dictionary
# for movie in movies:
#     print(movie,":", movies[movie])

# Second approach to print key and values (this approach work when we access dictionary)
# for (key, value) in movies.items():
#     print(key, value)

# To add new key valu pair
# movies["Paramount"] = "Mission Impossible"
# print(movies)

# to remove key value 
# movies.pop("DC")

movies_and_shows = {

"movies" : {
    "Space" : "interstellar",
    "Comedy" : "American Pi",
    "Horror" : "Anabella" 
},

"Shows" : {
    "Space" : "Lost in space",
    "Comedy" : "Sisters",
    "Horror" : "Darr"
}

}

# print(movies_and_shows["movies"])


# print(movies_and_shows)


# squared_num = {x:x**2 for x in range(1,6)}
# print(squared_num)


# how construct dictionary from list and variable
# keys = ["Horror", "Adventure", "SciFi"]

# val = "Genre"

# new_dict = dict.fromkeys(keys, val)
# print(new_dict)