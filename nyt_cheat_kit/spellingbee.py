word_length = 7
min_length = 4

with open('../word_search/dicts/dict.txt') as file:
  n_letter_words = []
  for line in file.readlines():
    if min_length <= len(line.strip()):
      n_letter_words.append(line.strip())

included_letters = set(list(input('What letters in the word? ')))
center_letter = input('Center letter? ')

# input checks
while True:
    if len(included_letters) == word_length:
        break
    print(f'{len(included_letters)} letters entered. Please try again.')
    included_letters = input('What letters in the word? ')

while True:
    if len(center_letter) == 1:
        break
    print(f'{len(center_letter)} letters entered. Please try again.')
    knowns = input('center letter? ')

print(f'included: {included_letters}\ncenter: {center_letter}')

filtered_words = []
best_word = ''
for word in n_letter_words:
    if set(word).issubset(included_letters) and (center_letter in word):
        if set(word) == included_letters:
           best_word = word
        filtered_words.append(word)

filtered_words = sorted(filtered_words, key=lambda x: len(x), reverse=True)

print(f'There are {len(filtered_words)} in the list.'
      f'\n The highest scoring word is {best_word}.')

if input('Do you want to see the words? (y/n) ').lower() == 'y':
    print('\n'.join(filtered_words))
