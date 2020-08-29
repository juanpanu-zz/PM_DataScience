import re

def run():
    book = ''
    with open('bible.txt','r',encoding='utf-8') as f:
        book = f.read()

    pattern=re.compile(r'Ju\w+')

    words_type_1=set(re.findall(pattern,book))
    for word in words_type_1:
        print(word)

if __name__ == "__main__":
        run()