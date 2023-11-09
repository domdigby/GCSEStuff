def car_discount():
    # Get the retail cost
    retail_cost = input("Enter the retail cost of the car: ")
    discount_amount = 1000

    # Convert to a float
    retail_cost = float(retail_cost)

    # Check if discount is due
    if retail_cost > 10000:
        print(
            f"Congratulations.  Because you spent {retail_cost}, you are due discount of {discount_amount}.  Therefore the total cost will be {(retail_cost - discount_amount)}")
    else:
        print("Congratulation on the purchase of your car.")


def speed_distance_time():
    # #ask for desired output
    calc_dec = input("Enter what you want to calculate.\n Speed, Distance or Time? ")

    while calc_dec.lower() not in ("speed", "distance", "time"):
        calc_dec = input("Please enter a valid option: Speed, Distance or Time? ")

    try:
        if calc_dec.lower() == "speed":
            distance = float(input("Enter Distance in metres: "))
            time = float(input("Enter Time in seconds: "))
            units = "m/s"
            calc = distance / time
        elif calc_dec == "distance":
            speed = float(input("Enter Speed in m/s: "))
            time = float(input("Enter Time in seconds: "))
            units = "m"
            calc = speed * time
        else:  # calc_dec == "time"
            distance = float(input("Enter Distance in metres: "))
            speed = float(input("Enter Speed in m/s: "))
            units = "s"
            calc = distance / speed

    except ZeroDivisionError:
        calc = 0

    print(f"The desired {calc_dec} will be: {calc} {units}")


if __name__ == '__main__':
    # car_discount()
    speed_distance_time()
