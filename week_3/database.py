import csv
import os


class BaseCar:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = ''

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        self.body_length, self.body_width, self.body_height = 0, 0, 0

        if body_whl:
            lst = self.body_whl.split('x')
            self.body_length, self.body_width, self.body_height = float(lst[0]), float(lst[1]), float(lst[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def create_car(line):
    if line[0] == 'car':
        return Car(line[1], line[3], float(line[5]), int(line[2]))
    if line[0] == 'truck':
        return Truck(line[1], line[3], float(line[5]), line[4])
    if line[0] == 'spec_machine':
        return SpecMachine(line[1], line[3], float(line[5]), line[6])
    return None


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) != 7:
                continue
            else:
                obj = create_car(row)
                car_list.append(obj)
    return car_list


def main():
    path = 'coursera_week3_cars.csv'
    get_car_list(path)


if __name__ == '__main__':
    main()


