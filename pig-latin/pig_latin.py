vowels = 'aeiou'
def translate_text(text):
    if vowels.find(text[0]) != -1:
        return text+'ay'
    elif text[:2] == 'xr' or text[:2] == 'yt':
        return text+'ay'
    elif text[:3] == 'sch' or text[:3] == 'squ' or text[:3] == 'thr':
        return text[3:] + text[:3] + 'ay'
    elif text[:2] == 'qu' or text[:2] == 'rh' or text[:2] == 'th' or text[:2] == 'ch':
        return text[2:] + text[:2] + 'ay'
    else:
        return text[1:] +text[0] + 'ay'

def translate(text):
    return ' '.join(list(map(translate_text, text.split())))
