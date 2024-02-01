from uuid import uuid4


class Car:

    def __init__(self, make, model, year, color, img):
        self._id = str(uuid4())
        self._is_sold = False
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._img = img

    def to_dict(self):
        car_dict = {
            'id': self._id,
            'make': self._make,
            'model': self._model,
            'year': self._year,
            'color': self._color,
            'pic': self._img
        }
        if self.is_sold():
            car_dict['owner_name'] = self._owner_name
            car_dict['owner_age'] = self._owner_age
        return car_dict


    def sell(self, name, age):
        self._owner_name = name
        self._owner_age = age
        self._is_sold = True

    def is_sold(self):
        return self._is_sold



if __name__ == "__main__":
    car1 = Car('BMW', '330i', 2020, 'red', 'https://vehicle-images.dealerinspire.com/409f-110005683/WBA5R7C02LFJ09798/cf7e99d4feb1de698e683cca89ced0af.jpg')
    print(car1.to_dict())
    car2 = Car('BMW' , 'X5', 2019, 'black', 'https://www.primemotorz.com/imagetag/1133/main/l/Used-2019-BMW-X5-50i-XDRIVE-AWD-xDrive50i-1652475974.jpg')

