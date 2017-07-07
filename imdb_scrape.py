import urllib
import re

f=open("movie_metadata.csv")
cont=f.read().split("\n")
buffer=""
for entry in cont[1:101]:
	try:
		entry_temp=entry.split(",") 
		conn=urllib.urlopen(entry_temp[17])
		text=conn.read()
		trailerid=re.search(r'\/imdb\/vi([0-9]+)',text)
		description=re.search(r'temprop\=\"description\"\>[\n][\s]*(.*)[\n]',text)
		image_url=re.search(r'rel\=\'image\_src\'\ href\=\"(.*)\"',text)
		print trailerid.group(1)
		print description.group(1)
		print image_url.group(1)
		if (entry_temp[21]==""):
			entry_temp[21]="N/A"
		s=entry_temp[11]+":::"+description.group(1)+":::"+image_url.group(1)+":::"+trailerid.group(1)+":::"+entry_temp[1]+":::"+entry_temp[3]+":::"+entry_temp[21]
        	buffer=buffer+s+"\n"
	except Exception,e:
		print ("OOPS::"+entry)
		pass
	#s=entry_temp[3]+","+description.group(1)+","+image_url.group(1)+","+trailerid.group(1)
	#buffer=buffer+s+"\n"

target=open("movies_trailers.csv", 'w')
target.truncate()
target.write(buffer)
target.close()
