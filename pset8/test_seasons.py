from seasons import mins_lived
import pytest


def main():
    test_mins_lived()
    test_exception()


def test_mins_lived():
    assert mins_lived(1999, 1, 1) == "Thirteen million, thirty-six thousand, three hundred twenty minutes"
    assert mins_lived(1999, 12, 31) == "Twelve million, five hundred twelve thousand, one hundred sixty minutes"




def test_exception():
    assert mins_lived(1, 1, 1999) == "Invalid date"




if __name__ == "__main__":
    main()
