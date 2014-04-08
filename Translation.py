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
  DupEnglish = "to " + English
  cur.execute("SELECT english FROM revian WHERE english = ?", (str(DupEnglish),))
  thecount = cur.fetchone()
  print str(thecount)+"\n"
  cur.execute("SELECT english FROM revian WHERE english = ?", (str(English),))
  normality = cur.fetchone()
  print normailty
  print "-------------------------------\n\n\n"
  print str(English)+"\n"
  Decision = raw_input('1: Translate This Word | 2: This is not a word | 3: Insert word | 4: Quit\nChoice: ')
  print Decision
  if Decision == "1":
    print "-------------------------------\n\n\n"
    ReverseEnglish = English[::-1]
    print ReverseEnglish+"\n"
    LenRE = len(ReverseEnglish)
    Suggestion = English[0:1]+ReverseEnglish[1:(LenRE - 1)]+English[(LenRE - 1):]
    print 'English: '+ str(English)
    print 'Suggested Revian: '+ str(Suggestion)
    NewRevian = raw_input('\nIn Revian this is: ')
    chars = set('hjkpquwxz')
    if any((c in chars) for c in NewRevian.lower()):
      print 'Revian contains invalid characters\n'
      try:
        NewRevian = NewRevian.lower().replace('h','a')
        NewRevian = NewRevian.lower().replace('j','g')
        NewRevian = NewRevian.lower().replace('k','c')
        NewRevian = NewRevian.lower().replace('w','o')
        NewRevian = NewRevian.lower().replace('p','b')
        NewRevian = NewRevian.lower().replace('q','c')
        NewRevian = NewRevian.lower().replace('u','o')
        NewRevian = NewRevian.lower().replace('x','c')
        NewRevian = NewRevian.lower().replace('z','s')
      except:
        NewRevian = NewRevian
      print 'Here it is in proper Revian characters: '+str(NewRevian)
      Accept = raw_input('Accept new changes? (y/n)\n')
      if Accept == "n":
        NextWord()
    cur.execute("SELECT COUNT() FROM revian WHERE revian = ?", (str(NewRevian),))
    existing = cur.fetchone()
    existing = str(existing).strip("(),'")
    wait = raw_input()
    if existing != '0':
      print '---------------------\nRevian appears to already exist! Please rewrite.'
      NextWord()
    NewPos = raw_input('What part of speech is this: ')
    if NewPos.lower() == "verb":
      English = "to "+str(English)
      print 'Verb is: '+str(NewRevian)
      VerbNoun = raw_input('Please enter Noun form:\n')
      VerbNounEng = raw_input('Please enter Noun in English:\n')
      print 'English is: '+str(VerbNounEng)+' & in Revian is: '+str(VerbNoun)+' & is a: Noun\n'
      YesRight = raw_input('Is that correct? (y/n)\n')
      if YesRight == "y":
        cur.execute("INSERT INTO revian VALUES (?,?,?)", (str(VerbNounEng),str(VerbNoun),("Noun")))
        wdb.commit()
      if YesRight == "n":
        NextWord()
    print "English word: "+str(English)+" & in Revian is: "+str(NewRevian)+" & is a: "+NewPos+"\n"
    Correct = raw_input('Is that correct? (y/n)\n')
    if Correct == "y":
      cur.execute("INSERT INTO revian VALUES (?,?,?)", (str(English),str(NewRevian),str(NewPos)))
      wdb.commit()
      cur.execute("UPDATE words2 SET valid = 1 WHERE word = ?", (str(English),))
      wdb.commit()
      NextWord()
    if Correct == "n":
      NextWord()

  if Decision == "2":
    cur.execute("UPDATE words2 SET valid = 1 WHERE word = ?", (str(English),))
    wdb.commit()
    NextWord()
    
  if Decision == "3":
    Eng = raw_input('English word:\n')
    Rev = raw_input('Revian word:\n')
    Pos = raw_input('Part of Speech:\n')
    cur.execute("INSERT INTO revian VALUES (?,?,?)", (str(Eng),str(Rev),str(Pos)))
    wdb.commit()
    NextWord()
    
  if Decision == "4":
    sys.exit("User Quit")
    
  return

NextWord()
