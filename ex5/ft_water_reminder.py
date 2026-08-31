def ft_water_reminder():
    unwatered = int(input("Enter plant age in days: "))
    print(f"Days since last watering: {unwatered}")
    if (unwatered <= 2):
        print("Plants are fine")
    else:
        print("Water the plants!")
