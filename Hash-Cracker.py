#!/usr/bin/python
import StringIO
import getopt
import hashlib
import sys
import os
print "  "
print "Python Hash-Cracker"
print "Version 3.0-1 Stable"
more = "config/add.txt"

def info():
  print " "
  print "Information:"
  print "[*]Options:"
  print "[*](-h) Hash"
  print "[*](-t) Type [See supported hashes]"
  print "[*](-w) Wordlist"
  print "[*](-n) Numbers bruteforce"
  print "[*](-v) Verbose [{WARNING}Slows cracking down!]"
  print "[*]Examples:"
  print "[>]./Hash-Cracker.py -h <hash> -t md5 -w DICT.txt"
  print "[>]./Hash-Cracker.py -h <hash> -t sha384 -n -v"
  print "[*]Supported Hashes:"
  print "[>]md5, sha1, sha224, sha256, sha384, sha512"
  print "[*]Thats all folks!\n"

def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

def definepath():
    if check_os() == "posix":
        if os.path.isfile("fake-update"):
            return os.getcwd()
        else:
            return "/opt/Hermies"
    else:
        return os.getcwd() 

def check_config(param):
    fileopen = file("%s/config/config.txt" % (definepath()), "r")
    for line in fileopen:
        line=line.rstrip()
        #print line
        if line.startswith(param) != "#":
           if line.startswith(param):
                line = line.rstrip()
                line = line.replace('"', "")
                line = line.replace("'", "")
                line = line.split("=")
                return line[1]

class hash:
  def hashcrack(self, hash, type):
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
    wordlist1 = open(wordlist, "r")
    wordlist2 = wordlist1.read()
    buf = StringIO.StringIO(wordlist2)
    while True:
       line = buf.readline().strip()
       if (line == ""):
           print "\n[-]Hash not cracked:"
           print "[*]Reached end of wordlist"
           print "[*]Try another wordlist"
           print "[*]Words tryed: %s" % self.num
           break
       hash2 = h(line).hexdigest()
       if (ver == "yes"):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (hash2 == hash1):
           print "[+]Hash is: %s" % line
           print "[*]Words tryed: %s" % self.num
           break
       else:
           self.num = self.num + 1


  def hashcracknum(self, hash, type):
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
    num2 = 0
    while True:
       num2 = num2 + 1
       line = "%s" % num2
       hash2 = h(line).hexdigest()
       if (ver == "yes"):
           sys.stdout.write('\r' + str(line) + ' ' * 20)
           sys.stdout.flush()
       if (hash2 == hash1):
           print "[+]Hash is: %s" % line
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
        print "[*]Words tryed: %s" % h.num
  except KeyboardInterrupt:
        print "\n[Exiting...]"
        print "Words tryed: %s" % h.num
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
if __name__ == "__main__":
    main(sys.argv[1:])
