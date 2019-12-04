# upython

## Sensor de Temperatura  / Umidade
import dht 

## Controle da placa (pinagem, etc.)
import machine
import utime

def main():
    ## Pino D2
    gpio_pin = 4
    
    dht_pin = machine.Pin(gpio_pin)

    sensor = dht.DHT11(dht_pin)

    t = 0
    h = 0

    while True:
        
        utime.sleep(2)
        
        sensor.measure()
        
        t = sensor.temperature()
        h = sensor.humidity()
        
        print("Temperatura: {}°C, Umidade : {}%".format(t, h))


