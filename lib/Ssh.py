import paramiko
from exception.SshException import SshException

class Ssh:
    def __init__(self, user, password,ip):
        self.user = user
        self.password = password
        self.ip = ip
        self._stdin =False
        self._stdout = False
        self._stderr = False
        self.connection = self._initConnection()
        
    def _initConnection(self):
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if not ssh.connect(self.ip, username=self.user, password=self.password):
            raise SshException("Não foi possivel criar a conexão")
        return ssh
    
    def sendCommand(self,command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        self._stdin = stdin
        self._stdout = stdout
        self._stderr = stderr
        
    def sendParam(self, param):
        pass