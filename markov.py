import sys
import random

def leer_archivo(file):    
    with open(file) as f:
        contents = f.read()
    return contents
 
def proceso(data, context):
    '''Make a rule dict for given data.'''
    rule = {}
    words = data.split(' ')
    index = context
 
    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1
 
    return rule
 
 
def concatenacion(rule, length):    
    '''Use a given rule to make a string.'''
    oldwords = random.choice(list(rule.keys())).split(' ') #random starting words
    string = ' '.join(oldwords) + ' '
 
    for i in range(length):
        try:
            key = ' '.join(oldwords)
            newword = random.choice(rule[key])
            string += newword + ' '
 
            for word in range(len(oldwords)):
                oldwords[word] = oldwords[(word + 1) % len(oldwords)]
            oldwords[-1] = newword
 
        except KeyError:
            return string
    return string
 
 
if __name__ == '__main__':
    data = leer_archivo(sys.argv[1])
    rule = proceso(data, int(sys.argv[2]))
    string = concatenacion(rule, int(sys.argv[3]))
    print(string)