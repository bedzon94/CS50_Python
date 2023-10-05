import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    value = re.search(r"^.+src=\"https?://(www\.)?youtube\.com/embed/(.+)\".+$", s)
    if value:
        return (f"https://youtu.be/{value.group(2)}")
    else:
        return None




if __name__ == "__main__":
    main()
