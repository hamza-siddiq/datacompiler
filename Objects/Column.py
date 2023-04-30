
class Column:
    
    def __init__(self):
        self.words = []

    def add(self, word: str):
        self.words.append(word)
    
    def write(self, output):
        '''
        If a column is empty, output a space
        Otherwise, output the words in the words list
                   Also, if more than one word, add a space in between
        End the column, by displaying a partition "|"
        '''
        if len(self.words)==0:
            output.write(" ")
        else:
            for i in range(len(self.words)):
                output.write(self.words[i])
                if len(self.words) > 1 and i < len(self.words)-1:  
                    output.write(" ")
        output.write("|")
        self.words = []