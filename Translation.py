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
  English = str(rows).strip("(),'")
  print str(English)+"\n"
  Decision = raw_input('1: Translate This Word | 2: This is not a word | 3: Quit\nChoice: ')
  print Decision
  if Decision == "1":
    print "Correct\n"
    ReverseEnglish = English[::-1]
    print ReverseEnglish+"\n"
    LenRE = len(ReverseEnglish)
    Suggestion = English[0:1]+ReverseEnglish[1:(LenRE - 1)]+English[(LenRE - 1):]
    print 'English: '+ str(English)
    print 'Suggested Revian: '+ str(Suggestion)
    NewRevian = raw_input('\nIn Revian this is: ')
    NewPos = raw_input('\nWhat part of speech is this: ')
    print "English word: "+str(English)+" in Revian is: "+str(NewRevian)+" and is a: "+NewPos+"\n"
    Correct = raw_input('\nIs that correct?\n')
    if Correct == "1":
      cur.execute("INSERT INTO revian(english TEXT, revian TEXT, pos TEXT) VALUES (?,?,?)", (str(English),str(NewRevian),str(NewPos)))
      wdb.commit()
      NextWord()
    if Correct == "2":
      NextWord()

  if Decision == "2":
    cur.execute("UPDATE words2 SET valid = 1 WHERE word = ?", (str(English),)
    wdb.commit()
    NextWord()
    
  if Decision == "3":
    sys.exit("User Quit")
    
  return

NextWord()
