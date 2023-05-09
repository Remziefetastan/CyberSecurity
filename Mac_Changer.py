import subprocess

# İşletim sistemindeki ağ arabirimini almak için sistem komutunu kullanın
interface = input("Hangi ağ arabirimini kullanmak istersiniz? (Örneğin: eth0, wlan0) ")

# Yeni MAC adresini al
new_mac = input("Yeni MAC adresini girin (Örneğin: 00:11:22:33:44:55): ")

# Yeni MAC adresini değiştirin
print("Yeni MAC adresi: ", new_mac)
subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
print("MAC adresi değiştirildi!")
