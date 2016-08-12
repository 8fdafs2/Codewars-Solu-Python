import socket
import re


class Solution():
    def __init__(self):
        self.is_valid_IP = self.is_valid_IP_01

    def is_valid_IP_01(self, strng):

        segs = strng.split('.')
        if len(segs) != 4:
            return False
        for seg in segs:
            if not seg.isdigit() or seg[0] == '0':
                return False
            if not (0 <= int(seg) <= 255):
                return False
        return True

    def is_valid_IP_02(self, strng):

        try:
            socket.inet_pton(socket.AF_INET, strng)
        except socket.error:
            return False
        return True

    def is_valid_IP_03(self, strng):

        pat = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$'

        return bool(re.match(pat, strng))
