from flask import Flask, render_template, request
app=Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')


@app.route('/map')
def map():
    markers=[
        {
        'lat':0,
        'lon':0,
        'popup':'This is the middle of the map.'
        },
    ]
    return render_template('map.html',markers=markers )
