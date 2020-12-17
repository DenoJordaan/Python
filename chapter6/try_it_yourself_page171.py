person_information = {'first_name':'juan','last_name': 'gehring,','age':' 24','city':'EL'}
print(person_information)
print(person_information['first_name'])
print(person_information['last_name'])
print(person_information['age'])
print(person_information['city'])


favourite_numbers = {'juan':'25','reuban':'90','stefan':'23','tash':'65','jonny':'12'}
print(favourite_numbers)
print(favourite_numbers['juan'])
print(favourite_numbers['reuban'])
print(favourite_numbers['stefan'])
print(favourite_numbers['tash'])
print(favourite_numbers['jonny'])





# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))



favorite_places = {
 'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
 'erin': ['hawaii', 'iceland'],
 'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())


favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))






