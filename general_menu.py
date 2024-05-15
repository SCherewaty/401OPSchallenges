#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/14/2024



def display_menu():
    menu = {
        '1': "Search via TCP.", 
        '2': "Search via ICMP.",
        'E': "Exit."
    }

    options = sorted(menu.keys())
    for entry in options:
        print(entry, menu[entry])
    
def main():
    while True:
        display_menu()
        selection = input("Please Select (1, 2, or E): ")
        if selection == '1':
            scan_port()
            # TCP 
        elif selection == '2':
            print("ICMP")
            # ICMP
        elif selection == 'E':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 1 for TCP, 2 for ICMP, or E to exit.")

if __name__ == "__main__":
    main()