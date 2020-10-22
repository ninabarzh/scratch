"""A simple port scanner using socket requiring a hostname as argument
Authors: Reinica and Nina
Struggled with: https://bugs.python.org/issue32958
Port scanning is like going to someone’s house and checking their doors and windows.
If not by request of owners, use port scanners like this only on localhost or own website."""
import socket
import time
import argparse
import re


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument("-p", "--host", help="host to be scanned",
                        type=is_valid_hostname, default='localhost')
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

    # Split by label and verify
    #   length is within proper range
    #   does not contain bordering hyphens
    #   does not contain disallowed characters

    disallowed = re.compile("[^A-Z\\d-]", re.IGNORECASE)
    for label in hostname.split("."):
        if (len(label) > 63) or (label.startswith("-")) or (label.endswith("-")) or (disallowed.search(label)):
            raise argparse.ArgumentTypeError(f"{hostname} is not a valid hostname")


def scan(host):
    tip = socket.gethostbyname(host)
    print('Starting scan on host: ', tip)

    for i in range(50, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
