# Resolve the problem!!
import re

def run():
    # Start coding here
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        
        text2decode= f.readline()
        azchar= re.findall('[a-z]',text2decode)
        decodedText = ''.join(azchar)
        print('Hidden message is: ' + decodedText)


if __name__ == '__main__':
    run()
