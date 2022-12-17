from flask import Flask, request
from markupsafe import escape

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    name = request.args.get("name", "World")
    return app.send_static_file('index.html')

@app.route('/view-price')
def viewprice_page():
    name = request.args.get("name", "World")
    return app.send_static_file('view-price.html')

@app.route('/track-price')
def trackprice_page():
    name = request.args.get("name", "World")
    return app.send_static_file('track-price.html')

@app.route('/manage-trackers')
def managetrackers_page():
    name = request.args.get("name", "World")
    return app.send_static_file('manage-trackers.html')

@app.route('/export-prices')
def exportprices_page():
    name = request.args.get("name", "World")
    return app.send_static_file('export-prices.html')


""" if __name__ == "__main__":
    app.run(debug=True) """

""" TO run : python -m flask run """