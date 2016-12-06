# Python-Hash-Cracker
Extremely Fast Python Hash Cracker with GUI!!! This tool can try 300,000 words a second!!! It comes in a command line version and a compiled executable windows gui!!!( This tool is faster than Cain www.Oxid.it)
It supportes several hash formats with options like a Numbers Bruteforce and verbose (command line).
#Usage
![Alt text](img2.JPG?raw=true "Screenshot")

Command line is fairly straight forword, here are the options:

-h [hash]

-t [type]

-w [wordlist]

-n [numbers bruteforce, used in place of -w]

-v [verbose, slows down cracking time though :( ]

-i [help and info]

#Examples:
Hashcrack help:

./Hash-Cracker.py -i

Hashcrack with a wordlist and verbose mode:

./Hash-Cracker.py -h 7406e17d2e30b05b7220a800fad53a22 -t md5 -w Wordlist.txt -v

Numbers bruteforce fast:

./Hash-Cracker.py -h 7406e17d2e30b05b7220a800fad53a22 -t md5 -n

#Platforms
The command line tool works on iOS, Windows[7/8/10], Unix, and OS X. Gui works on all but iOS.

#Enjoy
