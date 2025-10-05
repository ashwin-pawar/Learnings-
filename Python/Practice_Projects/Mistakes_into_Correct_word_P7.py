# Correct Word Checker 
#importing library 

from spellchecker import SpellChecker

# creating class where all the logic will written
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self,text): #text is input enter by user 
        words = text.split()
        corrected_words = []  #list

        for word in words:
            corrected_word = self.spell.correction(word)  #corrected_word - funtion  correction- it'll check word is correct or wrong
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)

        # joining the all word or sentence which we splited using split() method
        return ' '.join(corrected_words)
    
    # running the app(Code)

    def run_text(self):
        print("\n---SPELL CHECKER---")

        while True:
            text = input("Enter the Sentence/Word  to Check or Type (quit) to exit : ")
            if text.lower() == "quit":
                print("Closing the Program.....🫡")
                break 

            corrected_text = self.correct_text(text)  #this will check input word and correct it
            print(f"Corrected Text : {corrected_text}")

#running the main program 
if __name__ == "__main__":
    SpellCheckerApp().run_text()

# ---OUTPUT---

    # ---SPELL CHECKER---
    # Enter the Sentence/Word  to Check or Type (quit) to exit : prograam
    # Correcting "prograam" to "program"
    # Corrected Text : program
    # Enter the Sentence/Word  to Check or Type (quit) to exit : pythoon
    # Correcting "pythoon" to "python"
    # Corrected Text : python
    # Enter the Sentence/Word  to Check or Type (quit) to exit : jupyterr
    # Correcting "jupyterr" to "jupiter"
    # Corrected Text : jupiter
    # Enter the Sentence/Word  to Check or Type (quit) to exit : quit
    # Closing the Program.....🫡

# Learning:
# In this project, I learned how to use the SpellChecker library to identify and correct misspelled words in a given text.
# The program splits the input text into individual words, checks each word for spelling errors, and suggests corrections
# in this i learn about SpellChecker Library and its functions like correction() and how to implement it in a class structure.
