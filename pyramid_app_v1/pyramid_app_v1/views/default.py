

from gotrue.types import Provider
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from ..db import base


@view_config(route_name='home', renderer='pyramid_app_v1:templates/mytemplate.jinja2')
def home_view(request):
    colors = ["black", "white", "yellow", "orange", "red", "purple", "magenta", "green", "teal", "blue"]

    users = base.auth.api.list_users()
  
    return {'users':users,'colors':colors}  



@view_config(route_name='register', renderer='pyramid_app_v1:templates/register.jinja2')
def register_view(request):
    if request.base is not  None:
        return HTTPFound(location=request.route_url('home'))

    if request.method == 'GET':
        return {}

    if request.method == 'POST':    
        email = request.POST['email']
        password = request.POST['password'] 
        try:   
            base.auth.sign_up(email=email,password=password)
            return HTTPFound(request.route_url('login'))
        except Exception as e:
             return {'error': e}   
       


@view_config(route_name='login', renderer='pyramid_app_v1:templates/login.jinja2')
def login_view(request):
    if request.base is not  None:
        return HTTPFound(location=request.route_url('home'))
    response = request.response
    if request.method == 'GET':
        return {}
    if request.method == 'POST':    
        email = request.POST['email']
        password = request.POST['password'] 
        try:
            user = base.auth.sign_in(email=email,password=password)
            response.set_cookie('jwt',user.access_token)   # type: ignore
            url = request.route_url('home') 
            return HTTPFound(location=url,headers=response.headers)
        except Exception as e:
            return {'error':e}    
       
       
@view_config(route_name='logout')
def logout_view(request):
    response = request.response
    base.auth.sign_out()
    response.delete_cookie('jwt')
    url = request.route_url('home') 
    return HTTPFound(location=url,headers=response.headers)


@view_config(route_name='auth')
def auth_(request):
    url = request.route_url('home')
    return HTTPFound(location=url )

@view_config(route_name='refresh')
def recover_(request):
    url = request.route_url('reset_password')
    return HTTPFound(location=url )       


@view_config(route_name='login_github')
def login_with_github_view(request):
    response=request.response
    url = base.auth.sign_in(provider= Provider.github)
    return HTTPFound(location=str(url),headers=response.headers)

@view_config(route_name='login_discord')
def login_with_discord_view(request):
    response=request.response
    url = base.auth.sign_in(provider= Provider.discord)
    return HTTPFound(location=str(url),headers=response.headers) 

@view_config(route_name='login_google')
def login_with_google_view(request):
    response=request.response
    url = base.auth.sign_in(provider= Provider.google)
    return HTTPFound(location=str(url),headers=response.headers) 


@view_config(route_name='forgot_password',renderer='pyramid_app_v1:templates/forgot_password.jinja2')
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        url = "http://localhost:6543/reset_password"
        try:
            base.auth.api.reset_password_for_email(email=email,redirect_to=url)
            return HTTPFound(location=request.route_url('home'))
        except Exception as e:
            ...    
    return {}  

@view_config(route_name='reset_password',renderer='pyramid_app_v1:templates/reset_password.jinja2')
def reset_password_view(request):
    if request.base is None:
        return HTTPFound(location=request.route_url('login'))
    if request.method == 'POST':
        password = request.POST['password']
        try:
            base.auth.update(attributes={'password':password})
            return HTTPFound(location=request.route_url('home'))
        except Exception as e:
            ...    
    return {}    



@view_config(route_name='profile',renderer='pyramid_app_v1:templates/profile.jinja2')
def profile_view(request):
    colors = ["black", "white", "yellow", "orange", "red", "purple", "magenta", "green", "teal", "blue"]
    if request.base is None:
        return HTTPFound(location=request.route_url('login'))
    if request.method == 'POST':
        color = request.POST['color']
        try:
            base.auth.update(attributes={'data':{'fav_color':color}})
            return HTTPFound(location=request.route_url('profile'))
        except Exception as e:
            ...        
    return {'colors':colors}                
    
        



