from twttr import shorten

def main():
    test_twttr()



def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("HELLO") == "HLL"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("CS50") == "CS50"
    assert shorten("50") == "50"





if __name__ == "__main__":
    main()
