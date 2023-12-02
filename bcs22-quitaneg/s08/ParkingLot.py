class ParkingSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_lot = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1

    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def park_car(self, car):
        if self.is_full():
            print('The parking is full.')
            return
        self.rear = (self.rear + 1) % self.capacity
        self.parking_lot[self.rear] = car
        self.size = self.size + 1
        print('Car %s parked' % car)
        self.display()

    def leave_car(self):
        if self.is_empty():
            print('The list is empty or underflow')
            return
        item = self.parking_lot[self.front]
        self.parking_lot[self.front] = None  # Set the slot to None
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1
        print("%s left the parking lot" % str(item))
        self.display()

    def get_front(self):
        if self.is_empty():
            print('Queue empty')
        print('Front: %s' % self.parking_lot[self.front])

    def get_rear(self):
        if self.is_empty():
            print('Queue empty')
        print('Rear: %s' % self.parking_lot[self.rear])

    def display(self):
        print('Current Parking Lot:')
        for i in range(self.capacity):
            print(self.parking_lot[i], end=' ')
        print('\n')


if __name__ == '__main__':
    parking_system = ParkingSystem(5)

    while True:
        print(f'\nOptions:')
        print(f'1. Park a Car')
        print(f'2. Get the front')
        print(f'3. Get the rear')
        print(f'4. Leave the parking lot')
        print(f'5. Exit')

        choice = int(input('Enter your options (1-5): '))

        if choice == 1:
            car_number = input(f'Enter the car: ')
            parking_system.park_car(car_number)
        elif choice == 2:
            parking_system.get_front()
        elif choice == 3:
            parking_system.get_rear()
        elif choice == 4:
            parking_system.leave_car()
        elif choice == 5:
            print(f'Exiting Parking System')
            break
        else:
            print(f'Choose a valid option.')