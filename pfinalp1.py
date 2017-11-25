#!/usr/bin/python
from subprocess import call
import logging
from lxml import etree
import os
import sys
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@ os.system("<comando a poner>")
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pfinalp1')
logger.debug('mensaje debug1')
logger.debug('mensaje debug2')
#Comando a utilizar:pfinalp1 <orden> <otros_parametros>
#import os os.system("<comando a poner>")
#####################################################<orden>###############################################################################
"""-crear: *.qcow2 y los ficheros de esp. XML
"qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 <name_VM>.qcow2 "
"cp plantilla-vm-p3.xml <name_VM>.xml"
Modificar el archivo <name_VM>.xml-bucle for y cambiar XXXX por lo que sea necesario
"sudo brct1 addbr LAN1"
"sudo brct1 addbr LAN2"
"sudo ifconfig LAN1 up"
"sudo ifconfig LAN2 up"
"""
"""Como los archivos originales .xml y .qcow2 ya estan copiados en una carpeta cuya localizacion estará situada donde el usuario del script 
quiera copiar dichos archivos
call(["mkdir /mnt/tmp/pfinal"])
call(["cd /mnt/tmp/pfinal"])"""
#La orden crear tendrá un parametro que será el numero de servidores que quiera crear el usuario que comprenderán entre 1 y 5 servidores
#En caso de superar dicho numero saltará un error y no se ejecutará el script
servers = []
if len(sys.argv) < 2 :
	print("Error, debe indicar una orden")
elif sys.argv[1]=="crear" :
	if len(sys.argv) < 3
		servers = ["lb", "c1","s1","s2"]
	elif sys.argv[2]=="1" :
		servers = ["lb", "c1","s1"]
	elif sys.argv[2]=="2" :
		servers = ["lb", "c1","s1", "s2"]
	elif sys.argv[2]=="3" :
		servers = ["lb", "c1","s1", "s2", "s3"]
	elif sys.argv[2]=="4" :
		servers = ["lb", "c1","s1","s2","s3","s4"]
	elif sys.argv[2]=="5" :
		servers = ["lb", "c1","s1","s2","s3","s4","s5"]	
	else :
		print("Error, debe indicar un número de servidores entre 1 y 5")
	if len(servers) > 0 :
		crear()
		fserver = open("./num_servers.txt", "w")
		fserver.write(len(servers)-2)
		fserver.close()
	#Si hay parámetros de más los ignoramos
elif sys.argv[1]=="arrancar" :
	if os.path.isfile("num_servers.txt") :
		server_create()
		arrancar()
	else :
		print("Error, debes crear antes de arrancar")
elif sys.argv[1]=="parar" :
	if os.path.isfile("num_servers.txt") :
		server_create()
		parar()
	else :
		print("Error, debes crear antes de parar")


#servers = ["lb", "c1","s1","s2","s3","s4","s5"]

# y si no van aqui estos 4 comandos van despues de haber copiado .xml y .qcow2

#if <orden> == crear :
def crear():
	for x in servers:
		os.system("qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 "+ x +".qcow2 ")
		os.system("cp plantilla-vm-p3.xml "+ x +".xml")
		#configurar fichero XML de cada maquina
		#lb xml
		#cargamos el fichero
	if x == "lb" :
		
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


	os.system("sudo brct1 addbr LAN1")
	os.system("sudo brct1 addbr LAN2")
	os.system("sudo ifconfig LAN1 up")
	os.system("sudo ifconfig LAN2 up")

	os.system("mkdir mnt")	
	for x in servers:
		os.system("sudo vnx_mount_rootfs -s r-r "+ x +".qcow2 mnt")
		###/etc/hostname
		f1 = open("./mnt/etc/hostname1", "w")
		f1.write(x)
		f1.close()
		
		if x == lb :
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f2 = open("./mnt/etc/network/interfaces", "w")
			f2.write("auto lo")
			f2.write("iface lo inet loopback")
			f2.write("auto eth0")
			f2.write("iface eth0 inet static")
			f2.write("address 10.0.1.1")
			f2.write("netmask 255.255.255.0")
			f2.write("auto eth1")
			f2.write("iface eth1 inet static")
			f2.write("address 10.0.2.1")
			f2.write("netmask 255.255.255.0")
			f2.close()
			f3 = open("./mnt/proc/sys/net/ipv4/ip_forward", "w")
			f3.write("1")
			f3.close()
		elif x == c1	:
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f2 = open("./mnt/etc/network/interfaces", "w")
			f2.write("auto lo")
			f2.write("iface lo inet loopback")
			f2.write("auto eth0")
			f2.write("iface eth0 inet static")
			f2.write("address 10.0.1.2")
			f2.write("netmask 255.255.255.0")
			f2.write("gateway 10.0.1.1")		
			f2.close()
		else:
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f2 = open("./mnt/etc/network/interfaces", "w")
			f2.write("auto lo")
			f2.write("iface lo inet loopback")
			f2.write("auto eth0")
			f2.write("iface eth0 inet static")
			if x = "s1" :
				f2.write("address 10.0.2.11")
			elif x = "s2" :
				f2.write("address 10.0.2.12")
			elif x = "s3" :
				f2.write("address 10.0.2.13")
			elif x = "s4" :
				f2.write("address 10.0.2.14")
			elif x = "s5" :
				f2.write("address 10.0.2.15")

			f2.write("netmask 255.255.255.0")
			f2.write("gateway 10.0.2.1")	
			f2.close()

		os.system("sudo vnx_mount_rootfs -u mnt")
	os.system("sudo ifconfig LAN1 10.0.1.3/24")
	os.system("sudo ip route add 10.0.0.0/16 via 10.0.1.1")

"""-arrancar:
Antes de arrancar cada maquina hay que configurarlas
"mkdir mnt"
"sudo vnx_mount_rootfs -s r-r <name_VM>.qcow2 mnt"
Modificar los ficheros /etc/hostname y /etc/network/interfaces(practica 2)
Terminar modificaciones
"sudo vnx_mount_rootfs -u mnt"
Balanceador de trafico como router-> Añadir línea "net.ipv4.ip_forward = 1" en el fichero /etc/systcl.conf
Habilitar los cambios "systcl -p /etc/systcl.conf"
"sudo virsh define <name_VM>.xml"
"sudo virsh start <name_VM>"
{"sudo virsh console <name_VM>"
"xterm -rv -sb -rightbar -fa  monospace -fs  10 -title  '<name_VM>' -e  'sudo virsh console <name_VM>'&"} hay que elegir entre estos dos comandos
"""
def arrancar():
	for x in servers:
		os.system("sudo virsh define "+ x +".xml")
		os.system("sudo virsh start "+ x)
		os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10 -title  '"+ x +"' -e  'sudo virsh console "+ x +"'&")
"""-parar:
"virsh shutdown"
"""
def parar():
	for x in servers:
		os.system("sudo virsh shutdown "+ x)

"""-destruir:
"virsh destroy"
"rm -R" borrar ficheros creados
"""
	def destruir():
		for x in servers:
			os.system("sudo virsh destroy "+ x)
			os.system("sudo rm -f " + x + ".qcow2")
			os.system("sudo rm -f " + x + ".xml")
			os.system("sudo rm -rf mnt")

