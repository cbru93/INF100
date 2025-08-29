def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))


print(
    f"Avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er {distance(x1, y1, x2, y2)}")
