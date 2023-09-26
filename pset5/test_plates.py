from plates import is_valid

def main():
    test_valid()
    test_valid2()
    test_valid3()
    test_valid4()


def test_valid():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True


def test_valid2():
    assert is_valid("cs") == True
    assert is_valid("50") == False


def test_valid3():
    assert is_valid("PI314") == True
    assert is_valid("PI3.14") == False


def test_valid4():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False









if __name__ == "__main__":
    main()