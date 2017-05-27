def get_summ(something, something_else, delim=' '):
	upper_someting=str(something).upper()
	upper_delim=str(delim)
	upper_someting_else=str(something_else).upper()
	return upper_someting+upper_delim+upper_someting_else


print(get_summ('str1','str2','__'))
print(get_summ(2,'str2'))  
print(get_summ('str2',2))
print(get_summ(2,2))
#print(str("sdcsdcds"))