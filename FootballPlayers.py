from BeautifulSoup import BeautifulSoup
import urllib3
import certifi

url = "https://www.pro-football-reference.com/players/Q/"

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
response = http.urlopen('GET', url)

soup = BeautifulSoup(response.data)

for link in soup.findAll(id='div_players'):
    print(link)