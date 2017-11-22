#!/usr/bin/python

#Comando a utilizar:pfinalp1 <orden> <otros_parametros>

#<orden>
"""-crear: *.qcow2 y los ficheros de esp. XML
"qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 <name_VM>.qcow2 "
"cp plantilla-vm-p3.xml <name_VM>.xml"
Modificar el archivo <name_VM>.xml-bucle for y cambiar XXXX por lo que sea necesario
"sudo brct1 addbr LAN1"
"sudo brct1 addbr LAN2"
"sudo ifconfig LAN1 up"
"sudo ifconfig LAN2 up"
"""

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

"""-parar:
"virsh shutdown"
"""

"""-destruir:
"virsh destroy"
"rm -R" borrar ficheros creados
"""




import logging
from lxml import etree

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pfinalp1')
logger.debug('mensaje debug1')
logger.debug('mensaje debug2')

"Usar maquinas virtuales(Practica 2)"

""