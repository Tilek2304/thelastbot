import RPi.GPIO as GPIO

# Настройка GPIO
GPIO.setmode(GPIO.BCM)

motors = {
    'Motor1': {'IN1': 27, 'IN2': 22, 'EN': 17},
    'Motor2': {'IN1': 5,  'IN2': 6,  'EN': 13},
    'Motor3': {'IN1': 19, 'IN2': 26, 'EN': 21},
    'Motor4': {'IN1': 16, 'IN2': 12, 'EN': 20},
}

for motor, pins in motors.items():
    GPIO.setup(pins['IN1'], GPIO.OUT)
    GPIO.setup(pins['IN2'], GPIO.OUT)
    GPIO.output(pins['IN1'], GPIO.LOW)
    GPIO.output(pins['IN2'], GPIO.LOW)

def move_forward():
    for motor, pins in motors.items():
        GPIO.output(pins['IN1'], GPIO.HIGH)
        GPIO.output(pins['IN2'], GPIO.LOW)

def move_backward():
    for motor, pins in motors.items():
        GPIO.output(pins['IN1'], GPIO.LOW)
        GPIO.output(pins['IN2'], GPIO.HIGH)

def turn_left():
    GPIO.output(motors['Motor1']['IN1'], GPIO.LOW)
    GPIO.output(motors['Motor1']['IN2'], GPIO.HIGH)
    GPIO.output(motors['Motor2']['IN1'], GPIO.HIGH)
    GPIO.output(motors['Motor2']['IN2'], GPIO.LOW)

def turn_right():
    GPIO.output(motors['Motor3']['IN1'], GPIO.HIGH)
    GPIO.output(motors['Motor3']['IN2'], GPIO.LOW)
    GPIO.output(motors['Motor4']['IN1'], GPIO.LOW)
    GPIO.output(motors['Motor4']['IN2'], GPIO.HIGH)

def stop_all():
    for motor, pins in motors.items():
        GPIO.output(pins['IN1'], GPIO.LOW)
        GPIO.output(pins['IN2'], GPIO.LOW)
