import subprocess
from unittest import result
import os
import pty
import time
import show_config as sc

class FirewallMigrator:
    
    def pfsense(self):
        username = input("\nEnter username : ")
        hostname = input("\nEnter hostname / ip address of the firewall : ")
        backup = "backup"
        print ("\nYour selections are : \n",
        "\nUsername : "+username+
        "\nHostname/IP : "+hostname)
        confirm = input("\nConfirm your Selections : ")

        #retrieve the configuration file from the pfsense firewall
        result = subprocess.getoutput('ssh '+username+'@'+hostname+' cat /cf/conf/config.xml > '+backup+'.xml')


        print('\nConfiguration Recieved')

    def OPNsense(self):

        username = input("\nEnter username : ")
        hostname = input("\nEnter hostname / ip address of the firewall : ")
        backup = "backup"
        print ("\nYour selections are : \n",
        "\nUsername : "+username+
        "\nHostname/IP : "+hostname)
        confirm = input("\nConfirm your Selections : ")

        #retrieve the configuration file from the pfsense firewall
        result = subprocess.getoutput('ssh '+username+'@'+hostname+' cat /cf/config.xml > '+backup+'.xml')


        print('\nConfiguration Recieved')
        
    def StartScreen(self):
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
        " ||                                                      (version 1.1) ||\n",
        "--------------------------------------------------------------------------\n",
        "--------------------------------------------------------------------------\n\n",
        "Tecxick Co\n",
        "Private Projects\n",
        "___________________________________________________________________________")
        
    def StartMigration(self):
        print("The following program uses the method of SSH method to access the firewall and do the procedings.\n")

        print("\nSelect the firewall to extract rules from : ")

        print("\n",
        "____________________________________\n\n",
        "          1  -   pfSense\n",
        "          2  -   OPNsense\n",
        "____________________________________")


        firewall = input("Insert the correct number : ")

        if firewall == "1":
            self.pfsense()

        elif firewall == "2":
            self.OPNsense()
            
    def __init__(self):
            self.StartScreen()
            self.StartMigration()
            print("Opening to Show Config")
            sc.import_data(self)


if __name__ == "__main__":
    FirewallMigrator()