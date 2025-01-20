from random import randint

Ez_turns = 10
Hd_turns = 5

def set_difficult():
    level = input("Para escolher a dificuldade do jogo, escolha 'facil' ou 'dificil' !:").lower()
    if level == "facil":
        return Ez_turns
    else:
        return Hd_turns

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Muito alto.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Muito baixo.")
        return turns - 1
    else:
        print("Acertou!")

def game():
    print("Estou pensando em um número entre 1 e 100.")
    answer = randint(1, 100)

    turns = set_difficult()

    guess = 0
    while guess != answer:
        print(f"Você ainda tem {turns} tentativas restantes.")

        guess = int(input("Faça uma tentativa: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Acabaram suas tentativas, você perdeu!")
            return
        elif guess != answer:
            print("Tente novamente.")


game()

