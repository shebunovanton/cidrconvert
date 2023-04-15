import sys
import ipaddress

dep = []

def list(ipdep):
    print(ipdep + "+++++++++++++++++++++++++++++++++")
    for addr in ipaddress.ip_network(ipdep):
        with open("result.txt","a") as f:
            f.write(str(addr) + "\n")

if __name__ == "__main__":
    
        with open(sys.argv[1],"r") as f:
            print(f.readlines)
            for ipdep in f.readlines():
                list(ipdep)
             