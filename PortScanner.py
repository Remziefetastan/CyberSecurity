import socket

# Menu options
print("Select the action you want to perform:")
print("1 - Scan a single port")
print("2 - Scan a range of ports")
print("3 - Scan multiple ports")
print("4 - Scan all ports")

# Get a selection from the user
choice = int(input("Enter your choice (1/2/3/4): "))

# Get an IP adress from the user
ip = input("Enter the target IP address: ")

if choice == 1:
    # Scan a port
    port = int(input("Enter the port number to scan: "))
    ports = [port]
    
elif choice == 2:
    # Port range scan
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    ports = range(start_port, end_port + 1)
    
elif choice == 3:
    # Multiple port scan
    ports = map(int, input("Enter the port numbers separated by commas: ").split(','))
    
elif choice == 4:
    # All ports scan
    ports = range(0, 65536)
else:
    print("Invalid choice!")
    ports = []

# Open ports
open_ports = [port for port in ports if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((ip, port)) == 0]

# Print results
if open_ports:
    print(f"Open ports: {', '.join(map(str, open_ports))}")
else:
    print("No open ports found.")
