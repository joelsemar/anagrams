import random
from anagram import is_anagram

def test_is_anagram():
    assert is_anagram("silent", "listen")
    assert is_anagram("William Shakespeare", "I am a weakish speller")
    assert is_anagram("rob", "orb")
    assert not is_anagram("Joel Semar", random_string(12))
    assert not is_anagram("fantastic", random_string(12))
    print "is_anagram seems to work"


def random_string(size):
    alpha =  "abcdefghijklmnopqrstuvwxyz"
    return "".join([random.choice(alpha) for i in range(size)])


if __name__ == "__main__":
    test_is_anagram()
