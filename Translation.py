import sqlite3
import sys

global English
global Revian
wdb = sqlite3.connect('words.db')
wdb.text_factory = str
print('opened database')
  
def NextWord():
  cur = wdb.cursor()
  cur.execute("SELECT word FROM words2 WHERE valid = 0 LIMIT 1")
  rows = cur.fetchone()
  global English
  English = str(rows).strip('(),')
  print str(English)+"\n"
  Decision = raw_input('1: Translate This Word | 2: This is not a word | 3: Quit\nChoice: ')
  print Decision
  if Decision == "1":
    print "Correct"
    ReverseEnglish = English[::-1]
    LenRE = len(ReverseEnglish)
    Suggestion = English[0:1]+ReverseEnglish[1:LenRE - 1]+English[LenRE -1:]
    print 'English: '+ str(English)
    print 'Suggested Revian: '+ str(Suggestion)
    NewWord = raw_input('In Revian this is: ')

  if Decision == "2":
    cur.execute("UPDATE words2 SET valid = 1 WHERE word = ?", (str(English)))
    wdb.commit()
    NextWord()
    
  if Decision == "3":
    sys.exit("User Quit")
    
  return

NextWord()
