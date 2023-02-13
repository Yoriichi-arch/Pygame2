import sys


def main():
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(num1 + num2)
    except:
        print(0)


if __name__ == "__main__":
    main()
