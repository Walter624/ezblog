from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

@app.route('/')
def default():
    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    posts = db.posts.find()
    return render_template("default.html", posts=posts)

@app.route('/post/<post_id>')
def single_post(post_id):
    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    post = db.posts.find_one({'_id': ObjectId(post_id)})
    return render_template('single_post_template.html', post=post)

@app.route('/post/create')
def create_post():
    return render_template('post_template.html', action='/post/process-create-post', title='Create Post')

@app.route('/post/process-create-post', methods=['POST'])
def process_create_post():
    errors = {}
    if len(request.form["title"]) < 5:
        errors['title'] = 'The title must be 5 characters or more'

    if len(request.form['content']) < 20:
        errors['content'] = 'The content must have 20 characters or more'

    if errors:
        return render_template('post_template.html', error=errors)

    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    db.posts.save({'title': request.form['title'], 'content': request.form['content']})
    return redirect(url_for('default'))

@app.route('/post/edit/<post_id>')
def edit_post(post_id):
    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    post = db.posts.find_one({'_id': ObjectId(post_id)})
    return render_template('post_template.html', post=post, action='/post/process-edit-post', title='Edit Post')

@app.route('/post/process-delete-post', methods=['POST'])
def process_delete_post():
    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    db.posts.remove({'_id': ObjectId(request.form['_id'])})
    return redirect(url_for('default'))

if __name__ == '__main__':
    app.run(debug=True)