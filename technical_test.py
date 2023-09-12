"""
Technical Test: Senior Software Developer - Python & Django

Complete the code tasks below. Remember to consider best practices and the principles of clean, efficient code.

Your code will be evaluated based on correctness, efficiency, readability, and best practices.
"""

# 1. Python Fundamentals

# 1.1. Complete the function below.
def max_repeat(numbers):
    filtered_res = (0,0)
    
    for index, x in enumerate(numbers):
        max_freq = 0
        most_frequent_digit = x % 10
        
        while x > 0:
            digit = x % 10
            count = 0
            temp = x
            while temp > 0:
                if temp % 10 == digit:
                    count += 1
                temp //= 10
            if count > max_freq:
                max_freq = count
                most_frequent_digit = digit
            x //= 10
        res = (max_freq, most_frequent_digit, index)
        
        if res[0] > filtered_res[0]:
            filtered_res = res
        
    return numbers[filtered_res[2]]

assert max_repeat([123, 1123, 332, 4445, 5566]) == 4445
print(max_repeat([123, 1123, 332, 4445, 5566]))


# 2. Django Fundamentals

# Assuming you have Django environment set up:

# 2.1. Create a Django model for a `BlogPost`.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    # TODO: Define title, content, publish_date, and author fields here
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 3. Django ORM & Databases

# 3.1. Given the BlogPost model above, retrieve all BlogPosts written by a User with username 'john_doe'.
# Write the query below:

posts_by_john = BlogPost.objects.filter(author__username="john_doe")

# 3.2. Optimize the following view function for better performance:

def get_latest_posts(request):
    # posts = BlogPost.objects.all().order_by('-publish_date')[:10]
    posts = BlogPost.objects.order_by('-publish_date')[:10]
    # TODO: Optimize the above line for better performance.
    return render(request, 'latest_posts.html', {'posts': posts})


# 4. Django Forms & Validation

from django import forms

# 4.1. Create a Django form for submitting a BlogPost.

class BlogPostForm(forms.ModelForm):
    # TODO: Ensure title is not more than 200 characters and content is not empty.
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea, required=True)
    publish_date = forms.DateTimeField(required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'publish_date', 'author']


# 5. Advanced Django Topics

# 5.1. Implement a Django middleware to record the response time of every request.

from datetime import datetime
from django.http import HttpResponse

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        response = self.get_response(request)
        # TODO: Calculate and print response time for the request.
        response_time = datetime.now() - start_time
        print(response_time)
        return HttpResponse(response)


# 6. Practical Application

# 6.1. Using the Django ORM, write a function that returns the title of the most recent BlogPost.

def get_latest_blog_title():
    post = BlogPost.objects.last().values('title')

    return post
# Test your function
# assert get_latest_blog_title() == "Your most recent blog's title"
