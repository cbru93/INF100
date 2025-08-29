import json

def main():
    # Read the grunntall from joker.json
    try:
        with open('joker.json', 'r') as file:
            data = json.load(file)
            grunntall = data['grunntall']
    except FileNotFoundError:
        print("Error: joker.json file not found")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in joker.json")
        return
    except KeyError:
        print("Error: 'grunntall' key not found in joker.json")
        return
    
    # Apply the strategy: "opp" if number <= 4, "ned" otherwise
    for tall in grunntall:
        if tall <= 4:
            print("opp")
        else:
            print("ned")

if __name__ == "__main__":
    main()
