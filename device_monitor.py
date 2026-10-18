
readings = [28, 31, 35, 37, 29]


# Display Menu
def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Readings")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


# Option 1: Display Readings
def display_reading(readings):
    print("\nCURRENT READINGS")
    print("----------------")

    position = 1

    for reading in readings:
        print(f"Reading {position} {reading} °C")
        position = position + 1


# Input Validation
def is_whole_number(text):
    if len(text) == 0:
        return False

    position = 0

    if text[0] == "-":
        position = 1

    if position == len(text):
        return False

    for character in text[position:]:
        if character not in "0123456789":
            return False

    return True


# Option 2: Add Readings
def add_reading(readings):
    reading = input("Enter new reading: ")

    if reading == "":
        print("Invalid input. Reading cannot be empty.")

    elif not is_whole_number(reading):
        print("Invalid input. Enter a whole number.")

    elif int(reading) < 0 or int(reading) > 100:
        print("Invalid reading. Enter a value from 0 to 100.")

    else:
        reading = int(reading)
        readings.append(reading)
        print("Reading added successfully!")


# Option 3: Classify Readings
def classify_reading(reading):
    if reading < 30:
        return "NORMAL"
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings):
    print("\nREADING CLASSIFICATIONS")
    print("-----------------------")

    for reading in readings:
        category = classify_reading(reading)
        print(f"{reading} °C - {category}")


# Option 4: Numerical Summary Functions
def compute_total(readings):
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    total = compute_total(readings)
    average = total / len(readings)

    return average


def find_minimum(readings):
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, category):
    count = 0

    for reading in readings:
        if classify_reading(reading) == category:
            count = count + 1

    return count


def compute_percentage(count, total):
    percentage = count / total * 100

    return percentage


def determine_overall_status(warning, critical):
    if critical > 0:
        return "ATTENTION REQUIRED"
    elif warning > 0:
        return "MONITOR"
    else:
        return "NORMAL"


def generate_summary(readings):
    total_readings = len(readings)

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal = count_category(readings, "NORMAL")
    warning = count_category(readings, "WARNING")
    critical = count_category(readings, "CRITICAL")

    normal_percentage = compute_percentage(normal, total_readings)
    warning_percentage = compute_percentage(warning, total_readings)
    critical_percentage = compute_percentage(critical, total_readings)

    status = determine_overall_status(warning, critical)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of Readings: {total_readings}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f} °C")
    print(f"Minimum: {minimum} °C")
    print(f"Maximum: {maximum} °C")

    print("\nCATEGORY BREAKDOWN")
    print("------------------")
    print(f"NORMAL: {normal} ({normal_percentage:.2f}%)")
    print(f"WARNING: {warning} ({warning_percentage:.2f}%)")
    print(f"CRITICAL: {critical} ({critical_percentage:.2f}%)")

    print(f"\nOverall Status: {status}")


# Main Program
def main():
    while 1 == 1:
        display_menu()

        choice = input("Enter choice: ")

        if choice == "1":
            display_reading(readings)

        elif choice == "2":
            add_reading(readings)

        elif choice == "3":
            display_classifications(readings)

        elif choice == "4":
            generate_summary(readings)

        elif choice == "5":
            print("Thank you for using our services!")
            break

        else:
            print("--------------")
            print("INVALID CHOICE")
            print("--------------")


main()
