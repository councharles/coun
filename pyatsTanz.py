from pyats.topology import loader
#from genie.testbed import load

testbed = loader.load('myfiles/testbed.yaml')
for device in testbed.devices.values():
    device.connect(init_exec_commands=['terminal length 0'],init_config_commands=[])
    out = device.execute('sh run int lo0')
    #out = device.parse('sh run int lo0')
    print(out)
