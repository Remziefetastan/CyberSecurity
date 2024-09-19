import subprocess

interface = input("Which network interface do you want to use? (Example: eth0, wlan0) ")

new_mac = input("Enter new MAC adress (Example: 00:11:22:33:44:55): ")

print("New MAC adress: ", new_mac)
subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
print("MAC address has been changed!")
