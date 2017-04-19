#-*-coding: utf-8 -*-
import re
import string

def readAndWrite(doSomething, textFile, resultFile):
    result = list()
    with open(textFile, 'rU') as f:
        for line in f:
            if line=='\n':
                continue
            line = line.strip()
            doSomething(line, result)
    with open(resultFile, 'w') as g:
        g.write('%s' % '\n'.join(result))

def lineSplit(line, result):
   line = re.compile(r'[?$|.*展开全文c|↓*.]|[a-zA-z]+://[^\s]*').sub('', line)
   print(line)
   newLine = re.split(r'[‘’…→（），。；@！？#【】《》：\...“”、\s]\s*', line)
   for i in range(len(newLine)):
       result.append(newLine[i])
   return result 

def removeAllPunctuation(line, result):
    translator = str.maketrans('', '', string.punctuation)
    line = line.translate(translator)
    result.append(line)
    return result

textFile = 'text.txt'
resultFile = 'resultSplit.txt'
readAndWrite(lineSplit, textFile, resultFile)
textFile = 'resultSplit.txt'
resultFile = 'resultRemovePunc.txt'
readAndWrite(removeAllPunctuation, textFile, resultFile)
