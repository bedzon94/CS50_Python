from fuel import convert, gauge
import pytest


def main():
    test_convert()
    test_gauge()



def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")



def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"






if __name__ == "__main__":
    main()
