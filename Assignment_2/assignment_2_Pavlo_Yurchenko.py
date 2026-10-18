import random

def random_word(arr):
    return random.choice(arr)

def get_guess(word_len, to_def_attempt, to_def_max_tries):
    try_guess = input(f"Attempt {to_def_attempt}/{to_def_max_tries} – Enter guess: ").strip().lower()

    if not try_guess:
        raise ValueError("Empty input, please enter a word.")
    if len(try_guess) != word_len:
        raise ValueError(f"Wrong length. Expected {word_len}, got {len(try_guess)}.")
    if not (try_guess.isascii() and try_guess.isalpha()):
        raise ValueError("Use only English letters.")

    return try_guess

def check_guess(to_def_secret_word, to_def_guess):
    if to_def_secret_word == to_def_guess:
        return True

    return False

def guess_revision(to_def_secret_word_len, to_def_guess):
    result = []
    for i in range(to_def_secret_word_len):
        symbol = to_def_guess[i]
        if symbol == secret_word[i]:
            result.append("[" + symbol.upper() + "]")
        elif symbol in secret_word:
            result.append("(" + symbol + ")")
        else:
            result.append(" " + symbol + " ")

    print(''.join([c for c in result if c]))

if __name__ == "__main__":
    words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
    secret_word = random_word(words)
    max_tries = 6
    attempt = 1
    secret_word_len = len(secret_word)

    print("Welcome to Wordle!")
    print(f"Guess the {secret_word_len}-letter word. You have {max_tries} tries.")

    while True:
        while True:
            try:
                guess = get_guess(secret_word_len, attempt, max_tries)
                break
            except ValueError as e:
                print(e)
            except (EOFError, KeyboardInterrupt):
                print("\nGame interrupted.")
                raise SystemExit

        if check_guess(secret_word, guess):
            print("You win!!!")
            break

        guess_revision(secret_word_len, guess)

        attempt += 1
        if attempt > max_tries:
            print(f"You lose! The word was: {secret_word}")
            break
