def hey(statement):
    if (statement.isspace() or len(statement) == 0):
        return 'Fine. Be that way!'
    elif (statement.isupper()):
        return 'Whoa, chill out!'
    elif (statement.strip().endswith('?')):
        return 'Sure.'
    else:
        return 'Whatever.'
