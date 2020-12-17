def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')