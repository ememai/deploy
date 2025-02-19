from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm as createAccount
from django.contrib import messages
from .models import *
from .form import *
from django.db.models import Q

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message = messages.success(request, f"Logged as {username}")
            return redirect('home')
        else:
            message = messages.error(request, 'User not found')
    context = {'page':page}
    return render(request, 'base/register_login.html', context)

def registerPage(request):
    form = createAccount()
    if request.method == "POST":
        form = createAccount(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            message = messages.success(request, f"Logged as @ {username}")
            return redirect('home')
        else:
            message = messages.error(request, 'Double check conditions and follow')
    context = {'form':form}
    return render(request, 'base/register_login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.all()
    rooms = Room.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(topic__name__icontains=q) |
        Q(host__username__icontains=q)
    )
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    rooms_count = rooms.count()

    context = {
        'rooms' : rooms, 'topics':topics, 
        'rooms_count':rooms_count, 
        'room_messages': room_messages
    }

    return render(request, 'base/home.html', context)

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context={
        'user':user
    }
    return render(request, 'base/user_profile.html', context)


@login_required(login_url='login')
def roomDetail(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created_at')
    room_members = room.members.all()
    message_number = room_messages.count()
    topics = Topic.objects.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            content = request.POST.get('content')
        )
        room.members.add(request.user)
        return redirect('room-detail', room.id)

    context = {'room':room, 'room_messages':room_messages, 'message_number':message_number, 'room_members':room_members, 'topics' :topics}
    return render(request, 'base/room_detail.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host and not request.user.is_superuser:
        return HttpResponse(" You'are not allowed to update this room ")
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.host == request.user
            room.save()
            return redirect('home')
    context = {'form': form}       
    return render(request, "base/room_form.html", context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host and not request.user.is_superuser:
        return HttpResponse(" You'are not allowed to delete this room ")

    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object':room})


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user and not request.user.is_superuser:
        return HttpResponse(" You'are not allowed to delete this message ")
    
    if request.method == "POST":
        message.delete()
        return redirect('room-detail', message.room.id)
    return render(request, 'base/delete.html', {'object':message})

def updateMessage(request, pk):
    message = Message.objects.get(id=pk)
    messageForm = MessageForm(instance=message)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.user == request.user
            message.save()
            return redirect('room-detail', message.room.id)

    context = {'message':message, 'messageForm':messageForm}
    return render(request, 'base/edit_message.html', context)

