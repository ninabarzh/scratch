"""Example using walk
Authors: Reinica and Nina"""
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument("-p", "--path", help="directory to start from", type=dir_path, default='.')
    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


def traverse(path):
    filesystem_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(path, file)
            filesystem_list.append(path)
        for directory in dirs:
            path = os.path.join(path, directory)
            filesystem_list.append(path)

    print(*filesystem_list, sep="\n")
    return filesystem_list


def main():
    parsed_args = parse_arguments()

    if parsed_args.path:
        traverse(parsed_args.path)


# Execute
if __name__ == '__main__':
    main()
