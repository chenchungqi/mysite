from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse

import user.models
from .forms import LoginForm, RegForm


# def login(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             user = login_form.cleaned_data['user']
#             auth.login(request, user)
#             return redirect(request.GET.get('from', reverse('home')))
#     else:
#         login_form = LoginForm()
#
#     context = {}
#     context['login_form'] = login_form
#     return render(request, 'user/login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']

            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def user_info(request):
    context = {}
    user = request.user
    # print(user.profile.studyInfo)
    s_info = user.profile.studyInfo
    #s_info = '七年级上册Unit3: 单词记忆25，生词2，熟词13，夹生词10，未学完0。;七年级上册Unit2: 单词记忆15，生词2，熟词13，夹生词10，未学完0。'
    s_info_list =s_info.split(';')
    # print(s_info_list)
    # llist = []
    # for each in s_info_list:
    #     aa =each.split('：')
    #     llist.append(aa)
    # print(llist)

    daily_scores_str = user.profile.daily_scores
    str_list = daily_scores_str.split(',')
    daily_scores_list = list(map(int, str_list))

    daily_units_str = user.profile.daily_units
    str_list2 = daily_units_str.split(',')
    daily_units_list = list(map(int, str_list2))


    context['daily_scores_list'] = daily_scores_list
    context['daily_units_list'] = daily_units_list
    context['studyInfo'] = s_info_list
    return render(request, 'user/user_info.html', context)


def group_info(request):
    context = {}
    return render(request, 'user/group_info.html', context)
