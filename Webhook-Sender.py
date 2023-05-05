import requests
import json

print("OWNED BY G4ME TOOLS -> DISCORD: https://discord.gg/vn67dFgnCE")

print("""
,                                       ▄
▄█▀▀▀                    ▌      ▐    ▐     ,     █       █▀▀▀▀▀▀▀▀       ▀▀▀     ▐▀▀▀▀     ▄█▀▀▀     ,      ▄█▀▀▀     ,       ▌           ▀▀▀═▄▄▄▄▄
█     ▀▀▀▀▀      ,▓     ▐       ▐     ▌   ,█     ▌                               █        ▐█         ▐     ▐█         ▐      ▐                 ▀
▐          ▄     ═▀      ▀       █         █     ▐▌             █                ▐▌        ▐          ▐     ▐          ▐      █        ▄▄
▐  ▄▄⌐     ▌               ▄     ▌        █      █       ███████▀                ▐         ▐         ,█     ▐          █     ▐▌          ▀▀▀▄▄     ▄
   ▀      ▐▌ ▄▄▄▄▄▄     ▄▄▄█    ▐▌       █       ▌                               █                  ,█               ,█                            ▌
          █             █       ▓       █       ▐               ▐▌              ▐▌      ▄         ,▄█    ▄         ,▄█              █           ▄█
▀▄▄▄▄▄▄▄█═▄▄▌        ▄▄▄▄▄▌   ╔▄▄▄█   ╒▄▄█▀   ▄▄▄▄█  ╔▄▄▄▄▄▄▄▄▄▄▄▄█           ▄▄▄▄█        ▀&▄▄▄▄▄▄█▀▀      ▀&▄▄▄▄▄▄█▀▀   ▄▄▄▄▄▄▄▄▄▄▄▄▌ ▀▀▄▄▄▄▄▄▄██▀ 
""")

# Prompt the user to enter their Discord webhook URL
webhook_url = input("Enter your Discord webhook URL: ")

# Prompt the user to enter the message to be sent
message = input("Enter the message you want to send: ")

# Prompt the user to enter the number of times to send the message
num_times = int(input("Enter the number of times to send the message: "))

# Define the payload
payload = {
    "content": message
}

# Send the request num_times number of times
for i in range(num_times):
    response = requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    
    # Check the response status code
    if response.status_code == 204:
        print(f"Message {i+1} sent successfully!")
    else:
        print(f"Failed to send message {i+1}. Error {response.status_code}: {response.text}")
