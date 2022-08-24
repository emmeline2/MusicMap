import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

# data base helper functions ---------
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None: 
        abort(404)
    return post

# flask setup ------------------
app=Flask(__name__)
app.config['SECRET_KEY'] = 'randomstringofStuff109238ksldkjf'


# page routing functions ------------
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    title = None
    if request.method == 'POST': 
        title = request.form['title']
        content = request.form['content']
        lat = request.form['lat']
        lon = request.form['lon']
    if not title: 
        flash('Title is required!')
    else: 
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title,content, lat, lon) VALUES (?,?, ?,?)', (title, content, lat, lon))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        lat = request.form['lat']
        lon = request.form['lon']
    
        if not title: 
            flash('Title is required!')
        else: 
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?, lat = ?, lon = ?'
            ' WHERE id = ?', 
            (title, content, lat, lon, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was sucessfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

@app.route('/map')
def map():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    print("POSTS: ", posts)
    # create markers matrix
    markers = []
    for post in posts:
        pin_point = {
            'lat': post['lat'],
            'lon': post['lon'],
            'popup': (post['title'] + " : " + post['content']),
        }
        markers.append(pin_point)
        pin_point = {}

    return render_template('map.html',markers=markers )
