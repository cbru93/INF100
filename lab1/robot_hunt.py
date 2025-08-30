"""Robot hunt."""

# Input
print('Hvor mange roboter er det nå?')
population = int(input())
hunting_licenses = [10, 7, 18]
year = 0

# Første år
population = population + (population // 10)  # til sommeren
population = population - hunting_licenses[year]  # til høsten
year += 1
print(f'Om {year} år er det {population} roboter i flokken')

# Andre år
population += population // 10
population -= hunting_licenses[year]
year += 1
print(f'Om {year} år er det {population} roboter i flokken')

# Tredje år
population += population // 10
population -= hunting_licenses[year]
year += 1
print(f'Om {year} år er det {population} roboter i flokken')
