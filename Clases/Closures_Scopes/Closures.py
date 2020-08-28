def make_repeater_of(n):
    def repeater(string):
        return string*n
    return repeater

def run():
    repeat_5 =make_repeater_of(5)
    print(repeat_5('Hola'))

    repeat_50 =make_repeater_of(50)
    print(repeat_50('Platzi'))

if __name__ == "__main__":
    run()
    