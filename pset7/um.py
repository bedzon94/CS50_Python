import re


def main():
    print(count(input("Text: ")))


def count(s):
    find = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(find)


if __name__ == "__main__":
    main()
