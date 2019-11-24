# micropython
Material para aula de MicroPython (Linguagens de Programação)

Clonando este repositório:
```
$ git clone https://github.com/pedromxavier/micropython.git
$ cd micropython
```

1 - Instruções para gravar no microcontrolador:

Primeiro instalar a biblioteca `esptool`:
```
$ pip install esptool
```

Em seguinda, com o dispositivo conectado por USB:
```
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-upython.bin
```

**Nota:** No Windows, sempre substituir `--port /dev/ttyUSB0` por `--port COM1`.

2 - Intruções para usar o shell do dispositivo:

No Windows, instalar o programa `Tera Term`.

No OSX, usar o terminal.

No Linux, instalar o pacote usando o comando `$ sudo apt install picocom`.
```
$ picocom /dev/ttyUSB0 -b 115200
```
