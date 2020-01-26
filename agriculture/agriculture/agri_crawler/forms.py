from django import forms
from django.contrib.auth.models import User
from .models import UploadFileModel
from .models import Document
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'password','email']
#def min_length_3_validator(value):
#       if len(value) < 3:
#          raise forms.ValidationError('3글자 이상 입력해주세요')
        
class UploadFileForm(forms.ModelForm):
   class Meta:
      model = UploadFileModel
      fields = ('title', 'file')
   def __init__(self, *args, **kwargs):
      super(PostForm, self).__init__(*args,**kwargs)
      self.fields['file'].required = False
class DocumentForm(forms.ModelForm):
    class Meta:
       model = Document
       fields = ('file', )
