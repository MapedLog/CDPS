#!/usr/bin/python
import os
from lxml import etree
servers = ["lb", "c1","s1","s2","s3","s4","s5"]
for x in servers:
	#cargamos el fichero
	if x == "lb" :
		os.system("cp plantilla-vm-p3.xml "+ x +".xml")
		tree = etree.parse(x+'.xml')
		#name
		root = tree.getroot()
		name = root.find("name")
		name.text = x
		#devices
		source = root.find("./devices/disk/source")
		source.set("file", "./"+x+".qcow2")
		#bridge
		bridge = root.find("./devices/interface/source")
		bridge.set("bridge", "LAN1")
		f1 = open("./lb.xml","w")
		f1.write(etree.tostring(tree))
		f1.close()
		fxml1= open("./"+x+".xml","r")
		fxml2 = open("./cambio.xml","w")
		for line in fxml1 :
			if("</interface>") in line:
				fxml2.write(line)
				fxml2.write('<interface type="bridge">')
				fxml2.write('<source bridge="LAN2"/>')
				fxml2.write('<model type="virtio"/>')
				fxml2.write('</interface>')
			else :
				fxml2.write(line)
		fxml1.close()
		fxml2.close()
	elif x == "c1" :
		os.system("cp plantilla-vm-p3.xml "+ x +".xml")
		tree = etree.parse(x+'.xml')
		#name
		root = tree.getroot()
		name = root.find("name")
		name.text = x
		#devices
		source = root.find("./devices/disk/source")
		source.set("file", "./"+x+".qcow2")
		#bridge
		bridge = root.find("./devices/interface/source")
		bridge.set("bridge", "LAN1")
		f1 = open("./c1.xml","w")
		f1.write(etree.tostring(tree))
		f1.close()
	else:
		os.system("cp plantilla-vm-p3.xml "+ x +".xml")
		tree = etree.parse(x+'.xml')
		#name
		root = tree.getroot()
		name = root.find("name")
		name.text = x
		#devices
		source = root.find("./devices/disk/source")
		source.set("file", "./"+x+".qcow2")
		#bridge
		bridge = root.find("./devices/interface/source")
		bridge.set("bridge", "LAN1")
		f1 = open("./"+x+".xml","w")
		f1.write(etree.tostring(tree))
		f1.close()

				
