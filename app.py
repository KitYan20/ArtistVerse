import spotify
import flask
from flask import Flask, Response, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    print(0)
    return render_template('Main.HTML')

@app.route('/api/search',methods=['GET', 'POST'])
def search():
    query = request.form.get("artist")
    print(1, query)
    results = spotify.Playlist(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
