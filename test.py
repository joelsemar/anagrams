import random
from anagram import is_anagram
import unittest


class AnagramTest(unittest.TestCase):

    def test_is_anagram(self):
        self.assertTrue(is_anagram("silent", "listen"))
        self.assertTrue(is_anagram("William Shakespeare", "I am a weakish speller"))
        self.assertTrue(is_anagram("rob", "orb"))
        self.assertFalse(is_anagram("Joel Semar", random_string(12)))
        self.assertFalse(is_anagram("fantastic", random_string(12)))
        self.assertTrue(is_anagram("Nessiteras rhombopteryx", "Monster hoax by Sir Peter S"))
        self.assertTrue(is_anagram("RocKetBoys", "oct o ber sky"))

    def test_whitespace(self):
        self.assertTrue(is_anagram("rob", "o r b"))
        # make sure spaces don't fool us into thinking a word can be an anagram of itself
        self.assertFalse(is_anagram("rob", "r o b"))

    def test_punctuation(self):
        self.assertTrue(is_anagram("silent", "listen!"))
        # make sure punctuation doesn't fool us into thinking a word can be an anagram of itself
        self.assertFalse(is_anagram("silent", "s.i.l.e.n.t"))


    def test_random_shuffle(self):
        base_words = [random_string(12) for _ in range(1000)]

        for word in base_words:
            anagram = create_anagram(word)
            self.assertTrue(is_anagram(word, anagram))
            self.assertFalse(is_anagram(word, random_string(12)))


def random_string(size):
    alpha =  "abcdefghijklmnopqrstuvwxyz"
    return "".join([random.choice(alpha) for i in range(size)])


def create_anagram(text):
    """
    Not a real anagram (does not create valid words)
    Just random shuffle with random number of spaces and punctuation added
    """
    anagram = list(text)
    random.shuffle(anagram)

    punctuation = '".:;!?^%$#@!()*'
    #insert random spaces
    for i in range(random.randint(0, len(anagram)/2)):
        index = random.randint(0, len(anagram))
        anagram.insert(index, " ")

    #insert random punctuation
    for i in range(random.randint(0, len(anagram)/2)):
        index = random.randint(0, len(anagram))
        anagram.insert(index, random.choice(punctuation))

    return "".join(anagram)


if __name__ == "__main__":
    unittest.main()
