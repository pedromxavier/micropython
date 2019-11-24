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
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-upython.bin
```

