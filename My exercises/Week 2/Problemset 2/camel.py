



def main():
    s = input("CamelCase: ")
    snake_case(s)

    


def snake_case(s):
    for c in s:
        print(c, end="")
        if c.isupper():
            print("_", end="") 
    
    


main()