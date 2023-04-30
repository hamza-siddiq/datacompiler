def tokenize(line: str) -> list:
  '''Gets the words from a line, and adds it to a list'''
  words = line.split(" ")
  removeNewLine(words)
  return words

def removeNewLine(words: str):
    '''
    New line is getting added to words, which we don't need for parsing,
    so remove it
    '''
    if words[-1][-1] == '\n':
        words[-1] = words[-1][:-1]