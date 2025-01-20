try:
  age = int(input("Quantos anos você tem?: "))
except ValueError:
  print("Você inseriu um valor incorreto.")
  age = int(input("Quantos anos você tem? :"))

if age >= 18:
  print(f"Você pode dirigir com essa idade : {age}.")
