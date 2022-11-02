import pandas

# {new_key: new_value for  (index, row) in df.iterrows()}

# todo 1. Create a dictionary in this format:
{"A": "Alpha", "B": "Bravo"}

data = pandas.read_csv("./List Copmrehension and the NATO Alphabet/nato_phonetic_alphabet.csv")
# print(data.to_dict())

new_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_alphabet)

# todo 2. create a list of the phonetic code words from a word that user inputs.
word = input("enter a word: ").upper()
output_list = [new_alphabet[letter] for letter in word]
print(output_list)

