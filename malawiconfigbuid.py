import ipaddress

ips = """
3200	10.160.1.0/24	OOB Mgmt
3201	10.160.3.0/24	ACI Inband
3202	10.160.7.0/27	FW App Mgmt (FXOS)
3203	10.160.7.32/27	FW Admin Context
3204	10.160.7.64/27	GI Context
3205	10.160.7.96/27	FW GRX Context
3206	10.160.7.128/27	Enterprise COntext
3207	10.160.7.160/27	SIP context
3208	10.150.102.0/24	Omlich FW Mgmt
3216	10.160.12.0/29	Gi Context Trust
3217	10.160.12.8/29	Gi Context Untrust
3218	10.160.12.16/29	GRX Context Media Cn
3219	10.160.12.24/29	GRX Context Sig Cn
3220	10.160.12.32/29	GRX Context Untrust
3221	10.160.12.40/29	GRX Context eDNS
3222	10.160.12.48/29	ACI to Omlich Firewall Inside
3223	10.160.12.56/29	ACI to Omlich FW Outside Global
3224	10.160.12.64/29	ACI to Omlich FW Outside OAM
3225	10.160.12.72/29	ACI to Omlich FW Outside Cha-EXT
3226	10.160.12.80/29	Enterprise Context Trust
3227	10.160.12.88/29	Enterprise Context Untrust
3228	10.160.12.96/29	SIP Context Trust
3229	10.160.12.104/29	SIP Context Untrust

"""
def get_last_three_usable_ips():
    for ee in ips.split('\n'):
        if ee =='': continue
        rr =ee.split('\t')
        subnet = rr[1]
        network = ipaddress.ip_network(subnet)
        # usable_ips = list(network.hosts())
        usable_ips = [a.exploded for a in network.hosts()]
        print('\n'.join(usable_ips[-3:-1]))
        x = 1
        for uu in usable_ips[-3:-1]:
            print(f"""interface Be200.{rr[0]}
description {rr[2]}    
ip address {uu} {network.netmask}
vrrp 10 ip {usable_ips[-1]}
vrrp 10 priority {x}
vrrp 10 preempt
vrrp 10 timers advertise msec 10\n""")
            x += 9
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n')
get_last_three_usable_ips()

