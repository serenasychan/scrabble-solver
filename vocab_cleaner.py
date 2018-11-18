# cleaning French vocabulary
import string
from functools import reduce

chars_to_omit = ['\'', '.', '\\', '-', '/'] + [d for d in string.digits]

def clean_french_vocab(infile='vocab_fr.txt'):
    convert_to_alpha = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a',
    'å': 'a', 'æ': 'ae', 'ç': 'c', 'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
    'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i', 'ð': 'o', 'ñ': 'n', 'ò': 'o',
    'ó': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ø': 'oe', 'ù': 'u', 'ú': 'u',
    'û': 'u', 'ü': 'u', 'ý': 'y', 'þ': 'th'}

    outfile = '{}-cleaned.{}'.format(*infile.split('.'))

    with open(infile, 'r', encoding='utf-8') as f_in:
        f_out = open(outfile, 'w')
        for word in f_in.readlines():
            word = word.strip()
            if reduce((lambda x, y: x or y),
                      map(lambda x: x in word, chars_to_omit)):
                continue
            elif len(word) == 1:
                continue
            cleaned_word = ''
            for c in word.lower():
                if c not in string.ascii_lowercase:
                    cleaned_word += convert_to_alpha[c]
                else:
                    cleaned_word += c
            f_out.write(cleaned_word + '\n')
        f_out.close()
            

