directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        word_in_lowercase = word.lower()
        if word_in_lowercase in directions:
            result.append(('direction', word))
        elif word_in_lowercase in verbs:
            result.append(('verb', word))
        elif word_in_lowercase in stops:
            result.append(('stop', word))
        elif word_in_lowercase in nouns:
            result.append(('noun', word))
        else:
            number = convert_number(word_in_lowercase)
            if(number):
                result.append(('number', number))
            else:
                result.append(('error', word))
    return result
    
