from pypresence import Presence
import time
import random

DRPC_Version = "1.0.2"
running = True

print("===============================")
print(" Da-xn's Rich Presence Creator ")
print("===============================")

print(f"\nVersion {DRPC_Version}\n")

client_id = input("Enter your Client ID: ")
client_state_input = input("Rich Presence State: ")
client_details_input = input("Rich Presence Details: ")

RPC = Presence(client_id)
RPC.connect()
RPC.update(state=f"{client_state_input}", details=f"{client_details_input}")

print("\nRich Precense Updated Successfully!")
print(f"\nState: {client_state_input}")
print(f"Details: {client_details_input}")

quitPrompt = input("Quit? y/n: ")

if (quitPrompt == "Y" or "y"):
    running = False

while (running == True):
    time.sleep(15)
