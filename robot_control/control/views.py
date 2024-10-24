from django.shortcuts import render
from django.http import JsonResponse
from .gpio_control import move_forward, move_backward, turn_left, turn_right, stop_all
import cv2
from django.http import StreamingHttpResponse

def forward(request):
    move_forward()
    return JsonResponse({"status": "Moving forward"})

def backward(request):
    move_backward()
    return JsonResponse({"status": "Moving backward"})

def left(request):
    turn_left()
    return JsonResponse({"status": "Turning left"})

def right(request):
    turn_right()
    return JsonResponse({"status": "Turning right"})

def stop(request):
    stop_all()
    return JsonResponse({"status": "Stopped"})



def gen_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen_camera(), content_type='multipart/x-mixed-replace; boundary=frame')
