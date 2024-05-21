# Wordle
Text-based replication of NY Times word game - Wordle

In my first semester of study (B. CompSci), I used Python to create a minigame which replicates the famous NY Times game - Wordle.

How It Works: 

1. A 6-letter word is selceted at random by the system
2. The user has 6 attempts to guess the word. Each guess must be a valid 6-letter word.
3. When the user inputs a guess, each letter in the guessed word will be evaluated as either: missing (black), present with incorrect placement (yellow), or present with correct placement (green)
4.The user can input 'k' or 'K' to display a map showing all keyboard evaluations since the first guess
5. Once the user has guessed the word (each letter is green), a scorecard will be displayed showing how many guesses it took, as well as the current win streak of the user
6. The user can quit at anypoint in the game by inputting 'q' or 'Q'
7. Once the game is over (6 failed guesses or a successful guess) the user can chose to play again or quit the game.
