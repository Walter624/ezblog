from bson.objectid import ObjectId
from flask import render_template, request, redirect, url_for

from ezblog import app
from ezblog.models import db
from ezblog.models.blog import Post


@app.route('/')
def default():
    post_model = Post(db)
    return render_template("default.html", posts=post_model.get_all_posts())

@app.route('/post/<post_id>')
def single_post(post_id):
    post_model = Post(db)
    return render_template('single_post_template.html', post=post_model.get_single_post(post_id))

@app.route('/post/create')
def create_post():
    return render_template(
        'post_template.html',
        action='/post/process-create-post',
        title='Create Post'
    )

@app.route('/post/process-create-post', methods=['POST'])
def process_create_post():
    errors = {}
    if len(request.form["title"]) < 5:
        errors['title'] = 'The title must be 5 characters or more'

    if len(request.form['content']) < 20:
        errors['content'] = 'The content must have 20 characters or more'

    if errors:
        return render_template('post_template.html', error=errors)

    post_model = Post(db)
    post_model.save_post({'title': request.form['title'], 'content': request.form['content']})
    return redirect(url_for('default'))

@app.route('/post/edit/<post_id>')
def edit_post(post_id):
    post_model = Post(db)
    return render_template(
        'post_template.html',
        post=post_model.get_single_post(post_id),
        action='/post/process-edit-post',
        title='Edit Post'
    )

@app.route('/post/process-edit-post', methods=['POST'])
def process_edit_post():
    post_model = Post(db)
    post_model.save_post({
        'title': request.form['title'],
        'content': request.form['content'],
        '_id': ObjectId(request.form['_id'])
    })
    return redirect(url_for('default'))

@app.route('/post/process-delete-post', methods=['POST'])
def process_delete_post():
    post_model = Post(db)
    post_model.remove_post(request.form['_id'])
    return redirect(url_for('default'))