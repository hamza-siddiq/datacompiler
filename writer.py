from _parser import fileName, extension, date, code


def write(output):
    '''
    Output each column
    '''
    code.write(output)
    date.write(output)
    fileName.write(output)
    extension.write(output)
    output.write("\n")