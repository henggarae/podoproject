from django import forms
from .models import User,Post

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','rank']
    def signup(self,request,user):
        user.name = self.cleaned_data['name']
        user.rank = self.cleaned_data['rank']

        user.save()
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'platoon_member',
            'platoon_member_rank',
            'content',
        ]
        #widgets = {
        #    'item_condition': forms.RadioSelect,
        #}