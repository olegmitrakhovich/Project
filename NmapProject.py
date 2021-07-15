import nmap
import json
import argparse

#importing nmap3 for python
import sys
sys.path.append('/root/python3-nmap')
import nmap3

parser = argparse.ArgumentParser()
parser.add_argument("Host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

nmap = nmap3.Nmap()
os_results = nmap.nmap_version_detection(host)
print(os_results)

#this pretty prints the json
#jsonoutput = json.dumps(os_results, indent=4)
#print(jsonoutput)

print('============================================================')

for i in range(len(os_results[host]['ports'])):
        variable = os_results[host]['ports'][i]['portid']
        variable2 = os_results[host]['ports'][i]['service']['name']
        variable3 = os_results[host]['ports'][i]['service']['version']
        print ('[*] Discovered Port: ' + variable)
        print ('[*] Service : ' + variable2)
        print ('[*] Version : ' + variable3)
        print ('============================================================')
