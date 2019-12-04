import network
import machine

from utime import sleep_ms
import usocket as socket


# Setup WiFi connection:
def connect_wifi(ssid, passwd):
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

    print("Connecting to WiFi '%s'. This takes some time..." % ssid)

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, passwd)

    while wifi.status() == network.STAT_CONNECTING:
        sleep_ms(100)

    if wifi.isconnected():
        print("Connection established. My IP is " + str(wifi.ifconfig()[0]))
        return True
    else:
        status = wifi.status()
        if status == network.STAT_WRONG_PASSWORD:
            status = "WRONG PASSWORD"
        elif status == network.STAT_NO_AP_FOUND:
            status = "NETWORK '%s' NOT FOUND" % ssid
        else:
            status = "Status code %d" % status
        print("Connection failed: %s!" % status)
        return False


# Echo Server:
def server(port, max_clients=1):
    print("Starting server at port %d..." % port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(max_clients)

    print("Echo-Server started. Connect a client now!")

    conn, cl_addr = sock.accept()
    print("New connection from %s:%d" % cl_addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received from client: " + str(data))
        conn.send(data.encode())

    sock.close()
    print("Server stopped.")


# Simple Client:
def client(host, port):
    print("Connecting to server %s:%d..." % (host, port))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    print("Connection established.")
    print("Enter 'exit' to close the client.")

    while True:
        msg = input(">> ")
        if msg.lower().strip() == "exit":
            break

        sock.send(msg.encode())
        data = sock.recv(1024).decode()

        print("Received from server: %s" % data)

    sock.close()
    print("Client closed.")


# Interface for setting up server/client:
def main():
    PORT = 5678

    while True:
        print()
        ssid = 'micropython-lp'
        passwd = '1234567890'
        if connect_wifi(ssid, passwd):
            break

    while True:
        cmd = input("Run server (S) or client (C)? ").lower()
        if cmd == 's':
            server(PORT)
            break
        elif cmd == 'c':
            ip = '192.168.4.1'
            try:
                client(ip, PORT)
                break
            except OSError:
                print("Connection failed. Did you already start the server on the other ESP?")
        else:
            print("Invalid input. Please enter 'S' or 'C'.")


main()
