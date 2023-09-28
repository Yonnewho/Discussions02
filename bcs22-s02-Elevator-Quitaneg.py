import time

def move_elevator(current_floor, designated_floor):
    if current_floor == designated_floor:
        print(f"Elevator is already on floor {current_floor}.")
    elif current_floor < designated_floor:
        for floor in range(current_floor, designated_floor + 1):
            print(f"Moving up: Floor {floor}")
            time.sleep(1)  
        current_floor = designated_floor
    else:
        for floor in range(current_floor, designated_floor - 1, -1):
            print(f"Moving down: Floor {floor}")
            time.sleep(1)  
        current_floor = designated_floor

    return current_floor

def main():
    current_floor = int(input("Enter the current floor (1-10): "))
    designated_floor = int(input("Enter the designated floor (1-10): "))

    if current_floor < 1 or current_floor > 10 or designated_floor < 1 or designated_floor > 10:
        print("Error: Invalid floor input.")
        return

    elevator_floors = list(range(1, 11))

    if current_floor not in elevator_floors or designated_floor not in elevator_floors:
        print("Error: Invalid floor input.")
        return

    current_floor = move_elevator(current_floor, designated_floor)

if __name__ == "__main__":
    main()
