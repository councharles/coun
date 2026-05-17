from ncclient import manager

with manager.connect(host='10.227.144.20', 
                     port=830, 
                     username='ciscosdnlab', 
                     password='Sdn@cc3ss!lab',
                     hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % 'host', 'w') as f:
        f.write(c)