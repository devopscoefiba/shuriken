from mongoengine import Document, SequenceField, MultiLineStringField


class Post(Document):
    post_id = SequenceField(primary_key=True)
    json_value = MultiLineStringField()
    # meta = {'collection': 'posts'}
