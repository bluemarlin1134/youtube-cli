import accurate

cmd = input("=>")


if  cmd.split()[0]== 'search':
	accurate.search('roses')

elif cmd.split()[0] == 'menu':
	print('menu')

elif cmd.split()[0] == 'autoplay':
	print('autoplay')

else:
	print('command not found')


