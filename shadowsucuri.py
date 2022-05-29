#!/usr/share/python3

import crypt
import sys

if len(sys.argv) != 3:
	print("Modo de uso: python3 shadowsucuri.py <hashfile> <passlist>")
	sys.exit(0)

hash = open(sys.argv[1],"r")
passlist = open(sys.argv[2],"r")
passwd = list(passlist)




for n in list(hash):
	
	uname = n.split(':')[0]

	actualhash = n.split(":")[1].strip('\n')

	fractioned = actualhash.split("$")
	if fractioned[1] == "y":
		salt = "${}${}${}$".format(fractioned[1],fractioned[2],fractioned[3])
	else:
		salt = "${}${}$".format(fractioned[1],fractioned[2])


	for p in passwd:
		if crypt.crypt(p.strip('\n'),salt) == actualhash:
			print("{} - {}".format(uname,p))
