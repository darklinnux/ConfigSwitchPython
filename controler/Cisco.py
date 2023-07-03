from controler.Switch import Switch

class Cisco(Switch):
    
    def __init__(self, ip, user, password):
        super().__init__(ip, user, password)
    
    def setConfigVlanPort(self, numbPort, numbVlan):
        commands = [
            "conf t",
            f"int gi{numbPort}",
            "switchport mode access",
            f"switchport access vlan {numbVlan}",
            "no shut",
            "end"]
        for command in commands:
            super()._setCommand(command)
            print(command)
    