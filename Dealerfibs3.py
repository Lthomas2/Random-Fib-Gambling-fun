import random
def stats(n):
    j=0
    s=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    while j<=n:
        p1=['Alive',.55,float(1000),float(950),37,35]
        p2=['Alive',.55,float(1000),float(950),19,17]
        p3=['Alive',.55,float(1000),float(950),8.5,8]
        p4=['Alive',.55,float(1000),float(950),1.111,1]
        p=[p1,p2,p3,p4]
        dealer=float(100000)
        i=0
        while (p[0][0]=='Alive' or p[1][0]=='Alive' or p[2][0]=='Alive' or p[3][0]=='Alive') and dealer!='dealer is dead':
            if i%4 ==0:
##                print 'Round '+str(i/4+1)
                r=(i/4+1)
            if p[i%4][0]=='Alive':
                b=random.randint(1,int(p[i%4][4]*1000+1000))
                if b<=1000:
                    b=1
                else:
                    b=-1
                if b==1:
                    w=p[i%4][3]
                    p[i%4][3]=p[i%4][3]+p[i%4][5]*p[i%4][1]*p[i%4][2]
                    dealer=dealer-p[i%4][5]*p[i%4][1]*p[i%4][2]
                if b==-1:
                    w=p[i%4][3]
                    p[i%4][3]=p[i%4][3]-p[i%4][1]*p[i%4][2]
                    dealer=dealer+p[i%4][1]*p[i%4][2]
                if dealer<=0:
                    dealer='dealer is dead'
                    k=0
                    while k<=3:
                        if p[k%4][0]=='Alive':
                            s[k%4][2]+=1
                        k+=1
                if p[i%4][3]<=0:
                    p[i%4][0]='Dead'
                    dealer=dealer-p[i%4][1]*p[i%4][2]+w
                    p[i%4][3]=0
                    s[i%4][0]=(w+s[i%4][0]*(j-s[i%4][2]))/(j+1-s[i%4][2])
                    s[i%4][1]=(r+s[i%4][1]*j)/float(j+1)
                   ## print 'player '+str(i%4+1)+' is dead'
                p[i%4][2]=w
            i+=1
        j+=1
##        print "dealer: "+str(dealer)
##        print p
    print s
    print "dealer has "+str(dealer)
    
