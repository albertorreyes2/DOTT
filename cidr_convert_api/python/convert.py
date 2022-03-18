# These functions need to be implemented
from netaddr import IPAddress
import socket
import struct
import ipaddress

class CidrMaskConvert:

    def cidr_to_mask(self, val):
        if (int(val) >= 1 and int(val) <= 32):
            host_bits = 32 - int(val)
            val = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
            return str(val)
        else:
            return 'Invalid'
        
    def mask_to_cidr(self, val):
        if val != '0.0.0.0' and IpValidate.ipv4_validation(self,val) == True and self.ipv4_mask_len(val) == True:
            try:
                val = IPAddress(val).netmask_bits()
                return str(val)
            except:
                return 'Invalid'
        else:
            return 'Invalid'

    def ipv4_mask_len(self, val):
        a, b, c, d = (int(octet) for octet in val.split("."))
        mask = a << 24 | b << 16 | c << 8 | d
        if mask == 0:
            return False
        # Count the number of consecutive 0 bits at the right.
        # https://wiki.python.org/moin/BitManipulation#lowestSet.28.29
        m = mask & -mask
        right0bits = -1
        while m:
            m >>= 1
            right0bits += 1
        # Verify that all the bits to the left are 1's
        if mask | ((1 << right0bits) - 1) != 0xffffffff:
           return False
        return True

class IpValidate:

    def ipv4_validation(self, val):
        try:
            ip = ipaddress.ip_address(val)
            return True
        except ValueError:
            return False