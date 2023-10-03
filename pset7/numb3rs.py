import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        return False
    ip_byte = ip.split(".")
    for byte in ip_byte:
        if int(byte) < 0 or int(byte) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
