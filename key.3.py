#!/usr/bin/env python3
import time

def display_challenge():
    banner = r"""
   
 ######  ####### ####### #######    #     # #     # #     # ####### ####### ######   #####  
 #     # #     # #     #    #       #     # #     # ##    #    #    #       #     # #     # 
 #     # #     # #     #    #       #     # #     # # #   #    #    #       #     # #       
 ######  #     # #     #    #       ####### #     # #  #  #    #    #####   ######   #####  
 #   #   #     # #     #    #       #     # #     # #   # #    #    #       #   #         # 
 #    #  #     # #     #    #       #     # #     # #    ##    #    #       #    #  #     # 
 #     # ####### #######    #       #     #  #####  #     #    #    ####### #     #  #####  
                                                                                            
                                                                            7H3 HUN73R 0000                  

    """
    challenge = """
    🔐 LOGIN USING THE BELOW CREDENTIALS TO UNLOCK THE TEAM INVITE LINK 🔐

    USERNAME          → root
    PASSWORD (HASHED) → aeb4af8051636122485358d10b021a6ebd78072a
    LINK (ENCRYPTED)  → aHR0cHM6Ly9yb290LWh1bnRlcnMudXAucmFpbHdheS5hcHAvd2VsY29tZQ

    🚨 MISSION: Decrypt the hashed password and decode the encrypted link to gain access.
               Only the worthy will claim their spot.

    💻 Crack. Decode. Dominate.
    """
    
    print("\033[1;31m")  # Red color
    print(banner)
    print("\033[1;36m")  # Cyan color
    for char in challenge:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print("\033[0m")     # Reset color

if __name__ == "__main__":
    display_challenge()
