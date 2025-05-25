import IPAddress

class IPToolIF:

    @staticmethod
    def isValid(ip:IPAddress.IPAddress) -> bool:

        ip = ip.toIPv4()

        partes = ip.split('.')

        if len(partes) != 4:
            return False
        
        for parte in partes:
            try:
                valor = int(parte)
            except:
                return False
            
            if valor > 255 or valor < 0 :
                return False

        return True

    @staticmethod
    def areSameNet(ip1:IPAddress.IPAddress,ip2:IPAddress.IPAddress,mask:IPAddress.IPAddress)  -> bool:
        
        ip1 = int(ip1.toBits().replace(" ", ""),2)
        ip2 =  int(ip2.toBits().replace(" ", ""),2)
        mask =  int(mask.toBits().replace(" ", ""),2)

        net1 = ip1 & mask
        net2 = ip2 & mask

        return net1 == net2
    
    @staticmethod
    def broadcast(ip:IPAddress.IPAddress, mask:IPAddress.IPAddress)-> IPAddress.IPAddress:
        ip = int(ip1.toBits().replace(" ", ""),2)
        mask =  int(mask.toBits().replace(" ", ""),2)
        broadcast =( ip | ((~mask))) & 0xFFFFFFFF
        broadcast = bin(broadcast).replace('0b','')

        return IPAddress.IPAddress(broadcast)
    
    @staticmethod
    def network(ip:IPAddress.IPAddress, mask:IPAddress.IPAddress) -> IPAddress.IPAddress:
        ip = int(ip1.toBits().replace(" ", ""),2)
        mask =  int(mask.toBits().replace(" ", ""),2)

        net = ip & mask
        net = bin(net).replace('0b','')
        return IPAddress.IPAddress(net)



        











ip1 = IPAddress.IPAddress("192.168.0.1")
ip2 = IPAddress.IPAddress("255.255.255.255")
ip3 = IPAddress.IPAddress("11000000101010000000000000000001")
mask = IPAddress.IPAddress("255.255.0.0")


broadcast = IPToolIF.broadcast(ip1,mask)
net = IPToolIF.network(ip1,mask)


print(broadcast.toIPv4())

print(net.toIPv4())