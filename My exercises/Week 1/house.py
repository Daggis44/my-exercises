
name = input("What's your name? ") .strip().title()

match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    
    case "Draco":
        print("Slytherin")

    case "Luna":
        print("Ravenclaw")

    case "Cedric":
        print("Hufflepuff")

    case "Albus":
        print("Headmaster")    
        
    case _:
        print("Who?")

