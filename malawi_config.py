import os, sys, re
aa= r"C:\Users\chugorji\OneDrive - Cisco\Airtel MPBN Malawi Ph2 - Team Space\ROUTING FOLDER From Arons Desktop\MALAWI\Config Dumps\LL"
ff = open(aa+r'\LGSS02.txt').readlines()

def bsslss(ff):
    ab = {}
    ac = []
    vlan = []
    vlan1 = []
    for a in ff:
        if 'configure ports' in a and 'display-string' in a:
            port = a.split(' ')[2]
            x = a.split(' ')[-1]
            ac.append(port + '\t' + x)

        if 'vlan' in a and 'tag' in a and 'port' not in a:
            id = a.split(' ')[-1].strip()  #
            name = a.split(' ')[2]
            vlan.append(name + '\t' + id + '\n')
            ab.update({name: id})

        if 'vlan' in a and 'tag' in a and 'port' in a and 'Default' not in a:
            ports = a.split(' ')[5] + '\t' + a.split(' ')[6]
            name = a.split(' ')[2]
            vlan1.append(name + '\t' + ports)

    print(''.join(ac))
    print('\n\n\n\n')
    print(''.join(vlan))
    print('\n\n\n\n')
    print(''.join(vlan1))
    print(ab)

    for a in vlan1:
        a1 = a.split('\t')[0]
        print(a + '\t' + ab[a1])
    # print(len(vlan))
    # print(len(ac))
#bsslss(ff)
aa1= r"C:\Users\chugorji\OneDrive - Cisco\Airtel MPBN Malawi Ph2 - Team Space\ROUTING FOLDER From Arons Desktop\MALAWI\Config Dumps\BT"
node ='BTZTECSR02'
ff1= open(aa1+r'\{}.log'.format(node)).read().split('\n\n')
#ff1= open(aa1+r'\{}.log'.format(node)).read().split('$')
def vrfIP(ff1):
    b=0
    for a in ff1:
        #if ('interface ' in a and 'description' in a and 'ip address' in a) or ('interface smartgroup' in a and 'description' in a) or ('interface vlan' in a and 'description' in a):
        if ('interface ' in a and 'ip address' in a) or ('interface smartgroup' in a and 'ip address' in a) or ('interface vlan' in a and 'ip address' in a):        
        #if 'interface vlan' in a and 'description' in a:
            a=a.replace('interface ','').replace('  description ','').replace(' ip address ','').replace('ip vrf forwarding ','')
            a=[aa.strip() for aa in re.split('\n' ,a)]
            print(node+'\t'+'\t'.join(a))
            b+=1
    print(b)
    for a in ff1:          #for all described interfaces on the Nodes
        if ('interface ' in a and 'description' in a and 'interface vlan' not in a and 'smartgroup' not in a):
        #if 'interface vlan' in a and 'description' in a:
            a=a.replace('interface ','').replace('  description ','').replace(' ip address ','').replace('ip vrf forwarding ','')
            a=[aa.strip() for aa in re.split('\n' ,a)]
            #print(node+'\t'+'\t'.join(a))
            b+=1
vrfIP(ff1)


rr= r"C:\Users\chugorji\OneDrive - Cisco\Airtel MPBN Malawi Ph2 - Team Space\ROUTING FOLDER From Arons Desktop\MALAWI\Config Dumps\BT"
node ='BTZTECSR01'
ff2= open(rr+r'\{}.log'.format(node)).read()
def portsDescription():
    for aa in ff2.split('exit'):
        c = []
        # if 'shutdown' not in aa and 'description' in aa:
        if 'shutdown' not in aa and 'description' in aa:
            c = [b.strip() for b in aa.split('\n') if 'description' in b or 'port' in b]
            print(('MZU-7750-01' + '\t' + '\t'.join(c)).replace('description', ''))
#portsDescription()


def vrfnames():
    for aa in ff2.split('\n'):
        if 'ip vrf VRF' in aa:
            print(aa.split(' ')[-1])


#vrfnames()

