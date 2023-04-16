from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from core.celery import debug_task
# Create your views here.
from .tasks import print_something

User = get_user_model()
@login_required
def home(request):
    # print_something().delay()
    current_user = request.user
    following = current_user.following
    # print(following)
    followers = current_user.followers
    context = {
        'follower': followers,
        'following': following
    }

    return render(request, 'index.html', context)


def add_instagram(request):
    current_user = User.objects.get(email__exact=request.user.email)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        browser = webdriver.Chrome()

        browser.implicitly_wait(1)

        browser.get('https://www.instagram.com/')

        sleep(1)

        username_input = browser.find_element(By.CSS_SELECTOR,"input[name='username']" )
        password_input = browser.find_element(By.CSS_SELECTOR,"input[name='password']" )

        username_input.send_keys(username)
        password_input.send_keys(password)


        login_button = browser.find_element(By.XPATH , "//button[@type='submit']")
        login_button.click()
        sleep(10)
        browser.get(f'https://www.instagram.com/{username}')
        

        # browser.find_element(By.XPATH,"//*[@id='mount_0_0_xl']/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
        # print('not now clikced')
        # browser.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()


        
        follower_count = int(browser.find_element(By.XPATH,".//*[contains(text(), 'followers')]/span").text)
        following_count = int(browser.find_element(By.XPATH, ".//*[contains(text(), 'following')]/span").text)
        current_user.followers = follower_count
        current_user.following = following_count
        current_user.save()
        
        print(follower_count, '-----------------------', following_count)



        # print('fiolll;', follower_count)
        # sleep(5)

        browser.close()
        return redirect(reverse_lazy('account:home'))
    # update_instagram_counts.apply_async(args=[current_user.email], countdown=1)





    return render(request, 'instagram.html')

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

def login(request):
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                django_login(request, user)
                print('looged in')
                messages.success(request, 'Siz ugurla login oldunuz')
                return redirect(reverse_lazy('account:home'))
            else:
                messages.success(request, 'Siz login ola bilmediniz')
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data =request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password = form.cleaned_data.get('password1')
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            messages.success(request, 'Siz ugurla qeydiyyatdan kecdiniz')
            return redirect(reverse_lazy('account:login'))
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)
