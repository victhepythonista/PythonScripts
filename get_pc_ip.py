import socket

"""
a much better and alternative way of getting your PCs ip
even if offline or unplugged

replacing the old non-reliable       -> socket.gethostname()

   """
class Solution:
    
    def get_ip(self):
        address = ("10.255.255.255", 1)                             # the dummy address
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #  create a UDP socket
        sock.connect(address)
        
        ip = sock.getsockname()[0]                                  # heres your IP !!!
        
        sock.close()
        return ip 
        
