from Objects.Column import Column


fileName, extension, date, code = Column(), Column(), Column(), Column() 
def parse(words: str):
    '''
    Parses the words into their respective columns
    '''
    for word in words:
        if "." in word:
            dotWords = word.split(".")
            fileName.add(dotWords[0])
            extension.add(dotWords[1])
        elif "-" in word:
            date.add(word)
        elif word.isupper():
            code.add(word)
        else:
            fileName.add(word)