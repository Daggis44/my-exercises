def main(): # main function to run the tip calculator
    dollars = dollars_to_float(input("How much was the meal? "))    # get user input
    percent = percent_to_float(input("What percentage would you like to tip? ")) # get user input
    tip = dollars * percent # calculate the tip
    print(f"Leave ${tip:.2f}") # print the tip, formatted to 2 decimal places


def dollars_to_float(d): # e.g., "$12.34" -> 12.34
    float_d = d.replace("$", "") # remove the dollar sign
    return float(float_d) # convert to float

    # TODO


def percent_to_float(p): # e.g., "15%" -> 0.15
    float_p = p.replace("%", "") # remove the percent sign
    return float(float_p) / 100 # convert to decimal

    # TODO


main() # run the program