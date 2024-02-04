#shebang to tell the OS shell where to find the interpreter for the file.
#!/usr/bin/env python3

#Install the required software on linux OS:
#  sudo apt install python3-pip
#  pip install python-nmap

# Import nmap
import nmap
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern to extract the number of ports to scan. Syntax for user input: (ex 10-100).
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Variable for Minimum and Maximum port.
port_min = 0
port_max = 65535

open_ports = []
# Input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    # You can scan 0-65535 ports. Scanning all the ports is not advised because it will take a VERY long time.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
# For loop through all the ports in the specified range.
for port in range(port_min, port_max + 1):
    try:
        #Scan the IP entered and the port that the for loop is on.
        result = nm.scan(ip_add_entered, str(port))
        # If you want to see the full result dictionary for that port uncomment the next line.
        #print(result)
        # Extract the specific value I want from the dictionary which is the port status. Which will be filtered or open.
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        if port_status == 'open':
            print(f"Port {port} is {port_status}")

    except:
        # If the port can't be scanned then it returns this string so the program won't crash.
        print(f"Cannot scan port {port}.")
