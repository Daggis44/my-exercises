def main():
    t = convert(input("What time is it? ").strip())

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time: str) -> float:
    time = time.strip()
    if ":" in time:
        h, m = time.split(":", 1)
        h = int(h)
        m = int(m) if m else 0        # handles "18:" as 18:00
    else:
        h, m = int(time), 0               # handles "18" as 18:00
    return h + m / 60

if __name__ == "__main__":
    main()
