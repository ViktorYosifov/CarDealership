from flask import Flask, render_template
from inventory import Dealership

app = Flask(__name__)
inv = Dealership()

inv.add_car('BMW', '330i', 2020, 'red', 'https://vehicle-images.dealerinspire.com/409f-110005683/WBA5R7C02LFJ09798/cf7e99d4feb1de698e683cca89ced0af.jpg')
inv.add_car('BMW' , 'X5', 2019, 'black', 'https://www.primemotorz.com/imagetag/1133/main/l/Used-2019-BMW-X5-50i-XDRIVE-AWD-xDrive50i-1652475974.jpg')


@app.route('/')
def home():
    cars = inv.list_available_cars()
    return render_template('home.html', cars=cars)

@app.route('/sell_car')
def sell_car():
    car_for_sale = inv.get_the_car_for_sale()
    return render_template('sell_car.html', car=car_for_sale)

@app.route('/add_car')
def add_car():
    pass

@app.route('/sold_cars')
def sold_cars():
    pass



if __name__ == "__main__":
    app.run(debug=True)