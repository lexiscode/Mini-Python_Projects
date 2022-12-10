import random

print("##THE HANGMAN GAME##\n")

## GENERATE A RANDOM WORD ##
words = ['the', 'keywords', 'for', 'the', 'four', 'data', 'modifiers', 'are', 'signed', 'unsigned', 'short', 'and', 'long', 'you', 'also', 
         'going', 'learn', 'about', 'several', 'mathematical', 'functions', 'provided', 'by', 'language', 'such']
# Pick a word/string at random from the list above
rword_str = random.choice(words)

## GENERATE AS MANY BLANK-DASHES AS LETTERS IN THE WORD
# Convert the word/string to a list
space_join = ' '.join(rword_str)
rword_list = space_join.split()
print(rword_list)
# Replace the list indexes with dashes, then convert back to a string format
for i in range(len(rword_list)):
    rword_list[i] = ' __ '
    #print(rword_list)
#print(rword_list)
str_rword_list = ''.join(rword_list) #back to string
print(f"Guess the letters: {str_rword_list}\n") 

while '__' in str_rword_list:
    ##ASK THE USER TO GUESS A LETTER
    guessed_letter = input("Guess a letter: ")
    guessed_letter.lower()

    #CHECK IF THE GUESSED LETTER IS IN THE WORD
    copy_rword_list = space_join.split() 

    if guessed_letter in copy_rword_list:
        # Search the index where the guessed letter is located
        index_search = copy_rword_list.index(guessed_letter)
        # Replace the blankdash-value where the index is located in the rword_list, with the guessed letter 
        rword_list[index_search] = guessed_letter
        #print(rword_list)
        # Change rword_list back to string
        str_rword_list = ''.join(rword_list) #back to string
        print(str_rword_list)

        #Check if all the blank-dashes are filled or not
        if '__' not in str_rword_list:
            print("\nYOU WIN!!!\nGAME OVER!")
