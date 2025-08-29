def add(a, b):
    return a + b


user_input1 = input("Oppgi et tall: ")
user_input2 = input("Oppgi et tall til: ")

a = int(user_input1)
b = int(user_input2)

result = add(a, b)
print("Summen av tallene er ", result)
