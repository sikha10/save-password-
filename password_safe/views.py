from django.shortcuts import render, redirect, HttpResponse
from .models import Profile_info, Saved_info
from cryptography.fernet import Fernet


def register(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        key = Fernet.generate_key()
        crypter = Fernet(key)
        enc_name = crypter.encrypt(name.encode())
        enc_password = crypter.encrypt(password.encode())
        objs = Profile_info.objects.all()
        is_prime = True
        for obj in objs:
            if obj.key:
                cut_key = obj.key[2:-1:] 
                cut_name = obj.name[2:-1:] 
                cut_password = obj.password[2:-1:]
                b_key = bytes(cut_key, encoding='utf-8')
                b_name = bytes(cut_name, encoding='utf-8')
                b_password = bytes(cut_password, encoding='utf-8')
                crypter = Fernet(b_key)
                dec_name = crypter.decrypt(b_name)
                dec_password = crypter.decrypt(b_password)
                if str(dec_name)[2:-1:] == name and str(dec_password)[2:-1:] == password:
                    print('eseti aris ukve')
                    is_prime = False  
        if is_prime:     
            Profile_info.objects.create(name=enc_name, password=enc_password, key=key)
        else:
            return HttpResponse("user or passwors is already in use")

    return render(request, 'login.html')

def checklogin(request):
    if request.method == 'POST':
        name = request.POST.get('name3')
        password = request.POST.get('password3')
        objs = Profile_info.objects.all()
        is_prime = False
        for obj in objs:
            if obj.key:
                cut_key = obj.key[2:-1:] 
                cut_name = obj.name[2:-1:] 
                cut_password = obj.password[2:-1:]
                b_key = bytes(cut_key, encoding='utf-8')
                b_name = bytes(cut_name, encoding='utf-8')
                b_password = bytes(cut_password, encoding='utf-8')
                crypter = Fernet(b_key)
                dec_name = crypter.decrypt(b_name)
                dec_password = crypter.decrypt(b_password)
                if str(dec_name)[2:-1:] == name and str(dec_password)[2:-1:] == password:
                    is_prime = True 
        if is_prime:
            dec_list_name = []
            dec_list_pass = []
            objs = Saved_info.objects.filter(user=name).all()
            for obj in objs:
                if obj.key:
                    cut_key = obj.key[2:-1:] 
                    cut_name = obj.name[2:-1:] 
                    cut_password = obj.password[2:-1:] 
                    # print(obj.key,cut_key,"--", obj.name, cut_name, "--", obj.password, cut_password)
                    b_key = bytes(cut_key, encoding='utf-8')
                    b_name = bytes(cut_name, encoding='utf-8')
                    b_password = bytes(cut_password, encoding='utf-8')
                    # print(key, name, password)
                    # print(type(key), type(name), type(password))
                    crypter = Fernet(b_key)
                    dec_name = crypter.decrypt(b_name)
                    dec_password = crypter.decrypt(b_password)
                    dec_list_name.append(str(dec_name)[2:-1:])
                    dec_list_pass.append(str(dec_password)[2:-1:])

            zip_lists = zip(dec_list_name, dec_list_pass)
            request.session['username'] = name
            context = {
                'username': name,
                'zip_lists': zip_lists
            }
            return render(request, 'main.html', context)
        else:
            return HttpResponse('username or password is incorrect')

    if 'username' in request.session:
        objs = Saved_info.objects.filter(user=request.session['username']).all() 
        dec_list_name2 = []
        dec_list_pass2 = []
        for obj in objs:
                if obj.key:
                    cut_key = obj.key[2:-1:] 
                    cut_name = obj.name[2:-1:] 
                    cut_password = obj.password[2:-1:] 
                    # print(obj.key,cut_key,"--", obj.name, cut_name, "--", obj.password, cut_password)
                    b_key = bytes(cut_key, encoding='utf-8')
                    b_name = bytes(cut_name, encoding='utf-8')
                    b_password = bytes(cut_password, encoding='utf-8')
                    # print(key, name, password)
                    # print(type(key), type(name), type(password))
                    crypter = Fernet(b_key)
                    dec_name = crypter.decrypt(b_name)
                    dec_password = crypter.decrypt(b_password)
                    dec_list_name2.append(str(dec_name)[2:-1:])
                    dec_list_pass2.append(str(dec_password)[2:-1:])

        zip_lists = zip(dec_list_name2, dec_list_pass2)
        context2 = {
            'username': request.session['username'],
            'zip_lists': zip_lists,
        }
        return render(request, 'main.html', context2)
    else:
        return render(request, 'main.html', context=None)

def create(request):
    if request.method == "POST":
        key = Fernet.generate_key()
        crypter = Fernet(key)
        name = request.POST.get('name2')
        password = request.POST.get('password2')
        user_name = request.POST.get('user_name')
        enc_name = crypter.encrypt(name.encode())
        enc_password = crypter.encrypt(password.encode())
        Saved_info.objects.create(name=enc_name, password=enc_password, user=user_name, key=key)
        return redirect('/')

def logout(request):
    try:
        request.session.pop('username')
    except:
        return HttpResponse("you can not log out")
    return redirect('/')


