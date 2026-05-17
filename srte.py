import glob, os, sys


def indexconvert():
    ss=open('myfiles/srte').read()
    ss = ss.replace('label 160', 'adjacency 10.88.38.').replace('01', '1').replace('02', '2').replace('03', '3').replace(
            '04', '4').replace('05', '5').replace('06', '6').replace('07', '7').replace('08', '8').replace('09', '9')
    # print(ss)

    pp=[]
    pp2=[]
    ip = {}
    for a in ss.split('\n'):
        if a=='': continue
        aa=a.split(' ')
        xx=aa[3].split('_SID')[0]
        ip.update({xx:aa[-1].split('.')[-1]})
        #print(ip.get(xx))
        pp.append(aa[3])
        pp2.append(aa[3].split('_SID')[0])

    gp =sorted(set(pp))
    gp2=sorted(set(pp2))
    out='\n\n\n'
    out4 = '\ncommit\n'
    out2='\n'
    out3= '\n'.join([f'no segment-routing traffic-eng segment-list {a}' for a in gp ])
    #print('\n'.join(gp2))
    for g2 in gp2:
        out+=f"""segment-routing traffic-eng segment-list {g2}_IGP
segment-routing traffic-eng segment-list {g2}_IGP index 10 mpls adjacency 10.88.38.{ip.get(g2)}\n"""
        out2+= f"""
segment-routing traffic-eng policy {g2} 
segment-routing traffic-eng policy {g2} color {ip.get(g2)} end-point ipv4 10.88.38.{ip.get(g2)}
segment-routing traffic-eng policy {g2} autoroute 
segment-routing traffic-eng policy {g2} autoroute force-sr-include
segment-routing traffic-eng policy {g2} autoroute include ipv4 10.88.38.{ip.get(g2)}/32
segment-routing traffic-eng policy {g2} candidate-paths 
segment-routing traffic-eng policy {g2} candidate-paths preference 1 
segment-routing traffic-eng policy {g2} candidate-paths preference 1 explicit segment-list {g2}_IGP 
segment-routing traffic-eng policy {g2} candidate-paths preference 200\n"""
    
        for g in gp:
            if g2 in g:
                out2+=f'segment-routing traffic-eng policy {g2} candidate-paths preference 200 explicit segment-list {g}\n'
    print(out3,out4,out,ss,out2)    




sid = """1	IG1_KJ3	55	15	19	1	8
2	IG1_KJ3	76	22	12	7	8
1	IG1_KJ4	55	15	19	1	9
2	IG1_KJ4	76	22	12	7	9
1	IG1_MR3	55	15	19	1	3
2	IG1_MR3	76	22	12	7	3
1	IG1_MR4	55	15	19	1	4
2	IG1_MR4	76	22	12	7	4
1	IG1_MW1	55	13			
2	IG1_MW1	76	56	14	13	
1	IG1_MW2	55	13	14		
2	IG1_MW2	76	56	14		
1	IG2_KJ3	56	14	12	7	8
2	IG2_KJ3	22	12	7	8	
1	IG2_KJ4	56	14	12	7	9
2	IG2_KJ4	22	12	7	9	
1	IG2_MR3	56	14	12	7	3
2	IG2_MR3	22	12	7	3	
1	IG2_MR4	56	14	12	7	4
2	IG2_MR4	22	12	7	4	
1	IG2_MW1	75	55	13		
2	IG2_MW1	56	14	13		
1	IG2_MW2	75	55	13	14	
2	IG2_MW2	56	14			
1	KJ3_IG1	1	19	15	55	75
2	KJ3_IG1	7	12	22	76	75
1	KJ3_IG2	7	12	14	56	76
2	KJ3_IG2	7	12	22	76	
1	KJ4_IG1	1	19	15	55	75
2	KJ4_IG1	7	12	22	76	75
1	KJ4_IG2	7	12	14	56	76
2	KJ4_IG2	7	12	22	76	
1	MR3_IG1	1	19	15	55	75
2	MR3_IG1	7	12	22	76	75
1	MR3_IG2	7	12	14	56	76
2	MR3_IG2	7	12	22	76	
1	MR4_IG1	1	19	15	55	75
2	MR4_IG1	7	12	22	76	75
1	MR4_IG2	7	12	14	56	76
2	MR4_IG2	7	12	22	76	
1	MW1_IG1	55	75			
2	MW1_IG1	14	56	76	75	
1	MW1_IG2	55	75	76		
2	MW1_IG2	14	56	76		
1	MW2_IG1	13	55	75		
2	MW2_IG1	56	76	75		
1	MW2_IG2	13	55	75	76	
2	MW2_IG2	56	76			

"""
def segments(sid):
    data = [[ai for ai in a.split('\t') if ai != ''][-1] for a in sid.split('\n') if a !='']

    print(data)
    gp = sorted(set([a.split('\t')[1] +'xx'+[ai for ai in a.split('\t') if ai != ''][-1] for a in sid.split('\n') if a != ''] ))
    gp2=sorted(set([a.split('\t')[1] +'_SID'+a.split('\t')[0] for a in sid.split('\n') if a != ''] ))
    b=''
    f=[]
    for rr in sid.split('\n'):
        ss=rr.split('\t')
        a = 10
        ss = [x for x in ss if x != ""]
        c=1
        for aa in ss[2:]:
            #if aa == '': continue
            if c==1:print(f"""segment-routing traffic-eng segment-list {ss[1]}_IGP
segment-routing traffic-eng segment-list {ss[1]}_IGP index 10 mpls adjacency 10.88.38.{ss[-1]}
segment-routing traffic-eng segment-list {ss[1]}_SID{ss[0]}""")

            print(f"segment-routing traffic-eng segment-list {ss[1]}_SID{ss[0]} index {a} mpls adjacency 10.88.38.{aa}")
            a += 10
            c += 1

    for m in gp:
        mm= m.split('xx')[0]
        ip = m.split('xx')[1]
        aa= f"""segment-routing traffic-eng policy {mm} 
segment-routing traffic-eng policy {mm} color {ip} end-point ipv4 10.88.38.{ip}
segment-routing traffic-eng policy {mm} autoroute 
segment-routing traffic-eng policy {mm} autoroute force-sr-include
segment-routing traffic-eng policy {mm} autoroute include ipv4 10.88.38.{ip}/32
segment-routing traffic-eng policy {mm} candidate-paths 
segment-routing traffic-eng policy {mm} candidate-paths preference 1 
segment-routing traffic-eng policy {mm} candidate-paths preference 1 explicit segment-list {mm}_IGP 
segment-routing traffic-eng policy {mm} candidate-paths preference 200"""
        print(aa)
        for li in gp2:
            if mm in li:
                print(f'segment-routing traffic-eng policy {mm} candidate-paths preference 200 explicit segment-list {li}')
    #print(gp2)
    #print('\n'.join(f),'\n', len(f))
#segments(sid)
#indexconvert()

myFolder= r"C:\Users\chugorji\OneDrive - Cisco\Documents\Cisco_scripts\SRTE MOGO\*".replace('\\','/')
home = os.path.dirname(sys.argv[0]).replace('\\', '/')
oneof = open(home+'/oneof', 'w+')
def mySrteForder():
    print(myFolder)
    for filepath in glob.glob(myFolder):
        fname=filepath.split('\\')[-1]
        with open(filepath, 'r') as file:  
            content = file.readlines()
            for aa in content:
                if 'adjacency' in aa :
                    #print(f'{fname}\t{aa}')  
                    oneof.write(f'{fname}\t{aa}')


mySrteForder()