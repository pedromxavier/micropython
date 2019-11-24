# micropython
Material para aula de MicroPython (Linguagens de Programação)

Clonando este repositório:
```
$ git clone https://github.com/pedromxavier/micropython.git
$ cd micropython
```

Instruções para gravar no microcontrolador:

Primeiro instalar a biblioteca `esptool`:
```
$ pip install esptool
```

Em seguinda, com o dispositivo conectado por USB:
```
$ esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash
$ esptool.py --chip esp266 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp8266-micropython.bin
```

