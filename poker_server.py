# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import json
app = Flask(__name__)

sim_data = {}


@app.route('/ddz_start', methods=["POST"])
def ddz_start():
    if request.method == 'POST':
        username = request.form['user1']
        print(request.form)
        print("q%sq" % (username))
    return "ok"


@app.route('/ddz')
def ddz():
    return render_template("ddz.html")


@app.route('/ddz_count', methods=["POST"])
def ddz_count():
    if request.method == 'POST':
        data = request.data.decode("utf8")
        print(data)
        j_data = json.loads(data)
        users = j_data['users'].split(';')
        dz = j_data['dz']
        print(j_data)
        is_win = int(j_data['is_win'])
        is_men = int(j_data['is_men'])
        bomb = int(j_data['bomb'])
        dz_score = (is_win * 2 - 1) * 2 * 2 ** (bomb + is_men)
        print("dz %d" % dz_score)
        if dz not in sim_data:
            sim_data[dz] = [dz_score]
        else:
            sim_data[dz].append(sim_data[dz][-1] + dz_score)
        for u in users:
            if u != dz:
                if u not in sim_data:
                    sim_data[u] = [-dz_score // 2]
                else:
                    sim_data[u].append(sim_data[u][-1] + (-dz_score // 2))
        print(sim_data)
        return json.dumps(sim_data)
    return "ok"


@app.route('/ddz_score', methods=["POST"])
def ddz_score():
    if request.method == 'POST':
        data = request.data
        j_data = json.loads(data)
        users = j_data['users'].split(';')
        return str(users)
    return "ok"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.data
    print(data)
    return data


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
