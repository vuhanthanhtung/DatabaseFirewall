import os
import glob
import optparse
import pyfiglet
asciiart = pyfiglet.figlet_format("Dataabase Firewall")

def lower_string(string):
    	return string.lower()

def scan_select(string):
    	result=""
    	string=lower_string(string)
    	if ("\"select" in string):
    		tmp_str1=string.split("\"select")[1]
#        tmp_str2=string.split("\";")[1]
        	tmp_str=tmp_str1.split("\"")[0]
        	tmp_str="select"+tmp_str
        	result=tmp_str
	if ("\'select" in string):
        	tmp_str1=string.split("\'select")[1]
        	tmp_str=tmp_str1.split("\'")[0]
        	tmp_str="select"+tmp_str
        	result=tmp_str

#        if(tmp_str2==""):
#            return result
#        tmp=scan_select(tmp_str2)
#        result.append(tmp)

    	return result

def scan_insert(string):
    	result=""
    	string=lower_string(string)
    	if("\"insert" in string):
        	tmp_str1=string.split("\"insert")[1]
        	tmp_str=tmp_str1.split("\"")[0]
        	tmp_str="insert"+tmp_str
        	result=tmp_str
	if ("\'insert" in string):
        	tmp_str1=string.split("\'insert")[1]
        	tmp_str=tmp_str1.split("\'")[0]
        	tmp_str="insert"+tmp_str
        	result=tmp_str

    	return result

def scan_update(string):
    	result=""
    	string=lower_string(string)
    	if("\"update" in string):
        	tmp_str1=string.split("\"update")[1]
        	tmp_str=tmp_str1.split("\"")[0]
        	tmp_str="update"+tmp_str
        	result=tmp_str
	if ("\'update" in string):
        	tmp_str1=string.split("\'update")[1]
        	tmp_str=tmp_str1.split("\'")[0]
        	tmp_str="update"+tmp_str
        	result=tmp_str

    	return result

def Del_space(string):
    	return string.strip()

def Del_all_space(string):
    	return string.replace(" ","")

def Replace_spaces_to_1_space(string):
    	while ("  " in string):
        	string=string.replace("  "," ")
    	return string

def split_multi_query(string):
    	return Del_space(string).split(";")

def Del_comment(string):   
    	result=""
	string=Replace_spaces_to_1_space(string)
    	if "//" in Del_space(string)[0:2]:
        	return result
    	if "; //" in Del_space(string):
        	string=string.split("; //")[0]
        	result=string+";"
        	return result	
    	if ";//" in Del_space(string):
        	string=string.split(";//")[0]
        	result=string+";"
        	return result
    	return string

def Del_html(string):
    	result=""
    	a=Del_all_space(string)
    	if (a[0]=="<"):
        	return result
    	return string

def check_sub_comma(string):
    	flag=0
    	string=Del_space(string)
    	if (string[-1]!=";"):
        	flag=1
    	return flag

def scanfile(file):
	result=[]
	save =""
	file = open(file,"r")
	result.append(os.path.basename(file.name))
	f = file.readlines()
	for i in f:
		if (Del_space(i) ==""):
			continue
    		tmp=Del_comment(i)
		if (tmp == ""):
		        continue
		else:
			i=tmp
    		tmp=Del_html(i)
    		if (tmp == ""):
        		continue
    		else:
        		i=tmp
    		if (check_sub_comma(i)==1):
        		save=save + " " +Del_space(i).replace("\n"," ")
        		#print save
        		continue
    		else:
        		save=save + " " +Del_space(i).replace("\n"," ")
    		#print save
    		if (save!=""):
        		array = split_multi_query(save) 
    		if (len(array)!=1):
        		for j in array:
        	    		if (j!=""):
                ####### solve the problem space in string such as abc=" select/insert/update fdsfsdfsdf";
        	        		j=Replace_spaces_to_1_space(j)
        	        		if ("\" " in j):
                	    			j=j.replace("\" ","\"")
			                if ("\' " in j):
	      		                        j=j.replace("\' ","\'")

                			j=Del_space(j)
                		if(scan_select(j)!= ""):
                	    		result.append(scan_select(j))
                		if(scan_insert(j)!= ""):
                	    		result.append(scan_insert(j))
                		if(scan_update(j)!= ""):
                	    		result.append(scan_update(j))
    		save=""
	print result

# Getting the current work directory (cwd)
# r=root, d=directories, f = files
#####################################################
#Code parsearg
usage = "usage: %prog -F framework -d directory -f file"
parser = optparse.OptionParser(usage=usage)
print asciiart
parser.add_option('-d', action="store", dest="directory", default="None",
                help="Path to directory of web application")
parser.add_option('-F', action="store", dest="framework",
                help="Choose the framework", default="PHP")
parser.add_option('-f', action="store", dest="file",
                help="Path to file of web application", default="None")
options, args = parser.parse_args()
if options.directory=="None" and options.file=="None":
	parser.error('Path not given')
directory = options.directory
file = options.file
Checkdir = 0
Checkfile = 0
if os.path.isdir(directory):
	Checkdir = 1
if os.path.isfile(file):
	Checkfile = 1
#####################################################
listfiles=[]
Result = 0
if Checkdir == 1:
	for r, d, f in os.walk(directory):
		for files in f:
			if ".php" in files:
				listfiles.append(os.path.join(r, files))
	Result +=1
elif directory == "None":
	Result +=1
else:
	print "Path to directory not found"
if Checkfile == 1:
	listfiles.append(file)
	Result +=1
elif file == "None":
        Result +=1
else:
	print "Path to file not found"
if Result == 2:
	print listfiles
	for i in listfiles:
		scanfile(i)


