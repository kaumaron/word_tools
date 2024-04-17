word_length = input("How many letters is the word? ")


with open('dicts/dict.txt') as file:
  n_letter_words = []
  for line in file.readlines():
    if len(line.strip()) == int(word_length):
      n_letter_words.append(line.lower().strip())

print(f'There are {len(n_letter_words)} words in the dictionary with'
       f' {word_length} letters.')

with open(f'dicts/n_letters-{word_length}.txt', 'w') as file:
    file.writelines([f'{n}\n' for n in n_letter_words])

wrong_locations = {i: None for i in range(int(word_length))}
correct_locations = {i: None for i in range(int(word_length))}

included_letters = set(list(input('What letters in the word? ')))
excluded_letters = set(list(input('What letters are not in the word? ')))
knowns = input('Known letters? Use - for unknowns. ')

# input checks
while True:
    if len(knowns) == int(word_length):
        break
    print(f'{len(knowns)} letters entered. Please try again.')
    knowns = input('Known letters? Use - for unknowns. ')

if not included_letters.isdisjoint(excluded_letters):
    print('Overlap between allowed and disallowed letters!')
    overlap = excluded_letters.intersection(included_letters)
    print(f'Removing {overlap} from disallowed.')
    excluded_letters -= overlap


for idx in wrong_locations.keys():
    wrong_locations[idx] = list(
        input(f'Not allowed in {idx + 1}? (Enter to skip): ')
        )

for idx, known in enumerate(list(knowns)):
    if known != '-':
        correct_locations[idx] = known

print(f'included: {included_letters}\nexcluded: {excluded_letters}')

allowed_words = []

if len(included_letters) == 0:
    allowed_words = n_letter_words.copy()
else:
    for i, word in enumerate(n_letter_words):
        if (included_letters.issubset(set(word)) and \
           set(word).isdisjoint(excluded_letters)):
            allowed_words.append(word)

filtered_words = []
for word in allowed_words:
    # collect condition checks, order isn't preserved
    conditions_met = []
    for idx in range(int(word_length)):
        # check if a known letter exists
        if correct_locations[idx]:
            # check if letter is correct else fail test
            if word[idx] == correct_locations[idx]:
                conditions_met.append(0)
            else:
                conditions_met.append(1)
        # check that wrong location is known
        if wrong_locations[idx]:
            if word[idx] in wrong_locations[idx]:
                conditions_met.append(1)
        else:
            conditions_met.append(0)
    if not any(conditions_met):
        filtered_words.append(word)

# remove dups
filtered_words = list(set(filtered_words))

with open(f'allowed/allowed_words-len_{word_length}_'
            f'inc_{"".join(included_letters)}-exc_'
            f'{"".join(excluded_letters)}.txt', 'w') as file:
    file.writelines([f'{n}\n' for n in allowed_words])

label = 'fil_'
for k,v in wrong_locations.items():
    label += str(k + 1)+''.join(v)
label += 'corr_'
for k,v in correct_locations.items():
    if v:
        label += str(k+1) + v


with open(f'filtered/filtered_words-len_{word_length}_'
            f'inc_{"".join(included_letters)}-exc_'
            f'{"".join(excluded_letters)}-{label}.txt', 'w') as file:
    file.writelines([f'{n}\n' for n in filtered_words])

print(f'There are {len(filtered_words)} remaining.')

if input('Do you want to see the remaining words? (y/n) ').lower() == 'y':
    print('\n'.join(filtered_words))
