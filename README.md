# micropython
Material para aula de MicroPython (Linguagens de Programação)

Clonando este repositório:
```
$ git clone https://github.com/pedromxavier/micropython.git
$ cd micropython
```

## **Importante:** não esqueça de executar os comandos abaixo usando `sudo`!


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

2 - Intruções para usar o shell do dispositivo:

Instalar o pacote usando o comando `$ sudo apt install picocom`.
```
$ picocom /dev/ttyUSB0 -b 115200
```

3 - Carregando arquivos:

Instale a biblioteca `ampy`:
```
$ pip install adafruit-ampy
```

Carregue ou execute *scripts Python* no dispositivo:
```
$ ampy --port /dev/ttyUSB0 run script.py

$ ampy --port /dev/ttyUSB0 put main.py
```
