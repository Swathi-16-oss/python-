def rev_str(str):
    # to split the string into words
    words=str.split(' ')
    #reverse the word and join with space
    
    rev_str=' '.join(reversed(words))
    #print string which is reversed
    return rev_str
if __name__=="__main__":
    string="swathi is a good"
    print(rev_str(string))
    
    
    
'''o/p:
good a is swathi'''
