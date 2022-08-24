from flask import Flask, render_template, request
app=Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

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
