#! /usr/bin/python

import os
import sys
import subprocess

def sec_file_transfer():

	# Congifure all the key properties here

	host_name = "192.168.0.27"
	h2 = ("ifconfig enp0s3 | grep 'inet\ addr' | cut -d: -f2|cut -d' ' -f1| tr -d '\n'")
	my_ip = subprocess.check_output(['bash', '-c', h2])
	response_re = os.system("ping -c 1 %s"%(host_name))
	if response_re==0:
		print "%s is up and running!"%(host_name)

		# Here is where the code executes : Transferring a file using Secure Copy Protocol

		command2 = os.system("sshpass -p 'Enigma10' scp '/home/shubha/Test_scp' shubha@%s:~"%(host_name))	# Change the machine's access credentials and location here
		if command2 == 0:
			print "File has been transferred successfully from %s to %s"%(my_ip,host_name)
			command3 = os.system(" sshpass -p 'Enigma10' ssh shubha@%s 'sshpass -p 'Enigma10' scp ~/Ack shubha@%s:~'"%(host_name,my_ip))
			if command3 == 0:
				print "Acknowledgement Received from %s to %s"%(host_name,my_ip)
			else:
				print "Acknowledgement NOT Received from %s to %s"%(host_name,my_ip)
		else:
			print "Transfer NOT Successful!"
	else:
		print "%s is down. Connection cannot be established!"%(host_name)

if __name__=="__main__":
	 sec_file_transfer()

