from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from home.models import registeration, attendance
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

# password for user veer is Veer$$@@

# Create your views here.

def index(request):
    context1 = {
        'display_logout': 'Logout'
    }
    context2 = {
        'display_login': 'Login'
    }
    
    if request.user.is_authenticated:
        print("Logged in")
        return render(request, 'index.html', context1)
    else:
        print("Not logged in")
        return render(request, 'index.html')

    #if request.user.is_anonymous:
    #    return redirect('/login')
    #return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        secret = request.POST.get('password')
        # Check if user entered correct credential.
        user = authenticate(username = username, password = secret)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
         
    return render(request, 'login.html')

def logoutUser(request):   
    logout(request)
    return redirect('/')

def Registeration(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        img = request.POST['img']

        register = registeration(name=name, roll_no = roll_no, email= email, phone=phone, department=department, img=img)
        register.save()
        return render(request, 'index.html')

    else:
        return render(request, 'registeration.html')

def base(request):
    return render(request, 'base.html')

def records(request):
    data = registeration.objects.all()
    print(data)
    return render(request, 'records.html', {'data': data})

def attendance_data(request):
    data = registeration.objects.raw('SELECT roll_no, home_registeration.name, home_attendance.date, home_attendance.status from home_registeration inner join home_attendance on home_registeration.roll_no=home_attendance.roll_no_id;')
    print(data.columns)
    return render(request, 'attendance.html', {'data':data})

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass