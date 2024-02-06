from flask import Flask, render_template, request, redirect, url_for
from inventory import Dealership

app = Flask(__name__)
inv = Dealership()

inv.add_car('BMW', '330i', 2020, 'red', 'https://pictures.dealer.com/b/bmwofmonterey/0912/686292d644118d3dab8af5372bf5a98bx.jpg')
inv.add_car('BMW' , 'X5', 2019, 'black', 'https://www.primemotorz.com/imagetag/1133/main/l/Used-2019-BMW-X5-50i-XDRIVE-AWD-xDrive50i-1652475974.jpg')
inv.add_car('Porshe', '911', 2022, 'green', 'https://bringatrailer.com/wp-content/uploads/2023/03/2022_porsche_911-gt3-touring_img_5048-5-18879.jpg')

@app.route('/')
def home():
    cars = inv.list_available_cars()
    return render_template('home.html', cars=cars)

@app.route('/sell_car', methods=["GET", "POST"])
def sell_car():
    if request.method == 'POST':
        name = request.form.get('inputName')
        age = request.form.get('inputAge')
        inv.sell_car(name, age)
        return redirect(url_for('sold_cars'))

    car_for_sale = inv.get_the_car_for_sale()
    return render_template('sell_car.html', car=car_for_sale)


#add redirect, and fix it
@app.route('/add_car', methods=["GET","POST"])
def add_car():
    if request.method == 'GET':
        return render_template('add_car.html')

    make = request.form.get('inputMake')
    model = request.form.get('inputModel')
    year = request.form.get('inputYear')
    color = request.form.get('inputColor')
    picture = request.form.get('inputPicture')
    #print(make, model, year, color, picture)
    inv.add_car(make, model, year, color, picture)

    cars = inv.list_available_cars()
    return render_template('home.html', cars=cars)
@app.route('/sold_cars')
def sold_cars():
    cars_sold = inv.list_sold_cars()
    return render_template('sold_cars.html', cars=cars_sold)



if __name__ == "__main__":
    app.run(debug=True)
