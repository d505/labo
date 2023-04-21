from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#ForeignKeyとoneTooneはここ見ればいい
# https://note.com/shinya_hd/n/n240c3613b60f

# ユーザーアカウントのモデルクラス
class Account(models.Model):
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Userにも保存されている。
    #追加の部分がAccountのテーブルに保存されている。
    def __str__(self): #管理画面で見るときに役に立つ。
        return self.user.username
    

class TemplateSelect(models.Model):

    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    image = models.ImageField(upload_to="profile_pics",blank=True)
    room = models.CharField(max_length=100)#研究室
    professor = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    url = models.URLField(max_length=1000,blank=True)

    def __str__(self):
        return f'{self.faculty}_{self.department}'


SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Review(models.Model):
   # lab_id = models.ForeignKey(TemplateSelect,on_delete=models.CASCADE)
    lab_id = models.CharField('研究室ID', max_length=10, blank=False)
    lab_name = models.CharField('研究室名', max_length=200, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='レビューコメント', blank=False)
    score1 = models.PositiveSmallIntegerField(verbose_name='担当教授の干渉度', choices=SCORE_CHOICES, default='3')
    score2 = models.PositiveSmallIntegerField(verbose_name='先輩・後輩との関わり', choices=SCORE_CHOICES, default='3')
    score3 = models.PositiveSmallIntegerField(verbose_name='研究室の設備', choices=SCORE_CHOICES, default='3')
    score4 = models.PositiveSmallIntegerField(verbose_name='学会などのレベル', choices=SCORE_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user','lab_id'],
                name="lab_unique"
            ),
        ]

    def __str__(self):
        return str(self.lab_id)

    def get_percent(self):
        percent1 = round(self.score1 / 5 * 100)
        percent2 = round(self.score2 / 5 * 100)
        percent3 = round(self.score3 / 5 * 100)
        percent4 = round(self.score4 / 5 * 100)
        return percent1,percent2,percent3,percent4
    
    def get_comment(self):
        return self.comment
    


        


