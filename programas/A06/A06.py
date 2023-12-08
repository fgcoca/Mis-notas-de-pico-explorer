from machine import Pin, PWM
import time

# crea y configura GP7 como salida PWM
pwm5 = PWM(Pin(5))
pwm5.freq(10000) # metodo freq para hacer f=10kHz en GP5

try:
    while True:
        for i in range(0, 65535):
            pwm5.duty_u16(i)
            time.sleep_us(100)
        for i in range(65535, 0, -1):
            pwm5.duty_u16(i)
            time.sleep_us(100)
except:
    pwm5.deinit()
            