from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        #   create a user
        testuser1 = User.objects.create_user(username='testuser1', password='123')
        testuser1.save()

        #   create a blog post
        testpost = Post.objects.create(author=testuser1, title='This made by a test user', body='This is a body content that made by test user...')
        testpost.save()
        
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'This made by a test user')
        self.assertEqual(body, 'This is a body content that made by test user...')
