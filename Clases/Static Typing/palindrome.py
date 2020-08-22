def is_palindrome(string: str)->bool:
    string=string.replace(' ','').lower().strip()
    return string == string[::-1]

def run():
    print(f'Ana = {is_palindrome("Ana")}')
    print(f'Luz azul = {is_palindrome("Luz azul")}')
    print(f'Python = {is_palindrome("Python")}')

if __name__ == "__main__":
    run()