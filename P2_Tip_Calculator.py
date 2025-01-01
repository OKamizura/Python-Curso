print("Welcome to the tip calculator!")

#Input of Variables:
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# Round arredonda o valor, o número 2 é quantas casas decimais, como o setprecision do C++;
final_amount = round(bill_per_person, 2)
#F-String deixa mais facilmente a associação das variáveis com uma string, sem a necessidade de + e de str(variable);
print(f"Each person should pay: ${final_amount}")


