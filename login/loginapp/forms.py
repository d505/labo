from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Review,Topics, Texts




# フォームクラス作成
#書き換える場合フィールド書けばいい。
class AccountForm(forms.ModelForm):
    # Userの上書き
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User #モデルに合わせてフォームが作成される。つまり、自分でフィールド設定しなくていいことだと思う。
        # フィールド指定 画面上に表示される
        fields = ('username','email','password')
        # フィールド名指定　
        labels = {'username':"ユーザーID",'email':"メール"}

# class AddAccountForm(forms.ModelForm):
#     class Meta():
#         # モデルクラスを指定
#         model = Account
#         #fields = ('last_name','first_name','account_image',)
#         fields = ('account_image',)
#         labels = {'account_image':"写真アップロード",}


class ReviewForm(forms.ModelForm):   
    class Meta:
        model = Review
        fields = ['score1','score2','score3','score4', 'comment']
        # フィールド名指定
        labels = {'score1':'担当教授の干渉度',
                  'score2':'先輩・後輩との関わり',
                  'score3':'研究室の設備',
                  'score4':'学会のレベル', 
                  'comment':'コメント',
                  }


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)

    class Meta:
        model = User
        fields = ['username','email']
        labels = {'username':'ユーザー名','email':'メールアドレス'}


class CreateTopicForm(forms.ModelForm):
    title = forms.CharField(label='Title')

    class Meta:
        model = Topics
        fields = ('title',)

class DeleteTopicForm(forms.ModelForm):

    class Meta:
        model = Topics
        fields = []

class PostTextForm(forms.ModelForm): 
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':5,'cols':50}))
    
    class Meta:
        model = Texts
        fields = ('text',)