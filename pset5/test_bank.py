from bank import value

def main():
    test_value()
    test_value2()
    test_value3()


def test_value():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("   hello   ") == 0



def test_value2():
    assert value("HAWK?") == 20
    assert value("hey") == 20
    assert value("   hi   ") == 20


def test_value3():
    assert value("What's happening") == 100
    assert value("What's up") == 100
    assert value("   cs50   ") == 100






if __name__ == "__main__":
    main()

