from art import logo, vs
from game_data import data
import random

def format_data(account):

  account_name = account["name"]
  account_descr = account["descryption"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
  if a_followers > b_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:
  account_a = account_b
  account_b = random.choice(data)
  print(f"A: {format_data(account_a)}.")
  print(vs)
  print(f"contra B: {format_data(account_b)}.")

  guess = input("Quem tem mais seguidores? Escreva 'A' ou 'B': ").lower()
  print("\n" * 20)
  print(logo)

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    score += 1
    print(f"Acertou! Seu(s) ponto(s) atual(is) : {score}!")
  else:
    print(f"Errou. Sua pontuação final : {score}!")
    game_continue = False

