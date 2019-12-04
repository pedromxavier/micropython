import machine
import utime

led = machine.Pin(2, machine.Pin.OUT)

N = 200_000

@micropython.native
def piscar():
    on = led.on
    off = led.off
    r = range(N//8)
    for i in r:
        on()
        off()
        on()
        off()
        on()
        off()
        on()
        off()
        on()
        off()

t = utime.ticks_ms()
piscar()
T = (utime.ticks_ms() - t)
T = T / 1000

print("Levou {} s, frequencia = {}Hz".format(T, N/T))
