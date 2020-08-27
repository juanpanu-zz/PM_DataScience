import time

class fiboIter():

    def __init__(self, max=None):
       self.max = max

    def __iter__(self):
        self.n1 = 1
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.counter < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            if self.counter == 1:
                self.counter += 1
                return self.n2
            self.aux = self.n1 + self.n2
            self.n1 = self.n2
            self.n2 = self.aux
            self.counter +=1
            return self.aux

        else:
            raise StopIteration

def fibo_gen(max=None):
    n1 = 1
    n2 = 1
    counter = 0
    while not max or counter < max:
        if counter == 0:
            counter += 1
            yield n1
        elif counter ==1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1 = n2
            n2 = aux
            counter += 1
            yield aux
            



def run():
    # my_iter = fiboIter()
    my_gen = fibo_gen()
    for element in my_gen:
        print(element)
        time.sleep(0.05)
    
if __name__ == "__main__":
    run()