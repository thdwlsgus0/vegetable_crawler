# Create your models here.
from djongo import models
from django import forms
from django.contrib.auth.models import User
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')
class Signup(models.Model):
    ID = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
   
class Emoticon(models.Model):
    like = models.CharField(max_length=100)
    warm = models.CharField(max_length=100)
    sad = models.CharField(max_length=100)
    angry = models.CharField(max_length=100)
    want = models.CharField(max_length=100)
    class Meta:
        abstract = True
class Document(models.Model):
   description = models.CharField(max_length=255, blank=True)
   file =  models.FileField(upload_to = 'webapp/')
   uploaded_at = models.DateTimeField(auto_now_add=True)
class EmoticonForm(forms.ModelForm):
    class Meta:
        model = Emoticon
        fields = (
            'like','warm','sad','angry','want'
        )
class Twitter(models.Model):
    userId = models.CharField(max_length=200, null=True)
    Id= models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
class UploadFileModel(models.Model):
   title = models.TextField(default='')
   file = models.FileField(null=True)
class title(models.Model):
    media = models.CharField(max_length=200, null=True)
    main_title = models.CharField(max_length=200, null=True)
    datetime = models.CharField(max_length=200, null=True)
    main_body = models.CharField(max_length=12000, null=True)
    count = models.FloatField(max_length=200, null=True)
    class Meta:
        abstract = True
class titleForm(forms.ModelForm):
    class Meta:
        model = title
        fields = (
           'media', 'main_title', 'datetime', 'main_body', 'count'
        )
class media_count(models.Model):
   kbs_count = models.CharField(max_length=200, null=True)
   mbc_count = models.CharField(max_length=200, null=True)
   sbs_count = models.CharField(max_length=200, null=True)
   jtbc_count = models.CharField(max_length=200, null=True)
   ytn_count = models.CharField(max_length=200, null=True)
   money_count = models.CharField(max_length=200, null=True)
   edaily_count = models.CharField(max_length=200, null=True)
   korea_count = models.CharField(max_length=200, null=True)
   dailyeconomy_count = models.CharField(max_length=200, null=True)
   seouleconomy_count = models.CharField(max_length=200, null=True)
   naver_count = models.CharField(max_length=200, null=True)
   daum_count = models.CharField(max_length=200, null=True)
   twitter_count = models.CharField(max_length=200, null=True)
   class Meta:
       abstract = True
class media_countForm(forms.ModelForm):
    class Meta:
        model = media_count
        fields ={
            'kbs_count', 'mbc_count', 'sbs_count', 'jtbc_count','ytn_count', 'money_count', 'edaily_count'
            ,'korea_count','dailyeconomy_count','seouleconomy_count','naver_count','daum_count','twitter_count'
        }
class news_count(models.Model):
    login_id = models.CharField(max_length=200, null=True)
    kbs_count = models.CharField(max_length=200, null=True)
    mbc_count = models.CharField(max_length=200, null=True)
    sbs_count = models.CharField(max_length=200, null=True)
    jtbc_count = models.CharField(max_length=200, null=True)
    ytn_count = models.CharField(max_length=200, null=True)
    money_count = models.CharField(max_length=200, null=True)
    edaily_count = models.CharField(max_length=200, null=True)
    korea_count = models.CharField(max_length=200, null=True)
    dailyeconomy_count = models.CharField(max_length=200, null=True)
    seouleconomy_count = models.CharField(max_length=200, null=True)
class naver_count(models.Model):
    login_id = models.CharField(max_length=200, null=True)
    naver_count = models.CharField(max_length=200, null=True)
class daum_count(models.Model):
    login_id = models.CharField(max_length=200, null=True)
    daum_count = models.CharField(max_length=200, null=True)
class twitter_count(models.Model):
    login_id = models.CharField(max_length=200, null=True)
    twitter_count = models.CharField(max_length=200, null=True)
class blogtitle(models.Model):
      main_title = models.CharField(max_length=200)
      main_body = models.CharField(max_length=200)
      datetime = models.CharField(max_length=12000)
      class Meta:
        abstract = True
class word(models.Model):
      user_id = models.CharField(max_length=200, null=True)
      key = models.CharField(max_length=200, null=True)
      value = models.CharField(max_length=200, null=True)
class blogForm(forms.ModelForm):
       class Meta:
           model = blogtitle
           fields = (
           'main_title','main_body','datetime'
           )
class daum_blog(models.Model):
    keyword = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=100, null=True)
    sub_body = models.EmbeddedModelField(
       model_container = title,
       model_form_class= titleForm
  )
    tag = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=10000, null= True)
class KBS(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class= titleForm
    )
class user_data(models.Model):
    ID = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class = titleForm
    )
class state1(models.Model):
    login_id = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    today_date = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True)
    type_state = models.CharField(max_length=100, null=True)

class MBC(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class = titleForm
    )

class SBS(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class = titleForm
    )


class JTBC(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class YTN(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class dailyEconomy(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class moneyToday(models.Model):
    keyword = models.CharField(max_length=130, null= True)
    nickname=models.CharField(max_length=130,null=True)
    sub_body= models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class eDaily(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname=models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class seoulEconomy(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname=models.CharField(max_length=130,null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class koreaEconomy(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname=models.CharField(max_length=130,null=True)
    sub_body = models.EmbeddedModelField(
        model_container=title,
        model_form_class=titleForm
    )

class naver(models.Model):
    keyword = models.CharField(max_length=130, null=True)
    nickname = models.CharField(max_length=130, null=True)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class=titleForm
    )
    main_url = models.CharField(max_length=130, null=True)

class daum(models.Model):
    keyword = models.CharField(max_length=130)
    sub_body = models.EmbeddedModelField(
        model_container = title,
        model_form_class=titleForm
    )

