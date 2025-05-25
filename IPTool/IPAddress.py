class IPAddress:
    def __init__(self,ip:str):
        self.ip = ip
        

    def toBits(self)->str:

        if len(self.ip) > 15:
            return self.ip
        
        a,b,c,d = self.ip.split(".")
        a,b,c,d = map(int, [a,b,c,d])

        aBin,bBin,cBin,dBin = '','','',''

        while d > 0:
            dBin =  str(d%2)+ dBin 
            d = d//2
        dBin = ((8 - len(dBin)) * '0')+dBin
        
        while c > 0:
            cBin=  str(c%2)+ cBin 
            c = c//2
        cBin = ((8 - len(cBin)) * '0')+cBin
        
        while b > 0:
            bBin=  str(b%2)+ bBin 
            b = b//2
        bBin = ((8 - len(bBin)) * '0')+bBin
        
        while a > 0:
            aBin=  str(a%2)+ aBin 
            a = a//2
        aBin = ((8 - len(aBin)) * '0')+aBin
              
        ipBin = f"{aBin} {bBin} {cBin} {dBin}"
        return ipBin

    def toIPv4(self)->str:

        if len(self.ip) <= 15:
            return self.ip

        bits = self.ip.replace(' ','')
        a,b,c,d = [bits[i:i+8] for i in range(0, len(bits), 8)]
   
        aV4,bV4,cV4,dV4 = 0,0,0,0 
        
        for i in range(len(a)):
           aV4 += 2**i*int(a[len(a)-i-1])

        for i in range(len(b)):
           bV4 += 2**i*int(b[len(b)-i-1])

        for i in range(len(c)):
           cV4 += 2**i*int(c[len(c)-i-1])

        for i in range(len(d)):
           dV4 += 2**i*int(d[len(d)-i-1])

        ipV4 = f"{aV4}.{bV4}.{cV4}.{dV4}"
        return ipV4
    
    def isMask(self) -> bool:
        ip = self.toBits().replace(' ', '')
        if "01" in ip:
            return False
        else:
            return True

    def maskBits(self) -> int:
        ip = self.toBits()
        return ip.count('1')


