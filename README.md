# Python-Hash-Cracker
Extremely Fast Python Hash Cracker! This script can try 300,000 words a second.
It supportes several hash formats with options like a `numbers bruteforce` and `verbose mode`.

![Alt text](img2.JPG?raw=true "Screenshot")

Command line is fairly straight forword, here are the options:

`-h` [hash]

`-t` [type]

`-w` [wordlist]

`-n` [numbers bruteforce, used in place of -w]

`-v` [verbose, slows down cracking time though :( ]

`-i` [help and info]

# Examples:
Hashcrack help:

`./Hash-Cracker.py -i`

Hashcrack with a wordlist and verbose mode:

`./Hash-Cracker.py -h 7406e17d2e30b05b7220a800fad53a22 -t md5 -w Wordlist.txt -v`

Numbers bruteforce fast:

`./Hash-Cracker.py -h 7406e17d2e30b05b7220a800fad53a22 -t md5 -n`

# Platforms
The command line tool has been tested on and works with iOS, Windows[7/8/10], Unix, and OS X.

# Enjoy
