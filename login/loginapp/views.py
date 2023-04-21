import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView #テンプレートタグ
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .name_list import NAME_LIST
from .models import TemplateSelect, Review
from .forms import AccountForm, ReviewForm #ユーザーアカウントフォーム


from django.contrib.auth.mixins import UserPassesTestMixin

class MyCustomMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(reverse('logno'))
#ログイン
#ログインの返答もこの関数を呼ぶ。
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'App_Folder_HTML/login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('home'))


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        # "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        # self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"App_Folder_HTML/register.html",context=self.params)

    #Post処理
    def post(self,request):
      
        self.params["account_form"] = AccountForm(data=request.POST)
       
        # self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save(commit=False)
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()
            

            # # 下記追加情報
            # # 下記操作のため、コミットなし
            # add_account = self.params["add_account_form"].save(commit=False)
            # # AccountForm & AddAccountForm 1vs1 紐付け
            # add_account.user = account

            # # 画像アップロード有無検証
            # if 'account_image' in request.FILES:
            #     add_account.account_image = request.FILES['account_image']

            # # モデル保存
            # add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"App_Folder_HTML/register.html",context=self.params)
    

#研究室の評価
class  ReviewLabolatory(MyCustomMixin, TemplateView):

    def __init__(self):
        self.params = {
        "LabCreate":False,
        "lab_form": Review(),
        }

    #Get処理
    
    def get(self,request):
        self.params["lab_form"] = ReviewForm()
        self.params["LabCreate"] = False
        return render(request,"App_Folder_HTML/review.html",context=self.params)
        
    #Post処理
   
    def post(self,request):
        labid = request.GET.get('labid')
        labname = request.GET.get('labname')
        self.params["lab_form"] = ReviewForm(data= request.POST)

        #フォーム入力の有効検証
        if self.params["lab_form"].is_valid():
            # アカウント情報をDB保存
            lab = self.params["lab_form"].save(commit=False)
            lab.lab_id = labid
            lab.lab_name = labname
            lab.user = request.user
            # # パスワードをハッシュ化
            # lab.set_password(lab.password)
            # # ハッシュ化パスワード更新
            lab.save()

            # アカウント作成情報更新
            self.params["LabCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["lab_form"].errors)

        return render(request,"App_Folder_HTML/review.html",context=self.params)
        # return print(self.params)

#ホーム
def home(request):
    params = {"UserID":request.user,}
    if request.method == 'POST':
      
        faculty_name = request.POST.get('学部')
        department_name = request.POST.get('学科')
        name = f"{faculty_name}_{department_name}"

        if name in NAME_LIST:     
        #,faculty=faculty_name,department=department_name  
            return redirect(facaluty_department,faculty=faculty_name,department=department_name)
        
    return render(request, "App_Folder_HTML/home.html",context=params)


def facaluty_department(request,faculty,department):
    
    # faculty_and_department = TemplateSelect.objects.filter(faculty=faculty,department=department).first()
    # labo_name_list= faculty_and_department.room.split(',')
    # print(labo_name_list)

    # params = {'name':faculty_and_department,'labo_name':labo_name_list}
    faculty_and_department = TemplateSelect.objects.filter(faculty=faculty,department=department).all()
    name = f'{faculty}_{department}'

    # params = {'name':name,'labo_name':labo_name_list}
    params = {'name':name,'lab':faculty_and_department}

    return render(request,f"faculty_and_department/base1.html",context=params)

def detail(request):
    lab_id = request.POST.get('labid')
    reviews = Review.objects.filter(lab_id=lab_id)
    percent = [0, 0, 0, 0]
    for review in reviews:
        percent = [x + y for x,y in zip(percent, review.get_percent())]
    params = {'labid': lab_id,'reviews':percent}
    print(percent)
    return render(request,"faculty_and_department/detail.html",context = params)

def logno(request):
    return render(request,"App_Folder_HTML/logno.html")
