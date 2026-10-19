import random

WORDS = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
MAX_TRIES = 6

def random_word():
    return random.choice(WORDS)

def get_guess(word_len, attempt):
    try_guess = input(f"Attempt {attempt}/{MAX_TRIES} – Enter guess: ").strip().lower()

    if not try_guess:
        raise ValueError("Empty input, please enter a word.")
    if len(try_guess) != word_len:
        raise ValueError(f"Wrong length. Expected {word_len}, got {len(try_guess)}.")
    if not (try_guess.isascii() and try_guess.isalpha()):
        raise ValueError("Use only English letters.")

    return try_guess

def check_guess(secret_word, guess):
    return secret_word == guess

def guess_revision(secret_word, guess):
    result = []
    for i in range(len(secret_word)):
        symbol = guess[i]
        if symbol == secret_word[i]:
            result.append(f"[{symbol}]")
        elif symbol in secret_word:
            result.append(f"({symbol})")
        else:
            result.append(symbol)

    print(' '.join(result))

def correct_guess_check(secret_word_len, attempt):
    while True:
        try:
            return get_guess(secret_word_len, attempt)
        except ValueError as e:
            print(e)
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted.")
            raise SystemExit

def play_round():
    secret_word = random_word()
    secret_word_len = len(secret_word)
    print(f"Guess the {secret_word_len}-letter word. You have {MAX_TRIES} tries.")

    attempt = 1

    while True:
        guess = correct_guess_check(secret_word_len, attempt)

        if check_guess(secret_word, guess):
            print("You win!!!")
            break

        guess_revision(secret_word, guess)

        attempt += 1
        if attempt > MAX_TRIES:
            print(f"You lose! The word was: {secret_word}")
            break

def restart_game():
    while True:
        try:
            try_restart = str(input("Do you want to restart? (y/n): ")).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted.")
            raise SystemExit

        if try_restart == "y" or try_restart == "n":
            return try_restart
        else:
            print("Invalid input, please enter 'y' or 'n'.")

if __name__ == "__main__":
    print("Welcome to Wordle!")

    while True:
        play_round()

        restart = restart_game()

        if restart == "y":
            print("Game will be restarted.")
        elif restart == "n":
            print("Have a good day!")
            break

"""
====================================================================
REFLECTION
====================================================================

Напишіть тут коротку рефлексію після завершення роботи.

1. Що саме ви змінили?


2. Чому нова структура коду краща?


3. Що ще можна було б додати, змінити або покращити?


"""
