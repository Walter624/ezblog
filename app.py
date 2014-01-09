from flask import Flask, render_template, request, redirect, url_for
import pymongo
import git

app = Flask(__name__)

@app.route('/')
def default():
    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    posts = db.posts.find()
    return render_template("default.html", posts=posts)

@app.route('/post/create')
def create_post():
    return render_template('create_post.html')

@app.route('/post/process-create-post', methods=['POST'])
def process_create_post():
    errors = {}
    if len(request.form["title"]) < 5:
        errors['title'] = 'The title must be 5 characters or more'

    if len(request.form['content']) < 20:
        errors['content'] = 'The content must have 20 characters or more'

    if errors:
        return render_template('create_post.html', error=errors)

    mongo_client = pymongo.MongoClient("localhost", 27017)
    db = mongo_client.ezblog
    db.posts.save({'title': request.form['title'], 'content': request.form['content']})
    return redirect(url_for('default'))

    repo = Repo.init("/usr/", bare=True)
    assert repo.bare == True
    repo.commit()

if __name__ == '__main__':
    app.run(debug=True)