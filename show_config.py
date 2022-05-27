import subprocess
import os
import pty
from textwrap import fill 
import time
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import *
from tksheet import Sheet
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

rules = []

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Rule : 
    def __init__(self, type, protocol, source, sport, destination, dport, gateway, description) :
        self.type = type
        self.protocol = protocol
        self.source = source
        self.sport = sport
        self.destination = destination
        self.dport = dport
        self.gateway = gateway
        self.description = description

def AddRule():
    print("\nSelect The Type")
    print("P = Pass")
    print("D = Deny")
    rtype = input("Type (P/D)  >> ")
    if rtype == "p" or rtype == "P":
        rtype = "pass"
    elif rtype == "d" or rtype == "D":
        rtype = "deny"
    else:
        print("\n!! Please enter P or D ::")
        AddRule()
    protocol = input("Protocol    >> ")
    source = input("Source      >> ")
    sport = input("Source Port >> ")
    destination = input("Destination >> ")
    dport = input("Destination Port >> ")
    gateway = input("Gateway          >> ")
    description = input("Description      >> ")

    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------- New Rule -----------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" | No. ", "|  Type ", "|  Protocol ", "|      Source      ", "|  Port  ", "| Destination      ", "|  Port  ", "|      Gateway     ", "|    Description")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print(' |(', '1', ')\t| ', rtype, ' | ', filBlanks(protocol,8), ' | ', filBlanks(source,15), ' | ',  filBlanks(sport,5), ' | ', filBlanks(destination,15), ' | ', filBlanks(dport,5), ' | ', filBlanks(gateway,15), ' | ', description)
    print("------------------------------------------------------------------------------------------------------------------------------------------------")

    rule = Rule(rtype, protocol, source, sport, destination, dport, gateway, description)
    rules.append(rule)
    GetUserAction()


def DeleteRule():
    userInput = input("Enter The NUmber of the Rule >> ")
    if int(userInput) <= len(rules):
        del rules[int(userInput)-1]
        print("Successfully Deleted")
        GetUserAction()
    else:
        print("Please enter a valid Rule Number")
        GetUserAction()

def ContinueToImport():
    print("Generating the XML File")
    filterRoot = "<filter>\n"
    ruleString = "\t<rule>"
    ruleString += "\t</rule>"
    filterRoot += ruleString + "</filter>"
    
    print(filterRoot);
    
    GetUserAction()

def SaveConfiguration():
    print("yada")
    GetUserAction()

def GetUserAction():
    print("Select your next action")
    print("(1) Show Existing Rules")
    print("(2) Add rule")
    print("(3) Delete rule")
    print("(4) Continue to import")
    print("(5) Save Configurations")
    print("(6) Exit")
    print("::::::::::::::::::::::::::::::::::::::")
    userAction = input("Action (Enter The Number) >> ")

    if userAction == "1":
        showrules(rules)
    elif userAction == "2":
        AddRule()
    elif userAction == "3":
        DeleteRule()
    elif userAction == "4":
        ContinueToImport()
    elif userAction == "5":
        SaveConfiguration()
    elif userAction == "6":
        return
    else:
        print ("Please Enter a Valid Number")
        GetUserAction()

print("Have A Nice Day!")

class showrules(tk.Tk) : 
   
    def __init__(self, data) :
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------- Existing Rules ---------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
    
        temp_rules = []
        counter = 1
        print(" | No. ", "|  Type ", "|  Protocol ", "|      Source      ", "|  Port  ", "| Destination      ", "|  Port  ", "|      Gateway     ", "|    Description")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        for r in data:
            
            rule = [str(r.type), str(r.protocol), str(r.source), str(r.sport), str(r.destination), str(r.dport), 
               str(r.gateway), str(r.description)]
            temp_rules.append(rule)
            rtype = r.type
            protocol = filBlanks(r.protocol, 8)
            source = filBlanks(r.source, 15)
            sport = filBlanks(r.sport, 5)
            destination = filBlanks(r.destination, 15)
            dport = filBlanks(r.dport, 5)
            gateway = filBlanks(r.gateway, 15)
            description = r.description
            
            print(' |(', counter, ')\t| ', rtype, ' | ', protocol, ' | ', source, ' | ',  sport, ' | ', destination, ' | ', dport, ' | ', gateway, ' | ', description)
            counter+=1 
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        
        GetUserAction()


def filBlanks(val, m):
    inputVal = val
    if len(val) < m:
        for i in range(m-len(val)):
            inputVal = inputVal + ' '
    return inputVal



file_name = input("Enter the Firewall configuration file name : ")
configs = open(file_name)
config_string = configs.read()

filter_start_index = config_string.find("<filter>")
filter_end_index = config_string.find("</filter>")+ len ("</filter>")
rules_string = config_string[filter_start_index:filter_end_index]
##print(rules_string)
   
mytree = ET.fromstring(rules_string)
def printDetected(rule_array): 
    for r in rule_array:
        print("Rule", r.protocol, r.description)
  
def fill_text(text_to_be_checked):
    return text_to_be_checked

    
myroot = ET.fromstring(rules_string)
         

#printing myroot
for rule in myroot:
    #print("--------------------------------")
    new_rule = Rule("-", "-", "-", "-", "-", "-", "-", "-")
    for xml_tag in rule:
        tag = ""
        text = ""
        if xml_tag.tag is not None:
            tag = xml_tag.tag
            if xml_tag.text is not None:
                text = xml_tag.text
            if tag == "type":
                new_rule.type = fill_text(text)
            if "ipprotocol" in tag:
                new_rule.protocol = fill_text(text)
            if "source" in tag:
                for y in xml_tag:
                    #print(y)
                    if "address" in y.tag:
                        new_rule.source = fill_text(y.text)
                    if "port" in y.tag:
                        new_rule.sport = fill_text(y.text)
                    if "network":
                        new_rule.source = fill_text(y.text)
                    if "any" in y.tag:
                        new_rule.source = "any"
                        new_rule.sport = "any"
            if "destination" in tag:
                for y in xml_tag:
                    if "address" in y.tag:
                        new_rule.destination = fill_text(y.text)
                    if "port" in y.tag:
                        new_rule.dport = fill_text(y.text)
                    if "network":
                        new_rule.destination = fill_text(y.text)
                    if "any" in y.tag:
                        new_rule.destination = "any"
                        new_rule.dport = "any"
            if "gateway" in tag:
                new_rule.gateway = fill_text(text)
            if "descr" in tag:
                new_rule.description = fill(xml_tag.text)
        
    rules.append(new_rule)
    del new_rule

#printDetected(rules)

app = showrules(rules)
#app.mainloop()
