aa = open('..\Prathmesh2\Ramadi_TZ-RM-NCS-560-4-SR02_2023-10-12_08-21-14').readlines()
vvv=''
valid = True
for a in aa:
    if '10.88.38' in a: vvv+=a
    if ('RP/0/RP0/CPU0:TZ' in a or 'RP/0/RP1/CPU0:TZ' in a) and 'show media' in a : vvv += a
    if 'apphost: ' in a or 'harddisk:   ' in a : vvv+=a
    if 'rootfs: ' in a: vvv+=a
   # if 'rootfs:' in a:
       # ss= a.split(' ')[-1].split('M')[0]
       # if 'G' not in ss and int(ss) < 700:
    if 'Media Info for Location: node0' in a: vvv+=a

print(vvv)