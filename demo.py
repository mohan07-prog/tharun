amount = 200
balance =150

try:
    if amount<balance:
        raise ValueError("amount less than balance")
    else:
        print("Amount Greater")
except ValueError as e:
    print(e)