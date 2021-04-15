from django.test import TestCase
from pigeonpost.models import Post, Comments, Like
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from pigeonpost.forms import NewPostForm, NewCommentForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test.utils import override_settings
import tempfile
import shutil

MEDIA_ROOT = tempfile.mkdtemp()

class LoginForceTest(TestCase):

    def test_loginSetUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

#Testing Login Functionality
class LoginFunctionalityTest(TestCase):

#Setting up a test User
    def setUp(self):
        print("Testing Login")
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        User.objects.create_user(**self.credentials)

#Verifying that we are using the right template
    def test_loginTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

#Attempting a login and verifying that we are authenticated
    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)     
        self.assertTrue(response.context['user'].is_authenticated)
        
#Attempting a login with a bad password and verifying that it does not authenticate
    def test_badLogin(self):
        response = self.client.post('/login/', {'username':'testuser','password':'wrongpassword'}, follow=True)     
        self.assertFalse(response.context['user'].is_authenticated)        

class PostModel(TestCase):

    def setUp(self):
        print("Testing Post Model")
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        username= User.objects.create_user(**self.credentials)
        self.post = Post.objects.create(description="test123",user_name=username)

#Verifying that the contents of the post is what we set it to        
    def test_create(self):
        self.assertEqual(str(self.post),"test123")
        
class CommentModel(TestCase): 

    def setUp(self):
        print("Testing Comment Model")   
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        username= User.objects.create_user(**self.credentials)
        post = Post.objects.create(description="test123", user_name=username)
        self.comment = Comments.objects.create(post=post, comment="testcomment123", username=username)

#Verifying that the contents of the comment is correct     
    def test_create(self):
        self.assertEqual(self.comment.comment,"testcomment123")
        
class LikeModel(TestCase): 

    def setUp(self):
        print("Testing Like Model")   
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        username= User.objects.create_user(**self.credentials)
        self.post = Post.objects.create(description="test123", user_name=username)
        self.like = Like.objects.create(post=self.post, user=username)

#Verifying that the like is properly associated to the right post        
    def test_create(self):
        self.assertEqual(self.like.post, self.post)
        
@override_settings(MEDIA_ROOT=MEDIA_ROOT)        
class NewPostFormTest(TestCase):

#Creating a dummy image to test
    def setUp(self):
        print("Testing New Post Form") 
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
       
        form_data={'description':'testdescription123','tags':'testtags'}
        file_data={'pic':uploaded}
        self.form = NewPostForm(data=form_data, files=file_data)

#Verifying that our form is valid        
    def test_formValid(self):
        self.assertTrue(self.form.is_valid())
        
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()        
        
class NewCommentFormTest(TestCase):
    
    def setUp(self):
        print("Testing New Comment Form")   
        form_data ={'comment':'testcomment'}
        self.form = NewCommentForm(data=form_data)

#Verifying that our form is valid         
    def test_create(self):
        self.assertTrue(self.form.is_valid())

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PostListViewTest(TestCase):

#Creating Dummy User Posts
    def setUp(self):
        print("Testing Post List View")  
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
       
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        username= User.objects.create_user(**self.credentials)
        for i in range(10):
            Post.objects.create(description="test123",user_name=username, pic=uploaded)
        self.response = self.client.get(reverse('home'))

#Verifying that we are redirected to a valid page    
    def test_create(self):
        self.assertEqual(self.response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)    
class UserPostListViewTest(TestCase):

#Creating Dummy User Posts
    def setUp(self):
        print("Testing User Post List View")  
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')
       
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'}
        username= User.objects.create_user(**self.credentials)
        for i in range(10):
            Post.objects.create(description="test123",user_name=username, pic=uploaded)
        self.response = self.client.post(reverse('user-posts', args=['testuser']), follow=True)

#Verifying that we are redirected to a valid page        
    def test_create(self):
        self.assertEqual(self.response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()
