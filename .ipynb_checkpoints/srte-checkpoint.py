aa="""


"""

def indexconvert():
    b = aa.replace('label 160', 'adjacency 10.88.38.').replace('01', '1').replace('02', '2').replace('03', '3').replace(
        '04', '4').replace('05', '5').replace('06', '6').replace('07', '7').replace('08', '8').replace('09', '9')
    print(b)




sid = """1	KJ3_SH1	7	11	13	63	55
2	KJ3_SH1	7	11	21	55	
3	KJ3_SH1	1	19	15	55	
4	KJ3_SH1	7	12	14	56	55
1	KJ3_SH2	7	12	14	56	
2	KJ3_SH2	2	20	16	64	56
3	KJ3_SH2	7	11	21	55	56
4	KJ3_SH2	1	19	15	55	56
1	KJ4_SH1	7	11	13	63	55
2	KJ4_SH1	7	11	21	55	
3	KJ4_SH1	1	19	15	55	
4	KJ4_SH1	7	12	14	56	55
1	KJ4_SH2	7	12	14	56	
2	KJ4_SH2	2	20	16	64	56
3	KJ4_SH2	7	11	21	55	56
4	KJ4_SH2	1	19	15	55	56
1	MR3_SH1	7	11	13	63	55
2	MR3_SH1	7	11	21	55	
3	MR3_SH1	1	19	15	55	
4	MR3_SH1	7	12	14	56	55
1	MR3_SH2	7	12	14	56	
2	MR3_SH2	2	20	16	64	56
3	MR3_SH2	7	11	21	55	56
4	MR3_SH2	1	19	15	55	56
1	MR4_SH1	7	11	13	63	55
2	MR4_SH1	7	11	21	55	
3	MR4_SH1	1	19	15	55	
4	MR4_SH1	7	12	14	56	55
1	MR4_SH2	7	12	14	56	
2	MR4_SH2	2	20	16	64	56
3	MR4_SH2	7	11	21	55	56
4	MR4_SH2	1	19	15	55	56
1	MW1_SH1	63	55			
2	MW1_SH1	14	56	55		
1	MW1_SH2	63	55	56		
2	MW1_SH2	14	56			
1	MW2_SH1	13	63	55		
2	MW2_SH1	56	55			
1	MW2_SH2	13	63	55	56	
2	MW2_SH2	56				
1	SH1_KJ3	63	13	11	7	8
2	SH1_KJ3	21	11	6	8	
3	SH1_KJ3	15	19	1	8	
4	SH1_KJ3	56	14	12	7	8
1	SH1_KJ4	63	13	11	7	9
2	SH1_KJ4	21	11	6	9	
3	SH1_KJ4	15	19	1	9	
4	SH1_KJ4	56	14	12	7	9
1	SH1_MR3	63	13	11	7	3
2	SH1_MR3	21	11	7	3	
3	SH1_MR3	15	19	1	3	
4	SH1_MR3	56	14	12	7	3
1	SH1_MR4	63	13	11	7	4
2	SH1_MR4	21	11	7	4	
3	SH1_MR4	15	19	1	4	
4	SH1_MR4	56	14	12	7	4
1	SH1_MW1	63	13			
2	SH1_MW1	56	14	13		
1	SH1_MW2	63	13	14		
2	SH1_MW2	56	14			
1	SH2_KJ3	14	12	7	8	
2	SH2_KJ3	64	16	20	2	8
3	SH2_KJ3	55	21	11	7	8
4	SH2_KJ3	55	15	19	1	8
1	SH2_KJ4	14	12	7	9	
2	SH2_KJ4	64	16	20	2	9
3	SH2_KJ4	55	21	11	7	9
4	SH2_KJ4	55	15	19	1	9
1	SH2_MR3	14	12	7	3	
2	SH2_MR3	64	16	20	2	3
3	SH2_MR3	55	21	11	7	3
4	SH2_MR3	55	15	19	1	3
1	SH2_MR4	14	12	7	4	
2	SH2_MR4	64	16	20	2	4
3	SH2_MR4	55	21	11	7	4
4	SH2_MR4	55	15	19	1	4
1	SH2_MW1	55	63	13		
2	SH2_MW1	14	13			
1	SH2_MW2	55	63	13	14	
2	SH2_MW2	14				

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
indexconvert()