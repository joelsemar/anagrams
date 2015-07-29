import re
import sys
import time
from functools import wraps

def find_anagrams(word_input, file_input):
    """
    Find all unique anagrams to the word_input argument in the given file
    """

    print "Finding anagrams for the word '%s' in file '%s'" % (word_input, file_input.name)
    found = []
    start = time.time()

    for word in file_input.readlines():
        if is_anagram(word_input, word):
            found.append(word.strip())

    found = set(found)
    time_taken = time.time() - start
    print "found %s anagrams in %s seconds" % (len(found), time_taken)
    print ", ".join(found)
    return found


def is_anagram(source, candidate):
    """
    Tests if two given words are anagrams of one another
    """

    # make sure we are comparing two strings here
    # TODO: find out of 'silent' is an anagram of ['l','i','s','t','e','n']
    if not isinstance(candidate, str):
        return False

    if not isinstance(source, str):
        return False

    candidate = clean(candidate)
    source = clean(source)

    if len(source) != len(candidate):
        return False

    # assuming a word cannot be an anagram of itself
    if source == candidate:
        return False

    return sorted(source) == sorted(candidate)


def clean(text):
    """
    Strip any whitespace or punctuation, as well as lower case text
    """
    text = text.lower()
    return re.sub("[^a-z]", "", text)



if __name__ == "__main__":
    word_input, filename_input = sys.argv[1], sys.argv[2]

    with open(filename_input, "r") as file_input:
        find_anagrams(word_input, file_input)

