import socket
import time
import picamera

import netifaces

def get_ip_addresses():
    ipaddrs = []
    for interface in netifaces.interfaces():
        for ad in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
            ipaddrs.append(ad['addr'])
    return ipaddrs

if __name__ == '__main__':
    ip_addresses = get_ip_addresses()
    print("IP Addresses: {}".format(' '.join(ip_addresses)))
    
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)

        # Accept a single connection and make a file-like object out of it
        connection = server_socket.accept()[0].makefile('wb')
        try:
            camera.start_recording(connection, format='h264')
            camera.wait_recording(60)
            camera.stop_recording()
        finally:
            connection.close()
            server_socket.close()

