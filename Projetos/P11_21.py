# 21 em python
import random
import art

print(art.logo)

def cardr():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

end_game = False
soma_total = 0


while not end_game:

    random_value = cardr()
    if random_value == 11:
        as_escolhido = int(input("Você teve a sorte de ter pegado o As, por isso "
              "escolha entre '1' e '11' para continuar!\n"))
        print(f"A sua carta recebida tem o seguinte valor: {as_escolhido}")
        soma_total += as_escolhido
    else:
        print(f"A sua carta recebida tem o seguinte valor: {random_value}")
        soma_total += random_value

    if soma_total > 21:
        print("Infelizmente você perdeu o jogo!")
        print(f"Seu valor final foi {soma_total}!")
        end_game = True
        break
    else:
        print(f"Sua soma atual é {soma_total}!")

    flag = input("Escreva 's' para continuar ou 'n' para desistir: \n").lower()
    if flag == "s":
        continue
    else:
        end_game = True
        print(f"Sua soma final foi {soma_total}!")
        break
