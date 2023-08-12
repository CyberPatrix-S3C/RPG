#!/usr/bin/env python

import secrets
import random
import string
import time
import sys
import os

from core.delay_print import delay_print, fast_delay_print
from argparse import ArgumentParser
from colorama import init, Fore, Back, Style


init(autoreset=True)
# clear the terminal
os.system("clear")


__author__ = Fore.WHITE+"CyberPatriX-S3C"
__version__ = Fore.WHITE+"1.0.3"


# Banner
print (Fore.BLUE+"""

                                                             
                                                             
RRRRRRRRRRRRRRRRR   PPPPPPPPPPPPPPPPP           GGGGGGGGGGGGG
R::::::::::::::::R  P::::::::::::::::P       GGG::::::::::::G
R::::::RRRRRR:::::R P::::::PPPPPP:::::P    GG:::::::::::::::G
RR:::::R     R:::::RPP:::::P     P:::::P  G:::::GGGGGGGG::::G
  R::::R     R:::::R  P::::P     P:::::P G:::::G       GGGGGG
  R::::R     R:::::R  P::::P     P:::::PG:::::G              
  R::::RRRRRR:::::R   P::::PPPPPP:::::P G:::::G              
  R:::::::::::::RR    P:::::::::::::PP  G:::::G    GGGGGGGGGG
  R::::RRRRRR:::::R   P::::PPPPPPPPP    G:::::G    G::::::::G
  R::::R     R:::::R  P::::P            G:::::G    GGGGG::::G
  R::::R     R:::::R  P::::P            G:::::G        G::::G
  R::::R     R:::::R  P::::P             G:::::G       G::::G
RR:::::R     R:::::RPP::::::PP            G:::::GGGGGGGG::::G
R::::::R     R:::::RP::::::::P             GG:::::::::::::::G
R::::::R     R:::::RP::::::::P               GGG::::::GGG:::G
RRRRRRRR     RRRRRRRPPPPPPPPPP                  GGGGGG   GGGG

""")
__info = '''
---[ {c}Version :  {v}           ]---
---[ {c}Aiuthor :  {a} ]---
'''.format(a=__author__, v=__version__, c=Fore.BLUE)

print (__info)


# Setting up the Argument Parser
parser = ArgumentParser(
    prog='Password Generator.',
    description='Generate any number of passwords with this tool.'
)

# Adding the arguments to the parser
parser.add_argument("-n", "--numbers", default=0, help="Number of digits in the PW", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Number of lowercase chars in the PW", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Number of uppercase chars in the PW", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Number of special chars in the PW", type=int)

# add total pw length argument
parser.add_argument("-t", "--total-length", type=int, 
                    help="The total password length. If passed, it will ignore -n, -l, -u and -s, " \
                    "and generate completely random passwords with the specified length")

# The amount is a number so we check it to be of type int.
parser.add_argument("-a", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

# Parsing the command line arguments.
args = parser.parse_args()


# list of passwords
passwords = []
# Looping through the amount of passwords.
for _ in range(args.amount):
    if args.total_length:
        # generate random password with the length
        # of total_length based on all available characters
        passwords.append("".join(
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                for _ in range(args.total_length)]))
    else:
        password = []
        # If / how many numbers the password should contain  
        for _ in range(args.numbers):
            password.append(secrets.choice(string.digits))

        # If / how many uppercase characters the password should contain   
        for _ in range(args.uppercase):
            password.append(secrets.choice(string.ascii_uppercase))
        
        # If / how many lowercase characters the password should contain   
        for _ in range(args.lowercase):
            password.append(secrets.choice(string.ascii_lowercase))

        # If / how many special characters the password should contain   
        for _ in range(args.special_chars):
            password.append(secrets.choice(string.punctuation))

        # Shuffle the list with all the possible letters, numbers and symbols.
        random.shuffle(password)

        # Get the letters of the string up to the length argument and then join them.
        password = ''.join(password)

        # append this password to the overall list of password.
        passwords.append(password)

# Store the password to a .txt file.
if args.output_file:
    with open(args.output_file, 'w') as f:
        f.write('\n'.join(passwords))
        
if not sys.argv[1:]:
        print (Fore.YELLOW+"["+Fore.RED+"X"+Fore.YELLOW+"] Type"+Fore.WHITE+" python rpg.py -h "+Fore.YELLOW+"to view the mannual")
        delay_print ("[-] Exiting...")
        print (" ")
        time.sleep(0.7)
        sys.exit(0)
        
else:
        # Printing the output to the terminal.
		print (Fore.BLUE+"["+Fore.WHITE+"*"+Fore.BLUE+"] Generating Random Password"+Fore.WHITE+"... ")
		time.sleep(0.7)
		print(Fore.BLUE+"**********************************************")
		print (Fore.BLUE+'['+Fore.WHITE+'+'+Fore.BLUE+'] P@SSW0RD >> ', end="")
		delay_print ("".join(passwords))
		print(Fore.BLUE+"\n**********************************************")
		print (" ")

		if args.output_file:
			print (Fore.BLUE+"["+Fore.WHITE+"+"+Fore.BLUE+"] Saving Generated Password to "+Fore.YELLOW+args.output_file+Fore.BLUE+"...",end="")
			time.sleep(3)
			print (Fore.GREEN+"Done.")

		print (Fore.YELLOW+"N0T3 ~~$$", end="")
		fast_delay_print(" Copy Generated Random Password after the \"P@SSW0RD >>\" to your Clipboard for future use... You can also specify the \"-o\" argument to the script to save generated password in a file for future purposes. STAY SAFE... your friendly developer CyberPatriX-S3C\n")
		sys.exit(0)
