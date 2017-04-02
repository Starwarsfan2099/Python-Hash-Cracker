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
more = "config/add.txt"

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

def check_os():
    if os.name == "nt":
        operating_system = "Windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

def file_len(fname, verbose):
    try:
      with open(fname, "rU") as f:
          for i, l in enumerate(f):
            if (verbose == "yes"):
              line = "[*]Loaded %s lines..." % i
              sys.stdout.write('\r' + str(line) + ' ' * 20)
              sys.stdout.flush()
            pass
    except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
        exit()
    return i + 1

def format_wordlist(wordlist):
  return wordlist

class hash:
  def hashcrack(self, hash, type):
    start = time.time()
    self.num = 0
    if (type == "md5"):
       h = hashlib.md5
    elif (type == "sha1"):
       h = hashlib.sha1
    elif (type == "sha224"):
       h = hashlib.sha224
    elif (type == "sha256"):
       h = hashlib.sha256
    elif (type == "sha384"):
       h = hashlib.sha384
    elif (type == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % type
       exit()
    with open(wordlist, "rU") as infile:
      for line in infile:
        line = line.strip()
        hash2 = h(line).hexdigest()
        if (ver == "yes"):
            sys.stdout.write('\r' + str(line) + ' ' * 20)
            sys.stdout.flush()
        if (hash2 == hash.lower()):
            end = time.time()
            print "\n[+]Hash is: %s" % line
            print "[*]Words tried: %s" % self.num
            print "[*]Time: %s seconds" % round((end-start), 2)
            exit()
        else:
            self.num = self.num + 1
    end = time.time()
    print "\n[-]Cracking Failed"
    print "[*]Reached end of wordlist"
    print "[*]Words tried: %s" % self.num
    print "[*]Time: %s seconds" % round((end-start), 2)
    exit()

  def hashcracknum(self, hash, type):
    start = time.time()
    self.num = 0
    if (type == "md5"):
       h = hashlib.md5
    elif (type == "sha1"):
       h = hashlib.sha1
    elif (type == "sha224"):
       h = hashlib.sha224
    elif (type == "sha256"):
       h = hashlib.sha256
    elif (type == "sha384"):
       h = hashlib.sha384
    elif (type == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Is %s a supported hash type?" % type
       exit()
    while True:
       line = "%s" % self.num
       line.strip()
       hash2 = h(line).hexdigest().strip()
       if (ver == "yes"):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (hash2.strip() == hash.strip().lower()):
           end = time.time()
           print "\n[+]Hash is: %s" % line
           print "[*]Time: %s seconds" % round((end-start), 2)
           break
       else:
         self.num = self.num + 1

def main(argv):
  what = check_os()
  print "[Running on %s]\n" % what
  global hash1, type, wordlist, line, ver, numbrute
  hash1 = None
  type = None
  wordlist = None
  line = None
  ver = None
  numbrute = None
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      print '[*]Type ./Hash-Cracker.py -i for information'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--type"):
          type = arg
      elif opt in ("-h", "--hash"):
          hash1 = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      elif opt in ("-v", "--verbose"):
          ver = "yes"
      elif opt in ("-n", "--numbers"):
          numbrute = "yes"
  if not (type and hash1):
      print '[*]./Hash-Cracker.py -t <type> -h <hash> -w <wordlist>'
      sys.exit()
  if (type == "hashbrowns"):
      if (hash1 == "hashbrowns"):
          if (wordlist == "hashbrowns"):
              print "     ______"
              print "^. .^      \~"
              print " (oo)______/"
              print "   WW  WW"
              print " What a pig!!! "
              exit()
  print "[*]Hash: %s" % hash1
  print "[*]Hash type: %s" % type
  print "[*]Wordlist: %s" % wordlist
  print "[+]Cracking..."
  try:
      if (numbrute == "yes"):
         h = hash()
         h.hashcracknum(hash1, type)
      else:
         h = hash()
         h.hashcrack(hash1, type)

  except IndexError:
        print "\n[-]Hash not cracked:"
        print "[*]Reached end of wordlist"
        print "[*]Try another wordlist"
        print "[*]Words tried: %s" % h.num
  except KeyboardInterrupt:
        print "\n[Exiting...]"
        print "Words tried: %s" % h.num
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
if __name__ == "__main__":
    main(sys.argv[1:])
