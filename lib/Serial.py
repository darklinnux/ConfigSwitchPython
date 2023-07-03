import serial
class Serial:
    
    def __init__(self,port='COM1',baudrate=9600,parity="N",stopbits=1,bytesize=8,timeout=8):
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
        self.serial = self._initConection()
    
    def _initConection(self):
        pass