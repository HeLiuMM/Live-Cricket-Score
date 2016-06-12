#Run pip install requirements.txt in your terminal

#If not working,paste this into your terminal
# sudo apt-get install libxml2-dev libxslt1-dev python-dev
#Run the first step again

# To do
#1.Give option to change the match
#2.Create a graphical interace
#3.How to bundle the entire thing as one single file
#4.Give a proper message if net connection is not present
#5.Learn how the threading is actually working.


########## First Project/Script? ############

########### First Git Push 	##################
###############  By Helium 	############


import requests,bs4,subprocess,sys,threading
from time import sleep

def matches():
	print "-------------------------------------------------------------------------------"
	print "		   	     Welcome to Helium's live cricket score application				  "
	print "-------------------------------------------------------------------------------"

	print "\n These are the matches going on currently or are going to happen soon"
	print "------------------------------------------------------------------------"
	for index in range(len(All_Match)):
		print "{}.\t{}".format(index+1,All_Match[index].text)

def inp():
	print "Please enter the number corresponding to the match whose result you want to see"
	print "Press 0 if you want to exit the application"
	while(1):
		try:
			n=int(raw_input())
			if n in range(1,len(All_Match)+1):
				return n
			elif n==0:
				break
			else:
				print "Invalid Input.Please enter again"
		except:
			print "Invalid Inpuyt.Please enter again"
	sys.exit()

def score(Choice,Soup):
	link=Soup.select("guid")[Choice-1].text
	final_link=link[0:7] + link[11:]				#To remove www. from the url
	page_choice=requests.get(final_link)
	# connection_error(page_choice)
	soup_choice=bs4.BeautifulSoup(page_choice.text,"html.parser")
	return soup_choice.select("title")[0].text

def exit():
	print "Enter 0 if you want to quit else minimize and enjoy live score"
	while (1):
		A=raw_input()
		try:
			if(int(A) == 0):
				break
			else:
				print "Enter 0 if you want to quit"

		except:
			print "Enter 0 if you want to quit"

	sys.exit()

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def change():
	while (1):
		Score=score(User_Choice,Soup)
		sendmessage(Score)
		# exit()	
		sleep(40)						#Change the time as per your need

# def connection_error(page):
# 	try:
# 		page.raise_for_status()
# 	except:
# 		print "Check your web connection"
# 		sys.exit()
# or continue#
#------  Work on this ------#

if (__name__=="__main__"):
	Page = requests.get('http://static.cricinfo.com/rss/livescores.xml')
	# connection_error(Page)
	Soup=bs4.BeautifulSoup(Page.text,"lxml")
	All_Match=Soup.select("title")[1:]
	matches()
	User_Choice=inp()
	d=threading.Thread(target=exit)
	t=threading.Thread(target=change)
	t.setDaemon(True)
	d.start()
	t.start()
	
