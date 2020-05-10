import webbrowser

#name input
name = input('What is your name?: ')
if name == "":
	print('''NO NAME
EXITING PROGRAM''')
	exit()

#intro
cd = input('''Welcome, ''' + name + '''! Do you prefer C or D? 
(both upper and lowercase characters are okay): ''')

#C/c input
if cd == "C" or "c": 
	print (name +' wants a print out of Oyster smiling.')
	webbrowser.open('https://www.youtube.com/watch?v=maAFcEU6atk')
 

#D/d input
elif cd == "D" or "d":
	print(name + ' wants to meet that dad.')
	webbrowser.open('https://www.youtube.com/watch?v=1g_UHV42jOA')

#otherwise
else:
	print ('''INVALID INPUT
EXITING PROGRAM''')