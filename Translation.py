import sqlite3

global English = ""
global Revian = ""

wdb = sqlite3.connect('words.db')
print('opened database')

cur = wdb.cursor()


cur.execute("SELECT word FROM words2 WHERE valid = 0 LIMIT 1")
rows = cur.fetchall()
English = rows
Decision = raw_input('1: Translate This Word | 2: This is not a word | 3: Quit')
if (Decision == 1):
  ReverseEnglish = English[::-1]
  LenRE = len(ReverseEnglish)
  Suggestion = English[0:1]+ReverseEnglish[1:LenRE - 1]+English[LenRE -1:]
  print 'English: '+English
  print 'Suggested Revian: '+Suggestion
  NewWord = raw_input('In Revian this is: ')