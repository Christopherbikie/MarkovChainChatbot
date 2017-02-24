Markov Chain Chatbot
====================

To use:
1. Put a text file to use to generate the Markov Chain in `/texts` (or just use one that's already there)
2. Run `lexiconGenerator.py` and select that file.
3. Run `main.py` and select the file you want to use.
4. Once you've finished playing with it, type "quit" to exit.

Notes
------

- Don't expect it to work well. This was more of an experiment, not an attempt at the next Siri.
- At the top of `main.py` there is a variable called `chains` which by default is set to 20000. This can be increased for better responces at the cost of longer processing time. It also does not need to be as long for shorter Markov Chain inputs. 20000 takes about 2 seconds on my PC and seems about right for War and Peace, which is much longer than most other books (~500,000 words). 
