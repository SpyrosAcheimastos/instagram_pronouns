import os
import json
import itertools

# Read all english words
dictionary = json.load(open('dictionary.json', 'r'))

# Read all instagram pronouns
pronoun_list = []
for file in os.listdir('pronouns'):
    pronoun_list += open(f'pronouns/{file}', 'r').read().split('\n')

# Keep unique pronouns (209 -> 175)
pronoun_list = sorted(set(pronoun_list))

# Find combinations of pronouns that appear in the dictionary
possible_words_dict = {}
for num_of_pronouns in range(1, 5):
    for pronouns in itertools.permutations(pronoun_list, num_of_pronouns):
        word = ''.join(pronouns)
        if word in dictionary:
            possible_words_dict[word] = '/'.join(pronouns)

# Sort possible words
possible_words_dict = dict(sorted(possible_words_dict.items()))

# Save possible words
with open('possible_words.txt', 'w') as f:
    for word, pronouns in possible_words_dict.items():
            f.write(f'{word: <20}{pronouns}\n')  