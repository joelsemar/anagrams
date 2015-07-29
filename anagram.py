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

    word_input = clean(word_input)
    for word in file_input.readlines():
        if is_anagram(word_input, word):
            found.append(word.strip())

    found = set(found)
    time_taken = time.time() - start
    print "found %s anagrams in %s seconds" % (len(found), time_taken)
    print ", ".join(found)
    return found


def fast_find_anagrams(word_input, file_input):
    """
    Find all unique anagrams to the word_input argument in the given file
    """

    print "Finding anagrams for the word '%s' in file '%s'" % (word_input, file_input.name)
    found = []
    start = time.time()

    sorted_word_input = sorted(clean(word_input))

    for word in file_input.readlines():
        if sorted(clean(word)) == sorted_word_input:
            found.append(word.strip())

    found = set(found)
    time_taken = time.time() - start
    print "found %s anagrams in %s seconds" % (len(found), time_taken)
    print ", ".join(found)
    return found


def clean_source(decorated_func):

    @wraps(decorated_func)
    def returned_func(*args):
        args = list(args)
        source = args[0]
        if not hasattr(decorated_func, 'last_source') or decorated_func.last_source != source:
            decorated_func.last_source = source
            decorated_func.last_source_clean = clean(source)
        args[0] = decorated_func.last_source_clean
        return decorated_func(*args)
    return returned_func


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
        fast_find_anagrams(word_input, file_input)

