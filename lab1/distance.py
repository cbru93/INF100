"""Distance."""

from decimal import Decimal, ROUND_DOWN


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Calculate the distance between two points."""
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print("x1 = ")
x1_value = int(input())
print("y1 = ")
y1_value = int(input())
print("x2 = ")
x2_value = int(input())
print("y2 = ")
y2_value = int(input())


dist = distance(x1_value, y1_value, x2_value, y2_value)
dist_str = str(Decimal(str(dist)).quantize(Decimal("0.000000000"), rounding=ROUND_DOWN))
print(f"Avstanden mellom ({x1_value}, {y1_value}) og ({x2_value}, {y2_value}) er {dist_str}")
