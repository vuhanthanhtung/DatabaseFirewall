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
    return result

def scan_update(string):
    result=""
    string=lower_string(string)
    if("\"update" in string):
        tmp_str1=string.split("\"update")[1]
        tmp_str=tmp_str1.split("\"")[0]
        tmp_str="update"+tmp_str
        result=tmp_str
    return result

def Del_space(string):
    return string.strip()

def split_multi_query(string):
    return Del_space(string).split(";")

def Del_comment(string):
    result=""
    if "//" in Del_space(string)[0:2]:
        return result
    if ";//" in Del_space(string):
        string=string.split(";//")[0]
        result=string+";"
        return result
    return string


#string="           zyx=\"select * from abc\" abc=\"select * from abc\"             "
#string="    abc=\"     select * from avxc \"          ;        "
#a=split_multi_query(string)
#print a

#result=Del_space(string)
#print result
result=[]
f = open("/var/www/html/basicwebsite/info.php","r").readlines()
for i in f:
    tmp=Del_comment(i)
    if (tmp == ""):
        continue
    else:
        i=tmp
    array = split_multi_query(i)
    if (len(array)!=1):
        for j in array:
            if (j!=""):
                if(scan_select(j)!= ""):
                    result.append(scan_select(j))

print result
