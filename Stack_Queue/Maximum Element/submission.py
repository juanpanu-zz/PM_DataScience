def stack_query(input):
    stack = []
    max_stack = []

    for i in range(int(input())):
        my_inp=input()

        if my_inp[0] == '1':				#Push element into the stack if input is 1
            n = int(my_inp.split()[1])
            stack.append(n)

            if len(max_stack) == 0 or max_stack[-1] < n:
                max_stack.append(n)				

            else: 
                max_stack.append(max_stack[-1])

        elif my_inp == '2':				#Delete the element present at the top of the stack
            stack.pop()	
            max_stack.pop()

        else:				#Print Max element.
            print(max_stack[-1])

    return max_stack
            
if __name__ == "__main__":
    STDOUT=stack_query(input)
    