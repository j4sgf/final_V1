import urllib.request
import re


web_url = 'http://www.sahih-bukhari.com'
web_url_req = urllib.request.Request(web_url)
web_url_open = urllib.request.urlopen(web_url_req)
respData1 = web_url_open.read()
link = re.findall(
    r'<a href="([^~]+?)"\sclass="Style8"', str(respData1))
print(link)

url = []
D = open('link.txt', 'w')
for allurl in link:
    url.append("http://www.sahih-bukhari.com/" + allurl)

for alllink in url:
    D.write("\n" + alllink)
D.close()

hadith = []

for allink in url:
    req = urllib.request.Request(allink)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    hadithraw = re.findall(
        r'Volume\s(\d{1,2}),\sBook\s(\d{1,3}),\sNumber\s(\d{1,4})(?:[^~]+?)<strong>Narrated\sby\s([^~]+?)</strong>(?:[^~]+?)<blockquote>([^~]+?)</blockquote>', str(respData))
    for hadith_data in hadithraw:
        hadith.append(hadith_data)
vol = []
book = []
number = []
narrator = []
ayah = []
for a in hadith:
    vol.append(a[0])
    book.append(a[1])
    number.append(a[2])
    narrator.append(a[3])
    ayah.append(a[4])

F = open('hadith.txt', 'a')
for j, k, l, m, n in zip(vol, book, number, narrator, ayah):
    F.write("Vol : " + j)
    F.write("\nBook : " + k)
    F.write("\nNumber : " + l)
    F.write("\nNarrated by : " + m)
    F.write("\nVerse : " + n)
    F.write("\n")
    F.write("\n")

F.close()
