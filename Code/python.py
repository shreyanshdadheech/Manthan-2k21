import os
import requests
import sys


log = os.popen(
    "sudo grep GET /var/log/apache2/access.log | awk '{print $1}' | uniq").read().strip('\n')
ASN = os.popen(
    "whois -h whois.cymru.com '-v 143.198.167.64' |  sed '1,2d' | awk '{print $1}'").read()

result = "ASN value for the ip {} is :" + ASN
print(result.format(log))
url = "https://bgp.potaroo.net/cgi-bin/as-report?as=AS" + ASN + "&view=2.0"


def traceIP(url):
    resp = requests.get(url)
    print(resp.status_code)
    return resp.text


victim_info = traceIP(url)
print(victim_info)
