import os
import pandas as pd
from django.db import IntegrityError
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView #テンプレートタグ
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db import models
from django.contrib.auth.models import User
from .name_list import NAME_LIST
from .models import TemplateSelect, Review, UserProfile,Topics
from .forms import AccountForm, ReviewForm, CustomUserChangeForm,CreateTopicForm,DeleteTopicForm,PostTextForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib import messages
from django.http import Http404
from .models import Topics, Texts



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
class  ReviewLabolatory(MyCustomMixin,TemplateView):

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
        try:
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

        except IntegrityError:
            # フォームが有効でない場合
            print(self.params["lab_form"].errors)
            return redirect(reverse('doubleac'))  

        return render(request,"App_Folder_HTML/review.html",context=self.params)

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
    
    name = f'{faculty}{department}'

    # params = {'name':name,'labo_name':labo_name_list}
    params = {'name':name,'lab':faculty_and_department}

    return render(request,f"faculty_and_department/base1.html",context=params)

def detail(request):
    lab_id = request.POST.get('labid')
    reviews = Review.objects.filter(lab_id=lab_id)
    number = Review.objects.filter(lab_id=lab_id).count()
    try:
        percent = [0, 0, 0, 0]
        comment = []
        for review in reviews:
            percent = [x + y for x,y in zip(percent, review.get_percent())]
            comment.append(review.get_comment())
        percent = [int(n/number) for n in percent]
        params = {'labid': lab_id,'review1':percent[0],'review2':percent[1],'review3':percent[2],'review4':percent[3],'comment':comment}
        return render(request,"faculty_and_department/detail.html",context = params)
    except ZeroDivisionError:
        return redirect(reverse('noreview'))

def logno(request):
    return render(request,"App_Folder_HTML/logno.html")

def doubleac(request):
    return render(request,"App_Folder_HTML/doubleac.html")

def noreview(request):
    return render(request,"App_Folder_HTML/noreview.html")

def chathome(request):
    return render(request, "chat/chathome.html")

def chatroom(request,room_name):
    return render( request, 'chat/chatroom.html',{"room_name": room_name})

@login_required
def profile(request):
    return render(request, 'profile/profile.html', {'user_profile': request.user})

@login_required
def profile_anke(request):
    user_answer = Review.objects.filter(user_id=request.user.id)
    return render(request, 'profile/profile_anke.html', {'an': user_answer})

@login_required
def profile_update(request):
    user_profile = request.user
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile')) 
    else:
        form = CustomUserChangeForm()
    
    return render(request, 'profile/profile_update.html', {'form': form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        request.user.is_active = False
        request.user.save()
        logout(request)  
        return redirect(reverse('home')) 
    return render(request, 'profile/profile_delete.html')  


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'profile/password_change_done.html' 


def board_create(request):
    create_topic_form = CreateTopicForm(request.POST or None)
    if create_topic_form.is_valid():
        create_topic_form.instance.user = request.user
        create_topic_form.save()
        return redirect(reverse('board_list'))
    
    return render(request, 'board/board_create.html', context={'create_topic_form': create_topic_form})

def board_list(request): 
    topics = Topics.objects.all()
    return render(request, 'board/board_list.html', context={'topics': topics})

def board_edit(request, id):
    topic = get_object_or_404(Topics, id=id)
    if topic.user.id != request.user.id:
        raise Http404
    edit_topic_form = CreateTopicForm(request.POST or None, instance=topic)
    if edit_topic_form.is_valid():
        edit_topic_form.save()
        return redirect(reverse('board_list'))
    return render(request, 'board/board_edit.html',context={'edit_topic_form': edit_topic_form,'id': id})

def board_delete(request, id): 
    topic = get_object_or_404(Topics, id=id)
    if topic.user.id != request.user.id:
        raise Http404
    delete_topic_form = DeleteTopicForm(request.POST or None)
    if delete_topic_form.is_valid():
        topic.delete()
        return redirect(reverse('board_list'))
    return render(request, 'board/board_delete.html', context={'delete_topic_form': delete_topic_form})

def board_post_texts(request, topic_id):
    post_text_form = PostTextForm(request.POST or None)
    topic = get_object_or_404(Topics, id=topic_id)
    texts = Texts.objects.pick_by_topic_id(topic_id) 
    if post_text_form.is_valid():
        post_text_form.instance.topic = topic
        post_text_form.instance.user = request.user
        post_text_form.save()
        return redirect('board_post_texts', topic_id=topic_id)
    return render(request, 'board/board_post_texts.html', context={'post_text_form': post_text_form,'topic': topic,'texts': texts,})