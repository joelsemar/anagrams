small piece of code to locate unique anagrams of a given word in a text file

you can run the example by ./run.sh
(you may need chmod +x run.sh)

Example output:
```
jsemar@HA002425 ~/anagrams (master) ▸ ./run.sh
Finding anagrams for the word 'empires' in file 'words'
found 5 words in 2.57160806656 seconds
spireme, emprise, epimers, imprese, premise
```

To run tests:
`python test.py`


It's the job of any decent developer to ask questions before jumping in to code. There are a number
that are unanswered for this.

1. The example file is given one word per line. Is this the only input format to be handled?
2. From wikipedia "An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase"
However the specs define it as such "(just a reminder: an anagram is the result of rearranging the letters of a word to form a new word"
This would restrict mulit-word candidate anagrams.
3. The input is given to be "empires" should be be able to support arbitrary inputs?
4. Does intermediate punctuation invalidate an anagram?
5. Are all input words valid words? (mpriese is not an anagram (afaik because it's not a valid word
6. How should the program be called? Command line? Imported and called?  and as such how should the data be returned?

I've gone ahead and created this program assuming:

1. Yes
2. wikipedia definition, however the inputs will restrict candidate return values
3. Yes
4. No
5. All inputs are valid words
6. Command line arguments, print resutls to stdout