def checkVRRP():
    aa="""vrrp
  interface smartgroup1.985
    vrrp 1 accept
    vrrp 1 ipv4 10.150.16.12
    vrrp 1 timers advertise 4
  
  interface smartgroup1.986
    vrrp 1 accept
    vrrp 1 ipv4 10.150.53.9
    vrrp 1 timers advertise 4
  
  interface smartgroup1.987
    vrrp 1 accept
    vrrp 1 ipv4 10.150.53.1
    vrrp 1 timers advertise 4
  
  interface smartgroup1.1070
              vrrp 1 accept
    vrrp 1 ipv4 10.150.92.30
    vrrp 1 timers advertise 4
  
  interface smartgroup1.1071
    vrrp 1 accept
    vrrp 1 ipv4 10.150.92.38
    vrrp 1 timers advertise 4
  
  interface smartgroup1.135
    vrrp 1 accept
    vrrp 1 ipv4 10.150.13.33
    vrrp 1 timers advertise 4
  
  interface smartgroup1.136
    vrrp 1 accept
    vrrp 1 ipv4 10.150.13.41
    vrrp 1 timers advertise 4
  
  interface smartgroup1.1500
    vrrp 1 accept
    vrrp 1 ipv4 10.154.0.1
    vrrp 1 timers advertise 4
  
  interface smartgroup1.1501
    vrrp 1 accept
    vrrp 1 ipv4 10.154.0.129
    vrrp 1 timers advertise 4
  
  interface smartgroup1.1105
    vrrp 1 accept
    vrrp 1 ipv4 172.26.185.145
    vrrp 1 timers advertise 4
  
  interface smartgroup1.4009
    vrrp 1 accept
    vrrp 1 ipv4 192.168.198.19
              vrrp 1 priority 254
    vrrp 1 timers advertise 4
  
  interface smartgroup1.212
    vrrp 3 accept
    vrrp 3 ipv4 192.168.198.6
    vrrp 3 timers advertise 4
  
  interface smartgroup1.920
    vrrp 5 accept
    vrrp 5 ipv4 172.28.227.249
    vrrp 5 timers advertise 4
  
  interface smartgroup1.199
    vrrp 7 accept
    vrrp 7 ipv4 192.168.199.10
    vrrp 7 timers advertise 4
  
  interface smartgroup1.921
    vrrp 8 accept
    vrrp 8 ipv4 10.150.30.33
    vrrp 8 timers advertise 4
  
  interface smartgroup1.862
    vrrp 10 accept
    vrrp 10 ipv4 172.26.191.254
    vrrp 10 timers advertise 4
  
  interface smartgroup1.132
    vrrp 15 accept
    vrrp 15 ipv4 10.157.12.1
    vrrp 15 timers advertise 4
  
  interface smartgroup1.125
    vrrp 13 accept
    vrrp 13 ipv4 10.200.1.1
    vrrp 13 timers advertise 4
            
  interface smartgroup1.110
    vrrp 12 accept
    vrrp 12 ipv4 10.200.0.1
    vrrp 12 timers advertise 4
  
  interface smartgroup1.4007
    vrrp 17 accept
    vrrp 17 ipv4 10.150.30.1
    vrrp 17 timers advertise 4
  
  interface smartgroup1.351
    vrrp 9 accept
    vrrp 9 ipv4 10.150.30.78
    vrrp 9 timers advertise 4
  
  interface smartgroup1.1067
    vrrp 18 accept
    vrrp 18 ipv4 10.150.101.84
    vrrp 18 timers advertise 4
  
  interface smartgroup1.740
    vrrp 16 accept
    vrrp 16 ipv4 10.150.102.1
    vrrp 16 timers advertise 4
  
  interface smartgroup1.650
    vrrp 19 accept
    vrrp 19 ipv4 10.150.99.1
    vrrp 19 timers advertise 4
  
  interface smartgroup1.652
    vrrp 20 accept
    vrrp 20 ipv4 10.150.99.17
    vrrp 20 timers advertise 4
  
  interface smartgroup1.655
              vrrp 21 accept
    vrrp 21 ipv4 10.150.99.41
    vrrp 21 timers advertise 4
    """
    b=[]
    rr=[]
    for a in aa.split('\n'):
        if 'inter' in a:
            b.clear()
            b.append(a)
        if 'inter' not in a:
            b.append(a)
            #print(b)
        if 'advertise 4' in a:        
            print('\t'.join([b[0].strip("interface "),b[2].split(' ')[-1]]))

checkVRRP()

aa= r"C:\Users\chugorji\OneDrive - Cisco\Documents\NTC & WTC nodes dump"
print(aa)
ff = open(aa+r"\NTC_M6K-8S-P_CR01.log").readlines()
print("oooo")                                                                                                                                                                                                                   
for a in ff:
    print(a)