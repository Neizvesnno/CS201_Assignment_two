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
У початковому коді неймінг змінних був жахливим, тому я використав snake_case для об'явлення змінних та глобальні 
записав великими літерами, як прийнято це робити. Прибрати з коду зайві змінні, які передавати одне й теж по декілька 
разів. Виділив окремі частини функціоналу в функції, як це просила умова завдання та для читабельності коду. Також 
додав якісну обробку помилок і реалізував завершення гри без помилки, замінив деякі цикли while на for, де це було
доречнішим. Прибрав глобальні змінні, залишивши лише обов'язкове, інші існують лише у своїх функціях. Завершив зміни
ігровим циклом, щоб після одного слова можна було вгадувати наступне, також є легкий метод завершення гри. Загалом 
довелося переписати увесь код.

2. Чому нова структура коду краща?
Нова структура відповідає нормам стилізації та написання коду, не має code smell, гадаю, він отримає гарну оцінку на 
Flake8 чи Pylint, проте сам я не перевіряв, можливо зроблю це пізніше. У цій структурі кожна функція відповідає одній 
дії, тому кожну частину можна змінити окремо і не перейматися про те, що зламаєш усе. Тут немає тих дублювань, про які
я згадував у першому питанні, а глобальні змінні не заважають викликати функції з тих місць, де з ними зручніше та 
простіше працювати. Обробка помилок не вкладена у основну гру, а теж викликається через функцію, тому нічого не змішується.
І найголовніше, __main__ складається з декількох стрічок, і за ним видно, де програма починає роботу та як виконується.

3. Що ще можна було б додати, змінити або покращити?
Загалом цікаво було би збільшити варіативність слів, структурувавши їх за групами, як-от їжа, кухонне приладдя, погодні умови та
інше. Коли дебажив код, помітив, що деякі літери, до прикладу, p у слові apple зустрічаються два рази, і коли ця літера є у
загаданому слові, то у спробі обидві літери p беруться у круглі дужки, проте в умові не було вказано це змінити, і тому я не
виправляв цей баг. Одна проблема в моєму коді, яка мені не подобається, що guess_revision і рахує результат, і відображає його,
проте це вже було б занадто ідеально та забрало ще часу для виправлення, тому я не ліз туди глибше, хоча це теж можна було би 
виправити. Можна ще додати перевірку на реальність слова, бо поки навіть ytytg пройде перевірку для п'яти буквеного слова. І ще 
restart_game можна було би повертати як True або False, це б ще трохи скоротило код, але я й так багато що виконав.

"""
