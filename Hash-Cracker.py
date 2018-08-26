#!/usr/bin/python
import StringIO
import getopt
import hashlib
import sys
import os
import time

print "  "
print "Python Hash-Cracker"
print "Version 3.0-3 Stable"


def info():
    print " "
    print "Information:"
    print "[*] Options:"
    print "[*](-h) Hash"
    print "[*](-t) Type [See supported hashes]"
    print "[*](-w) Wordlist"
    print "[*](-n) Numbers bruteforce"
    print "[*](-v) Verbose [{WARNING}Slows cracking down!]\n"
    print "[*] Examples:"
    print "[>] ./Hash-Cracker.py -h <hash> -t md5 -w DICT.txt"
    print "[>] ./Hash-Cracker.py -h <hash> -t sha384 -n -v"
    print "[*] Supported Hashes:"
    print "[>] md5, sha1, sha224, sha256, sha384, sha512"
    print "[*] Thats all folks!\n"


def checkOS():
    if os.name == "nt":
        operatingSystem = "Windows"
    elif os.name == "posix":
        operatingSystem = "posix"
    else:
        operatingSystem = "Unknown"
    return operatingSystem


class hashCracking:

    def hashCrackWordlist(self, userHash, hashType, wordlist, verbose):
        start = time.time()
        self.lineCount = 0
        if (hashType == "md5"):
            h = hashlib.md5
        elif (hashType == "sha1"):
            h = hashlib.sha1
        elif (hashType == "sha224"):
            h = hashlib.sha224
        elif (hashType == "sha256"):
            h = hashlib.sha256
        elif (hashType == "sha384"):
            h = hashlib.sha384
        elif (hashType == "sha512"):
            h = hashlib.sha512
        else:
            print "[-]Is %s a supported hash type?" % hashType
            exit()
        with open(wordlist, "rU") as infile:
            for line in infile:
                line = line.strip()
                lineHash = h(line).hexdigest()
                if (verbose == True):
                    sys.stdout.write('\r' + str(line) + ' ' * 20)
                    sys.stdout.flush()

                if (str(lineHash) == str(userHash.lower())):

                    SavedHashes = open('SavedHashes.txt', 'a+')
                    SavedHashes.write('%s : {}'.format(lineHash) % line)
                    SavedHashes.write('\n')
                    SavedHashes.close()

                    end = time.time()
                    print "\n[+]Hash is: %s" % line
                    print "[*]Words tried: %s" % self.lineCount
                    print "[*]Time: %s seconds" % round((end - start), 2)
                    print "[*]Hash to SavedHashes.txt"
                    exit()
                else:
                    self.lineCount = self.lineCount + 1
        end = time.time()
        print "\n[-]Cracking Failed"
        print "[*]Reached end of wordlist"
        print "[*]Words tried: %s" % self.lineCount
        print "[*]Time: %s seconds" % round((end - start), 2)
        exit()

    def hashCrackNumberBruteforce(self, userHash, hashType, verbose):
        start = time.time()
        self.lineCount = 0
        if (hashType == "md5"):
            h = hashlib.md5
        elif (hashType == "sha1"):
            h = hashlib.sha1
        elif (hashType == "sha224"):
            h = hashlib.sha224
        elif (hashType == "sha256"):
            h = hashlib.sha256
        elif (hashType == "sha384"):
            h = hashlib.sha384
        elif (hashType == "sha512"):
            h = hashlib.sha512
        else:
            print "[-]Is %s a supported hash type?" % hashType
            exit()
        while True:
            line = "%s" % self.lineCount
            line.strip()
            numberHash = h(line).hexdigest().strip()
            if (verbose == True):
                sys.stdout.write('\r' + str(line) + ' ' * 20)
                sys.stdout.flush()
            if (numberHash.strip() == userHash.strip().lower()):
                end = time.time()
                print "\n[+]Hash is: %s" % lineCount
                print "[*]Time: %s seconds" % round((end - start), 2)
                break
            else:
                self.lineCount = self.lineCount + 1

def main(argv):
    hashType = userHash = wordlist = verbose = numbersBruteforce = None
    print "[Running on %s]\n" % checkOS()
    try:
        opts, args = getopt.getopt(argv, "ih:t:w:nv", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
        print '[*]Type ./Hash-Cracker.py -i for information'
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-i':
            info()
            sys.exit()
        elif opt in ("-t", "--type"):
            hashType = arg
        elif opt in ("-h", "--hash"):
            userHash = arg
        elif opt in ("-w", "--wordlist"):
            wordlist = arg
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-n", "--numbers"):
            numbersBruteforce = True
    if not (hashType and userHash):
        print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
        sys.exit()

    # looks through saved hash file instead of hashing all WordList entries
    try:
        File = open('SavedHashes.txt', 'r')
        File.close()
    except:
        File = open('SavedHashes.txt', 'w')
        File.close()

    with open('SavedHashes.txt', 'rU') as SavedHashFile:
        for HASH in SavedHashFile:
            HASH = HASH.strip().split(" : ")
            try:
                if userHash.lower() == HASH[1]:
                    print "[*]Saved Hash is: %s" % HASH[0]
                    sys.exit()
            except IndexError:
                continue
        else:
            print "[*]Hash: %s" % userHash
            print "[*]Hash type: %s" % hashType
            print "[*]Wordlist: %s" % wordlist
            print "[+]Cracking..."
            try:
                h = hashCracking()
                if (numbersBruteforce == True):
                    h.hashCrackNumberBruteforce(userHash, hashType, verbose)
                else:
                    h.hashCrackWordlist(userHash, hashType, wordlist, verbose)

            except IndexError:
                print "\n[-]Hash not cracked:"
                print "[*]Reached end of wordlist"
                print "[*]Try another wordlist"
                print "[*]Words tried: %s" % h.lineCount

            except KeyboardInterrupt:
                print "\n[Exiting...]"
                print "Words tried: %s" % h.lineCount

            except IOError:
                print "\n[-]Couldn't find wordlist"
                print "[*]Is this right?"
                print "[>]%s" % wordlist

if __name__ == "__main__":
    main(sys.argv[1:])
