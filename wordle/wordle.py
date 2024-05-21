"""
Wordle Game (Text-Based UI)
"""

from string import ascii_lowercase

from typing import Optional

from wordle_support import (
    load_words,
    choose_word,
    VOCAB_FILE,
    ANSWERS_FILE,
    CORRECT,
    MISPLACED,
    INCORRECT,
    UNSEEN,
)


__author__ = "Jacob Habchi"
__email__ = "jacobhabchi11@hotmail.com"



def has_won(guess: str, answer: str) -> bool:
    """Funtion 5.1: has_won

    Returns True if the guess matches the answer perfectly. Otherwise, returns False.

    Parameters:
        guess (str): the guess based on user input
        answer (str): random answer derived from ANSWERS_FILE
        
    Returns:
        bool: True if guess == answer. False otherwise.
    
    Precondition:
        len(guess) == 6 and len (answer) == 6
    """
    if guess == answer and len(guess and answer)==6:
        return True
    else:
        return False
    
def has_lost(guess_number:int) -> bool:
    """Funtion 5.2: has_lost

    Returns True if the number of guesses by the user is >= 6, where 6 is the max
    number of guesses allowed. Otherwise, returns False.

    Parameters:
        guess_number(int): number of user guesses.
        
    Returns:
        bool: True if number of guesses >= 6. False otherwise.
    """
    if guess_number >= 6:
        return True
    else:
        return False
    
def remove_word(words: tuple[str, ...], word: str) -> tuple[str,...]:
    """Funtion 5.3: remove_word

    Returns a copy of words with word removed.
    
    Assumption:
        word appears in words exactly once.

    Parameters:
        words (tuple[str,...]): tuple of words incuding word
        word (str): word to be removed from words.
        
    Returns:
        tuple[str,...]: contains words with word removed
    """
    new_words=tuple()
    for wanted in words:
        if wanted!=word:
            new_words += (wanted,)
    return new_words

def prompt_user(guess_number:int, words: tuple[str,...]) -> str:
    """Funtion 5.4: prompt_user

    Prompts the user for their next guess, repeating until user inputs valid guess,
    requests help, lauches the keyboard, or quits the game.

    Parameters:
        guess_number (int): guess number
        words (tuple[str...]): words imported from "vocab.txt" in which a valid guess can be matched to.
        
    Returns:
        str: valid guess
    """
    spec = "KkHhQq"
    while True:
        attempt = (input("Enter guess " + str(guess_number) + ": ")).lower()
        if attempt not in words and len(attempt)==6 and attempt not in spec:
           print("Invalid! Unknown word")
        elif len(attempt)!=6 and attempt not in spec:
            print("Invalid! Guess must be of length 6")
        elif attempt in words or attempt in spec:
            return attempt
            break
        

def process_guess(guess: str, answer: str) -> str:
    """Funtion 5.5: process_guess

    Converts the guess into a modified representation based on wordle characters.
    
    Parameters:
        guess (str): the guess based on user input
        answer (string): answer imported from ANSWERS_FILE

    Returns:
        str: wordle characters representing guess accordingly
    
    Precondition:
        len(guess) == 6 and len (answer) == 6
    """
    result = [INCORRECT] * len(answer)
    for position in range(len(answer)):
        if guess[position] == answer[position]:
            result[position] = CORRECT
            answer = answer.replace(guess[position], INCORRECT, 1)
    for position in range(len(answer)):
        if guess[position] in answer:
            result[position] = MISPLACED
            answer = answer.replace(guess[position], INCORRECT, 1)
    return "".join(result)


def update_history( history: tuple[tuple[str, str], ...], guess: str,answer: str ) -> tuple[tuple[str, str], ...]:
    """Funtion 5.6: update_history

    Returns a copy of history updated to include the most previou guess
    and its wordle representation. 
    
    Parameters:
        history (tuple[tuple[str,str],...]): tuple of (guess,processed_guess)
        guess (str): guess input by user
        answer (str): answer imported from ANSWERS_FILE
        
    Returns:
        tuple[tuple[str,str],...]: multiple tuples of (guess,processed_guess)
    """
    
    processed = process_guess(guess,answer)
    previous = (guess, processed)
    return history + ((previous),)
    

