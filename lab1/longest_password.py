import json


def longest_password():
    with open('passwords.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        longest = max(
            data['people'], key=lambda x: len(x['password']))
        number_of_characters = len(longest['password'])
        print(number_of_characters)


longest_password()
