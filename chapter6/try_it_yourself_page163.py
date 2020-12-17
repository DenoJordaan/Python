Glossary = {'slice':'it cuts information','statements':'meh','parameters':'stuff you put in brackets','objects':'is a key'}

for key, value in Glossary.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")


rivers = {'nile':'egypt','orange':'south africa','amazon':'south america'}

for key, value in rivers.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")


	favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")