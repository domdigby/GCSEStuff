import math


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


def area_calculation():
    """
    Challenge 23:  A gardener needs to buy some turf for a project
    they are working on. The garden is rectangular
    with a circular flower bed in the middle.
    :return:
    """
    # Ask for user inputs - catch non number
    try:
        lawn_length = float(input("Enter the lawn length in metres: "))
        lawn_width = float(input("Enter the lawn width in metres: "))
        bed_radius = float(input("Enter the flower bed radius in metres: "))
    except ValueError as e:
        print(f"{e.args[0]} was not a valid number.  Please retry")
        return

    # Calculate the area of the rectangle
    lawn_area = lawn_length * lawn_width

    # Calculate the area of the flower beb
    flower_bed = math.pi * bed_radius * bed_radius

    # Subtract the flower bed from the lawn area for the turf required
    lawn_area = lawn_area - flower_bed

    print(f"{lawn_area:.2f} m2 of turf is required for a lawn {lawn_length} m by {lawn_width} m, with a flower bed of {bed_radius} m radius")


if __name__ == '__main__':
    # car_discount()
    #speed_distance_time()
    area_calculation()