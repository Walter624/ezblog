from core import Model
from bson.objectid import ObjectId


class Post(Model):
    def get_all_posts(self):
        return self.db.posts.find()

    def get_single_post(self, id):
        return self.db.posts.find_one({'_id': ObjectId(id)})

    def save_post(self, data):
        return self.db.posts.save(data)

    def remove_post(self, id):
        return self.db.posts.remove({'_id': ObjectId(id)})