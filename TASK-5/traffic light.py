light = input("Enter traffic light color: ")

if light.lower() == "red":
    print("Stop")
elif light.lower() == "yellow":
    print("Wait")
elif light.lower() == "green":
    print("Go")
else:
    print("Invalid color")