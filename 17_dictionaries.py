movie = {
    'title': "Life of Brian",
    'year': 1979,
    'cast': ["Graham Chapman", "John Cleese", "Terry Gilliam",
           "Eric Idle", "Terry Jones", "Michael Palin"],
}
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['director'] = "Terry Jones"
print(movie.get('director', 'Unknown Title'))
del movie['director']
print(len(movie))
print("=== DICTIONARIES KEYS")
print(movie.keys())
print("=== DICTIONARIES VALUES")
print(movie.values())
print("=== DICTIONARIES ITEMS")
print(movie.items())
print("=== DICTIONARIES ITERATE KEYS")
for key,value in movie.items():
    print(f"{key}: {value}")