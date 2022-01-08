import argparse, sys, time

parser = argparse.ArgumentParser(
    description="Stream one or more files with a delay between each line"
)
parser.add_argument("files", type=argparse.FileType("r"), nargs="*", default=["-"])
parser.add_argument("-d", "--delay-in-ms", type=int, default=100)


def main(args=None):
    parsed_args = parser.parse_args(args)
    delay_in_s = float(parsed_args.delay_in_ms) / 1000
    for file in parsed_args.files:
        if file == "-":
            file = sys.stdin
        for line in file:
            sys.stdout.write(line)
            sys.stdout.flush()
            time.sleep(delay_in_s)


if __name__ == "__main__":
    main()
