from scapy.all import sniff, TCP, IP 
import threading

capture_type = None
capture_count = None
total_packets = 0 


def packet_callback(packet):
    global total_packets 
    total_packets += 1
    if capture_type == 'TCP' and packet.haslayer(TCP):
        print("TCP Packet Summary:")
        print(packet.summary())
        print(f"Total Packets Captured: {total_packets}\n")
        packet.show()


def menu():
    global capture_type, capture_count
    while True:
        print("\n=== Packet Sniffer Menu ===")
        print("1. Capture TCP Packets")
        print("2. Capture UDP Packets")
        print("3. Exit")
        
        choice = input("Select the packet type to capture (1-3): ")

        if choice == '1':
            capture_type = 'TCP'
            capture_count = int(input("How many packets do you want to capture? "))
            break
        elif choice == '2':
            capture_type = 'UDP'
            capture_count = int(input("How many packets do you want to capture? "))
            break
        elif choice == '3':
            print("Exiting...")
            exit()
        else:
            print("Invalid choice. Please try again.")


def start_capture():
    interface = "Wi-Fi"
    print(f"Starting capture on {interface} for {capture_count} packets...")
    sniff(iface=interface, prn=packet_callback, count=capture_count)
    print("Capture complete. Returning to the menu...\n")
    menu()
    capture_thread = threading.Thread(target=start_capture)
    capture_thread.start()


menu()
capture_thread = threading.Thread(target=start_capture)
capture_thread.start()
