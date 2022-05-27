import os
from re import L
from unittest import result
from click import command, confirm


import subprocess

def pfsense():

    username = input("Enter the username : ")
    hostname = input("Enter the hostname(LAN IP address) : ")
    file_name = input("Enter file to be imported (without the extensions): ")

    confirm = input("Insert 'y' to confirm your details or 'n to change : ")

    if confirm == "Y" or "y":
        result = subprocess.getoutput("scp "+file_name+".xml "+username+"@"+hostname+":/cf/conf/config.xml")
        result = subprocess.getoutput("ssh "+username+"@"+hostname+" rm /cf/conf/bak")


    elif confirm == "N" or "n":
        pfsense()


def OPNsense():

    username = input("Enter the username : ")
    hostname = input("Enter the hostname (LAN IP address) of firewall: ")
    file_name = input("Enter file to be imported (without extensions): ")

    confirm = input("Input 'y' to confirm your details or 'n' to change: ")

    if confirm == "Y" or "y":
        result = subprocess.getoutput("scp "+file_name+".xml "+username+"@"+hostname+":/cf/config.xml")
        result = subprocess.getoutput("ssh "+username+"@"+hostname+" rm /cf/conf/bak")


    elif confirm == "N" or "n":
        OPNsense()


print("Select the firewall to import the configurations to: ")
print("\n",
"____________________________________\n\n",
"          1  -   pfSense\n",
"          2  -   OPNsense\n",
"____________________________________")


firewall = input("Insert the correct number : ")

if firewall == 1:
    pfsense()

elif firewall == 2:
    OPNsense()


