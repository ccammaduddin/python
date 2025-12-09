anime = ["One Piece", "Attack on Titan", "Black Clover", "Fairy Tail", "Naruto", "Dr Stone" ]
print(anime)

# Length
print(len(anime))

# Find Index
print(anime.index("Dr Stone"))


# Count occurrences
print(anime.count("One Piece"))


# Add item to the end
anime.append("Demon Slayer")
# anime.insert(0, "Sword Art Online")
print(anime)

# Sort items reverse
anime.sort(reverse=True)
print(anime)

# Sort items alphabetically
anime.sort()
print(anime)

# Reverse the order of items
anime.reverse()
print(anime)

numbers = [2,40,45,112,89,246,3]

# Add new item at index 2 i.e 0,1,2
numbers[2]= 288

# Find min
print(min(numbers))


#  Find max
print(max(numbers))


# Find Sum
print(sum(numbers))

# Extend list
anime.extend(numbers)
print(anime)

# Remove item "2"
anime.remove(2)
print(anime)

# Pop item at index -1
anime.pop(-1)
print(anime)

# Delete the list
# del anime
del anime[3]
print(anime)

# Clear the list
anime.clear()
print(anime)

