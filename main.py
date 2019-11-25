import machine
import utime

led = machine.Pin(2, machine.Pin.OUT)

N = 200_000
t = utime.time()
for i in range(N):
    led.on()
    led.off()
T = (utime.time() - t)

print("Levou {} s, frequencia = {}Hz".format(T, N/T))
