🎯 Purpose:

A simple console game where the program generates a random number (1–100) and the user tries to guess it.
🧭 Flow

Generates a target number: random.randint(1, 100).
Welcomes the player and describes the game.
Enters a loop asking the user for integer guesses.
Gives feedback: "Too low!", "Too high!", or "Congratulations!" when guessed correctly.
Loop ends when the correct number is guessed.
📌 Key details

Uses infinite while True loop and breaks when guessed correctly.
Assumes user enters valid integers (no error handling for invalid input).
No guess counter or replay option.
🔧 Improvements (optional)

Add input validation with try/except to handle non-integer input.
Keep a guess counter and show attempts.
Offer to play again after success.
Limit attempts for more challenge.
🕹️ Example

Program: "Enter your guess:" → User types "50" → Program replies "Too high! Try again." until the correct number is guessed.

