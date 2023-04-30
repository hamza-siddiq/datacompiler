from tokenizer import tokenize
from headingPrinter import printHeading
from _parser import parse
from writer import write


if __name__ == "__main__":
    output = open('output.txt','w')
    printHeading(output)
    with open('input.txt', 'r') as input:
        for line in input:
            words = tokenize(line)
            parse(words)
            write(output)
    output.close()