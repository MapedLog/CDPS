#!/usr/bin/python
from subprocess import call
#Comando a utilizar:pfinalp1 <orden> <otros_parametros>

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
crear_numServers = y #numero que viene como parametro
servers = ["lb", "c1"]
for i in range(1,crear_numServers):
	servers.append("s"+i)
call(["mkdir mnt"])	
# y si no van aqui estos 4 comandos van despues de haber copiado .xml y .qcow2
call(["sudo brct1 addbr LAN1"])
call(["sudo brct1 addbr LAN2"])
call(["sudo ifconfig LAN1 up"])
call(["sudo ifconfig LAN2 up"])
for x in servers:
	def crear(x):
		call(["qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 "+ x +".qcow2 "])
		call(["cp plantilla-vm-p3.xml "+ x +".xml"])
		call(["sudo vnx_mount_rootfs -s r-r "+ x +".qcow2 mnt"])
		if(x == (s1 or s2 or s3 or s4 or s5) ):
			###/etc/hostname
			f1 = ("/etc/hostname", "r")
			f2 = ("/etc/hostname1", "w")
			for line in f1:
				f2.write(line)
			f2.write()
			f1.close()
			f2.close()
			call(["mv /etc/hostname /etc/hostname.old"])
			call(["mv /etc/hostname1 /etc/hostname"])
			call(["rm /etc/hostname.old"])
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f3 = ("/etc/network/interfaces", "r")
			f4 = ("/etc/network/interfaces1", "w")
			for line in f3:
				f4.write("")
			f4.write("")	
			f3.close()
			f4.close()
			call(["mv /etc/network/interfaces /etc/network/interfaces.old"])
			call(["mv /etc/network/interfaces1 /etc/network/interfaces"])
			call(["sudo vnx_mount_rootfs -u mnt"])
		else if x == lb :
			###/etc/hostname
			f1 = ("/etc/hostname", "r")
			f2 = ("/etc/hostname1", "w")
			for line in f1:
				f2.write(line)
			f2.write()
			f1.close()
			f2.close()
			call(["mv /etc/hostname /etc/hostname.old"])
			call(["mv /etc/hostname1 /etc/hostname"])
			call(["rm /etc/hostname.old"])
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f3 = ("/etc/network/interfaces", "r")
			f4 = ("/etc/network/interfaces1", "w")
			for line in f3:
				f4.write("")
			f4.write("")	
			f3.close()
			f4.close()
			call(["mv /etc/network/interfaces /etc/network/interfaces.old"])
			call(["mv /etc/network/interfaces1 /etc/network/interfaces"])
			call(["sudo vnx_mount_rootfs -u mnt"])
		else if x == c1	:
			###/etc/hostname
			f1 = ("/etc/hostname", "r")
			f2 = ("/etc/hostname1", "w")
			for line in f1:
				f2.write(line)
			f2.write()
			f1.close()
			f2.close()
			call(["mv /etc/hostname /etc/hostname.old"])
			call(["mv /etc/hostname1 /etc/hostname"])
			call(["rm /etc/hostname.old"])
			#/etc/network/interfaces Dos formas o p2(para siempre) o p3( no es permanente: al rearrancar se pierden)
			f3 = ("/etc/network/interfaces", "r")
			f4 = ("/etc/network/interfaces1", "w")
			for line in f3:
				f4.write("")
			f4.write("")	
			f3.close()
			f4.close()
			call(["mv /etc/network/interfaces /etc/network/interfaces.old"])
			call(["mv /etc/network/interfaces1 /etc/network/interfaces"])
			call(["sudo vnx_mount_rootfs -u mnt"])


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
	def arrancar(x):
		call(["sudo virsh "+ x +".xml"])
		call(["sudo virsh console "+ x])
		call(["xterm -rv -sb -rightbar -fa  monospace -fs  10 -title  '"+ x +"' -e  'sudo virsh console "+ x +"'&"])
"""-parar:
"virsh shutdown"
"""
	def parar(x):
		call (["sudo virsh shutdown"])

"""-destruir:
"virsh destroy"
"rm -R" borrar ficheros creados
"""
	def destruir():
		call(["sudo virsh destroy"])

import logging
from lxml import etree

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pfinalp1')
logger.debug('mensaje debug1')
logger.debug('mensaje debug2')

"Usar maquinas virtuales(Practica 2)"

""