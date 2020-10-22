"""A simple port scanner using socket requiring a hostname as argument
Authors: Reinica and Nina
Struggled with: https://bugs.python.org/issue32958
Port scanning is like going to someone’s house and checking their doors and windows.
If not by request of owners, use port scanners like this only on localhost or own website."""
from socket import *
import time
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument("-p", "--host", help="directory to start from", type=str, default='localhost')
    return parser.parse_args()


def is_valid_hostname(hostname):
    # A valid DNS name:
    #   has a maximum length of 253 characters
    #   consists only of allowed characters
    #   doesn't begin or end with a hyphen

    if hostname.endswith('.'):                                      # A single trailing dot is legal
        hostname = hostname[:-1]                                    # Strip a dot from the right
    if len(hostname) < 1 or len(hostname) > 253:
        raise argparse.ArgumentTypeError(f"{hostname} is not a valid hostname")
    disallowed = re.compile("[^A-Z\\d-]", re.IGNORECASE)
    return all(                                                     # Split by label and verify
        (label and len(label) <= 63                                 # length is within proper range
         and not label.startswith("-") and not label.endswith("-")  # no bordering hyphens
         and not disallowed.search(label))                          # contains only legal characters
        for label in hostname.split("."))


def scan(host):
    tip = gethostbyname(host)
    print('Starting scan on host: ', tip)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        connect = s.connect_ex((tip, i))
        if connect == 0:
            print('Port %d: OPEN' % (i,))
        s.close()


def main():
    parsed_args = parse_arguments()

    if parsed_args.host:
        starttime = time.time()
        scan(parsed_args.host)
        print('Time taken:', time.time() - starttime)


# Execute
if __name__ == '__main__':
    main()
