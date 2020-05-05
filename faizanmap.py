#!/usr/bin/env python

import subprocess
import os
import sys

red = '\033[91m'
blue = '\33[94m'
yellow = '\33[93m'
end = '\033[0m'

if len(sys.argv) < 2:
    os.system("cls || clear")
    sys.stdout.write(red+"""                                                                                                                                                                                             
                                                                                                                                                                                             
 #######                                  #     #                      
 #         ##   # ######   ##   #    #    ##   ##   ##   #####  #    # 
 #        #  #  #     #   #  #  ##   #    # # # #  #  #  #    # #   #  
 #####   #    # #    #   #    # # #  #    #  #  # #    # #    # ####   
 #       ###### #   #    ###### #  # #    #     # ###### #####  #  #   
 #       #    # #  #     #    # #   ##    #     # #    # #   #  #   #  
 #       #    # # ###### #    # #    #    #     # #    # #    # #    # 
                                                                                                                                                                  \n"""+end)
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
else:
    sys.exit("Usage: To Scan Any Address By Nmap.py")


def mainMenu():
    print("-"*70)
    print("\t\t\t NMAP SCANNER")
    print("-"*70)
    print()
    print("\t\t\t1 ======> Discover Host")
    print("\t\t\t2 ======> Discover Ports")
    print("\t\t\t3 ======> Discover OS")
    print("\t\t\t4 ======> Clear The Screen")
    print("\t\t\t5 ======> Quit Program")
    print()

    choice = int(input("Enter The Choice: "))
    if choice == 1:
        host_dis()
        mainMenu()
    elif choice == 2:
        port_dis()
        mainMenu()
    elif choice == 3:
        os_dis()
        mainMenu()
    elif choice == 4:
        clear()
        mainMenu()
    elif choice == 5:
        clear()
        quit_pr()
    else:
        print("Wrong Choice")






def host_dis():
    host = input("enter the host name: ")
    print("." *60)
    subprocess.check_call(['nmap', '-V', '-n', '-Pn', '-sn', '-sL', 'PE', 'PP', 'oN', 'host.txt',' host'])
    print("."*60)

def port_dis():
    port_range = input("enter the host name: ")
    print("." *60)
    subprocess.check_call(['nmap', '-P', '1-100', '-oN', 'port_range.txt', port_range])
    print("."*60)

def os_dis():
    os = input("enter the host name: ")
    print("." *60)
    subprocess.check_call(['nmap', '-n', '-F', '-A', '-Pn', '-O', '-sS', '-oN', 'Os.txt', os])
    print("."*60)

def clear():
    os.system('cls||clear')

def quit_pr():
    clear()
    quit()

if __name__ == "__main__":
    mainMenu()