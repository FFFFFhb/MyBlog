import re         


def hello():
	print ('check emails')


def emails(e):
    if len(e)>= 5:
        if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]",e) !=None: 
        	return '邮箱格式正确！'

    return '邮箱格式有误'

