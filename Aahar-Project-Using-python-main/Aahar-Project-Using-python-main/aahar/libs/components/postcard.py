from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


class PostCard(MDCard):
    profile_pic = StringProperty()
    username = StringProperty()
    post = StringProperty()
    posted_ago = StringProperty()
