#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) >= 1:
        for i in range(len(sentence)):
            return (len(sentence), sentence[i])
    else:
        return (len(sentence), 'None')
