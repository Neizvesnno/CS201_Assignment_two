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

# while tries != 0:
#     guess = input("Attempt " + str(7 - tries) + "/6 – Enter guess: ").lower()
#
#     if guess == secret_word:
#         print("You win!!!")
#         break
#
#     result = [];
#     i = 0
#     while i < secret_word_len:
#         ch = guess[i]
#         if ch == secret_word[i]:
#             result.append('correct')
#         elif ch in secret_word:
#             result.append('present')
#         else:
#             result.append('absent')
#         i += 1
#
#     display = []
#     j = 0
#     while j < secret_word_len:
#         s = guess[j]
#         res = result[j]
#         if res == 'correct':
#             display.append("[" + s.upper() + "]")
#         elif res == 'present':
#             display.append("(" + s + ")")
#         else:
#             display.append(" " + s + " ")
#         j += 1
#
#     junk = ''.join([c for c in display if c])
#     print("Result:", ' '.join(display))
#     tries -= 1
# else:
#     print(f"You lose! The word was: {secret_word}")

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

        ###


        attempt += 1
        if attempt > max_tries:
            print(f"You lose! The word was: {secret_word}")
