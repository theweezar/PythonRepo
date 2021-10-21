import pyshark
import csv
import os
import sys

def main():
    pcap_file = sys.argv[1]
    csv_file = sys.argv[-1]
    os.system ('tshark -r '+ pcap_file +' > '+ csv_file +'.csv') 

if __name__ == "__main__":
    main()