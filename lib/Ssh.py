import paramiko
from exception.SshException import SshException
"""
Class responsavel por gerenciar as conexão SSH utilizando a bliblioteca Paramiko

"""
class Ssh:
    def __init__(self, user, password,ip,port=22):
        self.user = user
        self.password = password
        self.ip = ip
        self._stdin =False
        self._stdout = False
        self._stderr = False
        self._port = port
        self.connection = self._initConnection()
        
    """
    Método responsavel de abrir a conexão ssh, caso ocorra algum erro vai subir uma SshException
    """    
    def _initConnection(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip,self._port,username=self.user, password=self.password)
            return ssh
        except paramiko.ssh_exception.AuthenticationException:
            print(f'[-] {self.ip}:22 - Autenticação falhou')
        except paramiko.ssh_exception.NoValidConnectionsError:
            print(f'[-] {self.ip}:22 - Nenhuma conexão válida')
        except TimeoutError:
            print(f'[-] {self.ip}:22 - Uma tentativa de conexão falhou porque o componente conectado não respondeu corretamente após um período de tempo ou a conexão estabelecida falhou')
    
    """ 
    Método responsável por enviar commando via SSH
    """
    def sendCommand(self,command):
        stdin, stdout, stderr = self.connection.exec_command(command+"\n",get_pty = True)
        self._stdin = stdin
        self._stdout = stdout
        self._stderr = stderr
    """ 
    Método com nome ainda não definido, rsrs ainda estou sem ideia para o nome desse metodo
    Método responsavel por enviar sub comandos via Ssh
    """
    def sendParam(self, param):
        self._stdin.write(param+"\n")
        self._stdin.flush()
    """ 
    Método responsavel por pegar o retorno dos comando excecutado via SSH"""
    def getOutput(self):
        return self._stdout.readlines()
    
    def connectionClose(self):
        self.connection.close()