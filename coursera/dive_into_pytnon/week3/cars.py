import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand, self.photo_file_name, self.carrying = brand, photo_file_name, float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand, self.photo_file_name = brand, photo_file_name
        self.carrying, self.passenger_seats_count = float(carrying), int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        try:
            if body_whl != "" and len(body_whl.split("x")) == 3:
                self.body_width = float(body_whl.split("x")[1])
                self.body_height = float(body_whl.split("x")[2])
                self.body_length = float(body_whl.split("x")[0])
            else:
                self.body_width = float(0)
                self.body_height = float(0)
                self.body_length = float(0)
        except ValueError:
            self.body_width = float(0)
            self.body_height = float(0)
            self.body_length = float(0)

    def get_body_volume(self):
        return float(self.body_width) * float(self.body_height) * float(self.body_length)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand, self.photo_file_name = brand, photo_file_name
        self.carrying, self.extra, self.car_type = float(carrying), extra, 'spec_machine'


def _is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def _is_car_base(brand, photo_file_name, carrying):
    check_photo = set(['.jpg', '.jpeg', '.png', '.gif'])
    return brand != '' and os.path.splitext(photo_file_name)[1] in check_photo and _is_float(carrying)


def _is_car(car_type, passenger_seats_count, body_whl, extra):
    return car_type == 'car' and passenger_seats_count.isdigit() and body_whl == '' and extra == ''


def _is_truck(car_type, passenger_seats_count, extra):
    return car_type == 'truck' and passenger_seats_count == '' and extra == ''


def _is_spec_machine(car_type, passenger_seats_count, body_whl, extra):
    return car_type == 'spec_machine' and passenger_seats_count == '' and body_whl == '' and extra != ''


def get_car_list(csv_filename):
    try:
        with open(csv_filename, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            car_list = []
            cur_list = []
            car_dict = {}
            reader_list = list(reader)
            print(os.stat(csv_filename).st_size)
            if not os.stat(csv_filename).st_size <= 2:
                if reader_list[0][0] != '':
                    for row in reader_list[1:]:
                        if row != [] and row[0] != '':
                            cur_list.append(zip(reader_list[0], row))
                    for i in cur_list:
                        for j in i:
                            car_dict[j[0]] = car_dict.get(j[0], [])
                            car_dict[j[0]].append(j[1])
                    for i in range(len(car_dict['car_type'])):
                        if _is_car_base(car_dict['brand'][i], car_dict['photo_file_name'][i], car_dict['carrying'][i]):
                            if _is_car(car_dict['car_type'][i], car_dict['passenger_seats_count'][i], car_dict['body_whl'][i], car_dict['extra'][i]):
                                car_list.append(Car(car_dict['brand'][i], car_dict['photo_file_name'][i], car_dict['carrying'][i], car_dict['passenger_seats_count'][i]))
                            elif _is_truck(car_dict['car_type'][i], car_dict['passenger_seats_count'][i], car_dict['extra'][i]):
                                car_list.append(Truck(car_dict['brand'][i], car_dict['photo_file_name'][i], car_dict['carrying'][i], car_dict['body_whl'][i]))
                            elif _is_spec_machine(car_dict['car_type'][i], car_dict['passenger_seats_count'][i], car_dict['body_whl'][i], car_dict['extra'][i]):
                                car_list.append(SpecMachine(car_dict['brand'][i], car_dict['photo_file_name'][i], car_dict['carrying'][i], car_dict['extra'][i]))
    except KeyError:
        return car_list
    return car_list

