import re
import urllib.request
import json,socket
from termcolor import *

api_endpoint = 'https://ipinfo.io/'


def page_exists(page):
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False

def iplookup():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("your ip address is: {}".format(ip_address))


def specified_IP():
    user_ip = input("Enter specific IP address: ")
    #Regular expression for IPv4
    regexp = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    if not regexp.search(user_ip):
        print("Invalid input {}".format(user_ip))
        exit()
    if (page_exists(api_endpoint+user_ip)):
        page = urllib.request.urlopen(api_endpoint+user_ip)
        content = page.read().decode("utf-8")  # keep in mind the byte string needs to be decoded
        data = json.loads(content)
        if not data:
            return "place not found"
        country = (data['country'])
        city = (data['city'])
        postal = (data['postal'])
        state = (data['region'])
        if not postal:
            return "postal not found"
    else:
        print("ERROR:invalid API endpoint")
        return "place not found"
    print("IP address: {} , Postal code: {}, City: {}, state: {}, Country: {}".format(user_ip, postal, state, city, country))

# takes a user_input string as a parameter
# returns location string

def info_myIP():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    page = urllib.request.urlopen(api_endpoint)
    content = page.read().decode("utf-8")  # keep in mind the byte string needs to be decoded
    data = json.loads(content)
    country = (data['country'])
    city = (data['city'])
    postal = (data['postal'])
    state = (data['region'])
    print("IP address: {} , Postal code: {}, City: {}, state: {}, Country: {}".format(ip_address, postal, state, city, country))


def main():
    while (True):
        cprint("\n1 - lookup my IP address", 'blue')
        cprint("2 - lookup info about specified IP", 'blue')
        cprint("3 - lookup info for my IP address", 'blue')
        cprint("[q] Enter q to quit.", 'blue')

        choice = int(input("\nWhat would you like to do? "))
        if choice == 1:
            iplookup()

        elif choice == 2:
            specified_IP()
        elif choice == 3:
            info_myIP()

        elif choice == 'q':
            print("Exiting")
            break

if __name__ == '__main__':
    main()