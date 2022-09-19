# -*- coding: utf-8 -*-
"""
Tommy Le
CPSC 223P-01
Sun April 11, 2021
tommyle@fullerton.edu
"""

import random

# Hangman class.
class Hangman:
    def __init__(self, word, triesAllowed):
        self.word = word
        self.triesAllowed = triesAllowed
        self.letter = ""
        self.displayWord = '-' * len(self.word)
        self.letterUsed = ""
        self.letterFound = True
        self.wordBackup = word
        self.wordList = list(self.word)

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        self.letterUsed += letter
        self.letter = letter.lower()
        for i in range(len(self.word)):
            if self.letter in self.word:
                temp = list(self.word)
                temp[i] = self.letter
                self.wordBackup = "".join(temp)
                return True
            if self.letter not in self.word:
                self.triesAllowed -= 1
                return False
        return False

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        return self.triesAllowed

    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        wordList = list(self.word)
        counter = ''
        for i in range(len(self.word)):
          temp = 0
          for j in range(len(self.letterUsed)):
            if self.word[i] == self.letterUsed[j]:
              temp = 1
          if temp == 0:
            wordList[i] = '-'
        for v in wordList:
          counter += v
        return counter

    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        return self.letterUsed

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        if self.word in self.GetDisplayWord():
            return True
        if self.word not in self.GetDisplayWord() and self.triesAllowed  == 0:
            return False

    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        pass



# implement the logic of your game below
if __name__ == "__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()

    # Seed the random number generator with current system time
    random.seed()

    # Convert the string of words in wordFile to a list,
    # then get a random word using
    # randomIndex = random.randint(min, max)
    wordFileList = wordFileText.split()
    randomWordindex = random.randint(0, len(wordFileList) - 1)
    randomWord = wordFileList[randomWordindex]

    # Instantiate a game using the Hangman class
    wordLen = len(randomWord)
    game = Hangman(randomWord, wordLen)
    print("Here's your word so far: ", game.GetDisplayWord())
    print("You have " + str(game.GetNumTriesLeft()) + " tries left")
    
    # Use a while loop to play the game
    counter = wordLen
    while counter >= 1:
        print("Guess a letter: ")
        guessletter = input()
        game.Guess(guessletter)

        if guessletter in randomWord:
          print("Good Guess! Letters used: " + game.GetLettersUsed())
        else:
          print("Too bad! Letters used: " + game.GetLettersUsed())
          

        counter = game.GetNumTriesLeft()

        gamestatus = game.GetGameResult()

        print("Here's your word so far: ", game.GetDisplayWord())

        print("You have " + str(game.GetNumTriesLeft()) + " tries left")

        if gamestatus == True:
          print("Congratulations! You Won!! The word was " + randomWord)
          break
        if gamestatus == False:
          print("You lost. The word was " + randomWord)
          break
