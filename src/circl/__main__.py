import sys

from .interpreter import decode, execute


def main():
    if len(sys.argv) == 1:
        print("Put in circle string:")
        execute(decode(input()))
    else:
        execute(decode(sys.argv[1]))


if __name__ == "__main__":
    main()
