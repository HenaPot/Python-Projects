# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def breakline_remover(string):
    if "\n" in string:
        return string[:-1]
    else:
        return string


names_file = open("./Input/Names/invited_names.txt")
bday_invitation_text = open("./Input/Letters/starting_letter.txt")
clean_names = []
for name in names_file.readlines():
    clean_names.append(breakline_remover(name))

clean_text = []
for item in bday_invitation_text.readlines():
    clean_text.append(breakline_remover(item))

for clean_name in clean_names:
    with open(f"./Output/ReadyToSend/letter for {clean_name}.txt", mode="w") as file:
        for clean_line in clean_text:
            if "[name]" in clean_line:
                clean_line = clean_line.replace("[name]", clean_name)
            file.write(f"{clean_line}\n")

names_file.close()
bday_invitation_text.close()
