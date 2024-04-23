# NYT Cheat Kit

This set of code is a silly way of searching the web for the answers.

It's somewhat an exercise in web scraping but also a response to some people 
saying the [../word_search/word_search.py](word search tool) is cheating even 
though the intended use there is educational, it's absolutely possible that it 
can be used to cheat. So, if someone is inclined to use it to cheat, they can 
just use this cheat kit.

## Connections

Straight up looks for the answers from https://word.tips/todays-nyt-connections-answers/.
Provides them in difficulty order from lowest to highest.

## Wordle

Looks up the answer from https://www.tomsguide.com/news/what-is-todays-wordle-answer.
Tom's Guide is nice enough to give a hint before giving the answer so you're able to 
just get a hint if you don't quite want to cheat.

## Spelling Bee

Modified version of [../word_search/word_search.py](word search tool) that will apply 
the rules of spelling bee: minimum 4 letters, must have the center letter and can only 
be from the set of 7 letters provided. The cheat tool gives you the pangram (I think 
it's supposed to be the highest scoring word) and the option to get the rest of a list 
of words that meet the criteria in order of longest to shortest (presumably highest to 
lowest score). The non-common, non-proper and non-curse word rules aren't applied. 
That's an exercise left to the user. (I also didn't want to use another tool to get the 
frequency of words to determine non-common.)

## Mini

Straight up looks for the answers from https://word.tips/todays-nyt-mini-crossword-clues-answers/. Will provide the answers in order, grouped by 
ACROSS and DOWN.
