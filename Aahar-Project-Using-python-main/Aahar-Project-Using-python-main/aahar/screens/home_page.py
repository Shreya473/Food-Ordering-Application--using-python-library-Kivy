import json
from kivymd.uix.screen import MDScreen
from libs.components.postcard import PostCard


class HomePage(MDScreen):
    profile_picture = 'C:/Users/shreya jadhav/Desktop/aahar/assets/images/profile.jpg'

    def on_enter(self):
        self.list_posts()

    def list_posts(self):
        with open('assets/data/post.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username=username,
                    avatar=data[username]['avatar'],
                    profile_pic=self.profile_picture,
                    post=data[username]['post'],
                    posted_ago=data[username]['posted_ago']
                ))
