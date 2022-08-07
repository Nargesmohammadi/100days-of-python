fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + "pie")


make_pie(4)

facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'likes': 13, 'comments': 2, 'shares': 1},
    {'likes': 33, 'comments': 8, 'shares': 3},
    {'comments': 4, 'shares': 2},
    {'comments': 1, 'shares': 1},
    {'likes': 19, 'comments': 3}
]
total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        pass

print(total_likes)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("./Day30/nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# for continuing the code:
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
