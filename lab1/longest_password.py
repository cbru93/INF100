import json


def longest_password():
    with open('passwords.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        longest = max(
            data['people'], key=lambda x: len(x['password']))
        print(longest)


longest_password()
