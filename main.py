import requests

def open_file():
    with open("./usernames/usernames.txt") as f:
        lines = f.readlines()
    return lines

def main():
    try:
        lines = open_file()
    except Exception as e:
        print(f'Error: {e}')

    for username in lines:
        try:
            username = username.strip() 
            user_taken = requests.get(f"https://night-light.cz/responses.php?getAccount={username}")
            if not user_taken.text == "true":
                print(f"Username : {username} - Available !")
        except Exception as e:
            print(f"Error occured: {e}")

main()
