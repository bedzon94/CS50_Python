from numb3rs import validate


def main():
    test_validate()


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("275.3.6.28") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("64.128.256.512") == False
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1.2.3.1000") == False
    assert validate("8.8.8") == False




if __name__ == "__main__":
    main()
