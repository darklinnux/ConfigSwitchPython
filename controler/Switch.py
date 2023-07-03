from exception.SshException import SshException
from abc import ABC, abstractmethod
from lib.Ssh import Ssh

class Switch(ABC):
    
    def __init__(self,ip,user, password):
        self.ip = ip
        self.user = user
        self.password = password
        self._ssh = False
        #self._openConnection()
    
    def _openConnection(self):
        self._ssh = Ssh(self.user,self.password,self.ip)
                            
    def _setCommand(self, command):
        self._ssh.sendCommand(command)
        
    @abstractmethod
    def setConfigVlanPort(self, numbPort, numbVlan):
        pass