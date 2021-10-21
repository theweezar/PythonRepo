import pyshark
import csv
import os

def show_interface():
    print("Current Interface.")
    os.system("netsh interface show interface")

def main():
    show_interface()
    interface = input('Select interface: ')
    try: 
        capture = pyshark.LiveCapture(
            interface=interface,
            output_file="output.pcap"
        )
        capture.sniff(timeout=20)
        pyshark.capture.capture.StopCapture()
    except:
        print("Error")

if __name__ == "__main__":
    main()