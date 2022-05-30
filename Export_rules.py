import subprocess
from unittest import result
import os
import pty
import time

print("\n",
"--------------------------------------------------------------------------\n",
"--------------------------------------------------------------------------\n",
" ||  ███████╗██╗██████╗░███████╗░██╗░░░░░░░██╗░█████╗░██╗░░░░░██╗░░░░░ ||\n",
" ||  ██╔════╝██║██╔══██╗██╔════╝░██║░░██╗░░██║██╔══██╗██║░░░░░██║░░░░░ ||\n",
" ||  █████╗░░██║██████╔╝█████╗░░░╚██╗████╗██╔╝███████║██║░░░░░██║░░░░░ ||\n",
" ||  ██╔══╝░░██║██╔══██╗██╔══╝░░░░████╔═████║░██╔══██║██║░░░░░██║░░░░░ ||\n",
" ||  ██║░░░░░██║██║░░██║███████╗░░╚██╔╝░╚██╔╝░██║░░██║███████╗███████╗ ||\n",
" ||  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚══════╝ ||\n",
" ||                                                                    ||\n",
" ||  ███╗░░░███╗██╗░██████╗░██████╗░░█████╗░████████╗░█████╗░██████╗░  ||\n",
" ||  ████╗░████║██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ||\n",
" ||  ██╔████╔██║██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝  ||\n",
" ||  ██║╚██╔╝██║██║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗  ||\n",
" ||  ██║░╚═╝░██║██║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ||\n",
" ||  ╚═╝░░░░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ||\n",
" ||                                                      (version 1.0) ||\n",
"--------------------------------------------------------------------------\n",
"--------------------------------------------------------------------------\n\n",
"Name : K H M Dalpatadu\n",
"Index No : 10707070\n",
"Module Code : PRCO303SL\n",
"Module Name : Computing Project\n",
"___________________________________________________________________________")

print("The following program uses the method of SSH method to access the firewall and do the procedings.\n")

print("\nSelect the firewall to extrct rules from : ")

print("\n",
"____________________________________\n\n",
"          1  -   pfSense\n",
"          2  -   OPNsense\n",
"____________________________________")


firewall = input("Insert the correct number : ")

def pfsense():

    username = input("\nEnter username : ")
    hostname = input("\nEnter hostname / ip address of the firewall : ")
    backup = input("\nEnter name of backup file to export to (without extensions): ")
    print ("\nYour selections are : \n",
    "\nUsername : "+username+
    "\nHostname/IP : "+hostname)
    confirm = input("\nConfirm your Selections : ")

    #retrieve the configuration file from the pfsense firewall
    result = subprocess.getoutput('ssh '+username+'@'+hostname+' cat /cf/conf/config.xml > '+backup+'.xml')


    print('\nConfiguration Recieved')

def OPNsense():

    username = input("\nEnter username : ")
    hostname = input("\nEnter hostname / ip address of the firewall : ")
    backup = input("\nEnter name of backup file to export to (without extensions): ")
    print ("\nYour selections are : \n",
    "\nUsername : "+username+
    "\nHostname/IP : "+hostname)
    confirm = input("\nConfirm your Selections : ")

    #retrieve the configuration file from the pfsense firewall
    result = subprocess.getoutput('ssh '+username+'@'+hostname+' cat /cf/config.xml > '+backup+'.xml')


    print('\nConfiguration Recieved')

if firewall == "1":
    pfsense()

elif firewall == "2":
    OPNsense()

