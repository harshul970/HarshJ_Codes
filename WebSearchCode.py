import sys
import urllib
from bs4 import BeautifulSoup

AgrsList = sys.argv
ArgsListLen = len(AgrsList)
query=""

if ArgsListLen == 2:
	term = AgrsList[1]
	query = "http://www.shopping.com/products?KW="+term
	print "\nSearching Keyword : "+term+"\n"

elif ArgsListLen == 3:
	term = AgrsList[1]
	pageNo = AgrsList[2]
	query = "http://www.shopping.com/products~PG-"+pageNo+"?KW="+term
	print "\nSearching Keyword : "+term+" , Page No. :"+pageNo+"\n"

else:
	print "\n Invalid Arguments"
	sys.exit()
	
htmltext = urllib.urlopen(query).read()

soup1 = BeautifulSoup(htmltext,"html.parser")

search1 = soup1.findAll('div', attrs={'class':'gridBox'})
count =0

if len(search1) == 0:
	print "No Record Found"
else:	
	for gridB in search1:
		soup2 = BeautifulSoup(str(gridB), "html.parser")
		search2 = soup2.findAll('h2')
	
		soup3 = BeautifulSoup(str(search2), "html.parser")
		search3 = soup3.findAll('a')

		soup4 = BeautifulSoup(str(search3), "html.parser")
		search4 = soup4.findAll('span')
		if len(search4)== 0:
			print str(soup4.a['title'])
			count = count +1
		else:
			soup5 = BeautifulSoup(str(search4), "html.parser")
			print str(soup5.span['title'])
			count = count +1

print "\nTotal Number of Results : "+str(count)