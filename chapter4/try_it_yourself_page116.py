players = ['charles', 'martina', 'michael', 'florence', 'eli','joeps','mike']

print("Here are the first three players on my team:")
for player in players[:2]:
	print(player.title())


items = ['boots','sweets','toys','drinks']
print("The first three items on the list are:")
for item in items[:3]:
	print(item.title())


items = ['boots','sweets','toys','drinks']
print("The items from the middle of the list are:")
for item in items[1:4]:
	print(item.title())



items = ['boots','sweets','toys','drinks']
print("The last items on the list are:")
for item in items[-1:]:
	print(item.title())


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(friend_foods)
