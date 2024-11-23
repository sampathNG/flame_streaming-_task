from mongoengine import Document, StringField, EmailField, DateTimeField, ListField,ReferenceField
import datetime
class User(Document):
    username = StringField(required=True, unique=True, max_length=50)
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)
    gender = StringField(max_length=10)
    dateofbirth = DateTimeField()
    languages = ListField(StringField(max_length=50))
    homeTown = StringField(max_length=100)
    bio = StringField(max_length=500)
    following = ListField(StringField(max_length=50))  # List of usernames the user is following
    followers = ListField(StringField(max_length=50))  # List of usernames who follow the user
    likes = ListField(StringField(max_length=50))  # List of item IDs liked by the user
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    def __str__(self):
        return self.username
    
    def get_friends(self):
        return Friends.objects(user=self)   
class Friends(Document):
    fullname = StringField(required=True, max_length=50)
    active = StringField(max_length=10,default='not active')
    follow = StringField(max_length=50,default='unfollow')
    user = ReferenceField(User, required=True)
    def __str__(self):
        return self.fullname
