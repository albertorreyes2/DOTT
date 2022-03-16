import socket
import struct

# These functions need to be implemented
class CidrMaskConvert:

    def cidr_to_mask(self, val):
        host_bits = 32 - int(val)
        val = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        return str(val)

    def mask_to_cidr(self, val):
        return val



class IpValidate:

    def ipv4_validation(self, val):
        return True
