#!/usr/bin/env python

import subprocess
import time

success = 0

def handle_error(msg):
    print("Error! " + msg)
    exit(1)


def user_agreement():
    print("this is a program that will enable you to successfully run the realtek rtl88xxAU family network adapters.")
    print("If you have read the README file and you wish to proceed, acknowledge with Y-yes or  N-no")
    user_input = raw_input(" Your response: ")

    return user_input.lower()


def upgrade_update_packages(response):
    flag = 0

    #UPDATING PACKAGES
    print("\n\t########Updating Your Packages########")

    if response.lower() == 'y':
        subprocess.call(["sudo", "apt", "update"])
        flag = 1


    #UPGRADING PACKAGES
    print("\n\t########Upgrading Your Packages########")

    time.sleep(12)  #pauses for 12 seconds the updates the machine

    if flag > 0:
        subprocess.call(["sudo", "apt", "upgrade"])
        success = 1
    else:
        handle_error("Unable To perform the upgrade command.\n Ensure you are connected to the internet and try again.")
        return 0


def realtek():

    # UPGRADING PACKAGES
    print("\n\t########Installing the DKMS Package########")

    time.sleep(12)
    subprocess.call(["sudo", "apt", "install", "dkms"])

    print("\n\t########Please Wait for 40 minutes########")

    time.sleep(6)

    subprocess.call(["sudo", "apt", "install", "realtek88xxau-dkms"])


user_response = user_agreement()
upgrade_update_packages(user_response)



realtek()
print("**************Success!!!**************")
