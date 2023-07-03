from controler.Cisco import Cisco
#switch = Cisco("10.0.0.1","pedro","admin123")
#switch.SET

switch = Cisco("10.0.0.1","usuario","senha")
switch.setConfigVlanPort(20,19)
