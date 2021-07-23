from django.forms import ModelForm
from .models import Post

# form for post
class Add_Post(ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','category','summary','content','draft']

