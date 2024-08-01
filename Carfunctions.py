command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started. Ready to go!")
    if command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    if command == "help":
        print("""
Start --to start the car
Stop --to stop the car
Quit --to quit """)
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand.")

