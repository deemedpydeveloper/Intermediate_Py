PLACEHOLDER = '[Friend]'

with open('./Input/Names/names.txt') as names_file:
    names = names_file.readlines()   # stores as a list.

with open('./Input/Letters/letter.txt') as letter_file:
    letter_contents = letter_file.read()  # accessing letter contents by read mode.
    # replace the placeholder with names in names list.
    for name in names:
        stripped_name = name.strip()  # Since, list contains name/n.
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # replacing is done.
        # write files into output folder.
        with open(f'./Output/Ready_to_send/letter_to_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)