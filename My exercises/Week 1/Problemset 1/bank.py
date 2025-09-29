def main():
    input_str = input("Greeting: ")
    print(f"${value(input_str)}") #f-string to format output as currency


def value(greeting):     #function to determine value based on greeting
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):   #if greeting.lower().startswith("hello"): also works
        return 0
    elif greeting.startswith("h"): #    elif greeting[0].lower() == "h": also works
        return 20
    else:
        return 100      
    
main()
