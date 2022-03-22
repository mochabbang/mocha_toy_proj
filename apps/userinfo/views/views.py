from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import LoginForm
from ..models import UserInfo
from common.sql_helper import SqlHelper
from common.convert_model import ModelMapper

# Create your views here.
def login(request):
    sql_helper = SqlHelper()
    model_mapper = ModelMapper()
    userdata = None

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            userid = login_form.cleaned_data['userid']
            password = login_form.cleaned_data['password']

            if request.COOKIES.get('userinfo'):
                return redirect('freeboard/')

            parameters = (userid, password)
            userdata = sql_helper.get_data_list('[dbo].[USP_FREEBOARD_USERINFO_TB_SEL] @USERID=%s, @PASSWORD=%s', parameters)
            userinfo = [model_mapper.make_instance(UserInfo(), item) for item in userdata]

            if userinfo is not None:
                response = redirect('freeboard/')
                response.set_cookie('userinfo', userinfo)
                return response
    else:
        login_form = LoginForm()

    return render(request, 'userinfo/login_form.html', {
        'login_form': login_form
    })