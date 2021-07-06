import nmap
import nmap3
import json

nmap = nmap3.Nmap()
os_results = nmap.nmap_version_detection("10.129.179.163")
print(os_results)

#this pretty prints the json
jsonoutput = json.dumps(os_results, indent=4)
print(jsonoutput)

print('============================================================')

for i in range(len(os_results['10.129.179.163']['ports'])):
        variable = os_results['10.129.179.163']['ports'][i]['portid']
        variable2 = os_results['10.129.179.163']['ports'][i]['service']['name']
        variable3 = os_results['10.129.179.163']['ports'][i]['service']['version']
        print ('[*] Discovered Port: ' + variable)
        print ('[*] Service : ' + variable2)
        print ('[*] Version : ' + variable3)
        print ('============================================================')

