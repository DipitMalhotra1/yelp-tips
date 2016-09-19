import nltk
import json
import string
import re
#print "*****************************************************************Restaurant tips**************************************************************************************"
print "\n"
with open("yelp_academic_dataset_review.json") as f:
	f=open("yelp_academic_dataset_review.json")
	for line in f:
		line=line.rstrip()
		# print line
		# if re.search("[0-9]pm", line):
		# 	print line
		res= re.search("\.([^\.]*doctor[^\.]*)",line) 
		res1=re.search("\.([^\.]*between [0-9] pm[^\.]*)",line)


		if res is not None:
			x=str(res.group(1))
			if "available" in x:
				print "availability TIPS",x
			if "located" in x:
				print "Location TIPS",x 		

			
		if res1 is not None:
			y=str(res1.group(1))
			print "Timing PM",y
	print "********************************"


        	

