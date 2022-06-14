str1="my name is awais"
print(len(str1))
print(str1[4:11:1])#[starting index:ending index+1:print every nth alphabet ][1:2:3] if  1 is empty its=0 if 2 is empty  its=length   if 3 empty it=1
print(str1[-4:-2])# ==[7:9] *minus values counts from end of string
print(str1[::-1])# ==[7:9] *minus n in  3rd value will  print every nth alphabet in reverse  order
print(type(str1))# type(variable) is data type of variable
#there are *is* functions which give true false acccording to string condition eg
print(str1.isalpha())# space  is not alphabet
print(str1.endswith("ngs"))# check is given string is present at most end of  variablle  str
print(str1.count(" "))#counts parameter in string
#many other functions find from google *string funtions python