def print_history(history: tuple[tuple[str, str], ...]) -> None:
    """Funtion 5.7: print_history

    Displays the guess history by corresponding each letter to its wordle character below.
    
    Parameters:
        history (tuple[tuple[str,str],...]): tuple of (guess,processed_guess)
        
    Returns:
        None
    """
    print("-" * 15)
    trial = 0
    for guess in history:
        trial += 1
        print("Guess " + str(trial) + ":  " + " ".join(guess[0]) + "\n" + " " * 9 + guess[1])
        print("-" * 15)
    print()

def print_keyboard(history: tuple[tuple[str, str], ...]) -> None:
    """Funtion 5.8: print_keyboard

    Prints an updated keyboard by correspoding each individual letter to its wordle chracter. 
    
    Parameters:
        history (tuple[tuple[str,str],...]): tuple of (guess,processed_guess)
        
    Returns:
        None
    """
    print()
    print("Keyboard information")
    print ("-" * 12)
    keys = list(ascii_lowercase)
    d = {}
    for key in keys:
        d[key] = " "
        
    for char,squares in history:
        for letters in range(len(char)):
                d[char[letters]] = squares[letters]
    group = list(d.items())
    
    count = 0
    for letter in range(len(group)):
        if count == 0:
            letter = group[count][0]
            square = group[count][1]
            print(letter + ": " + square, end = "\t")
        elif count % 2 == 0 and count != 0:
            letter = group[count][0]
            square = group[count][1]
            print(letter + ": " + square, end = "\t")
        elif count % 2 != 0:
            
            letter = group[count][0]
            square = group[count][1]
            print(letter + ": " + square, end = "\n")
        count += 1
    print()


def print_stats(stats: tuple[int, ...]) -> None:
    """Funtion 5.9: print_stats

    Prints the game stats updated after each game is either won or lost.
    - Displays to the user the number of moves required to win
    - Displays total number of games lost
    
    Parameters:
        stats (tuple[int,...]): tuple of 7 characters, where the first
                                6 are the guesses required to win, and the
                                last is the number of games lost.  
    Returns:
        None
    """
    print()
    moves = 0
    print("Games won in:")
    for element in range(len(stats)):
        moves += 1
        if moves <= 6:
            print(str(moves) + " moves: " + str(stats[element]))
    print("Games lost: " + str(stats[-1]))
    

def main():
    """Funtion 5.10: main funtion
    The main funtion calls upon previously defined functions to run the wordle game.
    """
    all_answers = load_words(ANSWERS_FILE)
    answer = choose_word(all_answers)
    
    vocab = load_words("vocab.txt")
    answers = load_words("answers.txt")
    
    history = ()
    
    guess_count = 1
    
    help_request = "Ah, you need help? Unfortunate."

    stats = [0, 0, 0, 0, 0, 0, 0]
    lost_games = stats[-1]
    lose_count = 0
    win_count = 0
    
    while True:
        guess = prompt_user(guess_count, vocab)
        if guess in "Qq":
            break
        
        elif guess in "Hh":
            print(help_request)
            continue
        
        elif guess in "Kk":
            print_keyboard(history)
            continue
            
        history = update_history(history, guess, answer)
        print_history(history)
        guess_count += 1
        
        if guess == answer:
            print("Correct! You won in " + str(guess_count - 1) + " guesses!")
            win_count += 1
            stats[guess_count - 2] += win_count
            print_stats(stats)
            keep_playing = input("Would you like to play again (y/n)? ")

            if keep_playing in "Yy":
                history = ()
                guess_count = 1
                win_count = 0
                answer = choose_word(all_answers)
                continue
            
            if keep_playing in "Nn":
                break
            
        else:
            if guess_count > 6:
                print("You lose! The answer was: " + answer)
                lose_count += 1
                stats[-1] = lose_count
                print_stats(stats)
                keep_playing = input("Would you like to play again (y/n)? ")
                
                if keep_playing in "Yy":
                    history = ()
                    guess_count = 1
                    answer = choose_word(all_answers)
                    continue
                
                if keep_playing in "Nn":
                    break

if __name__ == "__main__":
    main()
