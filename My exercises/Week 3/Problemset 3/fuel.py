def main():
    p = convert(input("Fraction: "))
    print(gauge(p))
    
def convert(frac_str):

    while True:
        try:
            x_str, y_str = frac_str.split("/", 1)
            x, y = int(x_str), int(y_str)
            if x < 0 or y <= 0 or x > y:
                raise ValueError
            return round((x / y)* 100)
        except (ValueError, ZeroDivisionError):
            frac_str = input("Fraction: ")

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{p}%"


main()