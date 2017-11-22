"Comando a utilizar:pfinalp1 <orden> <otros_parametros>"
"""<orden>
-crear: *.qcow2 y los ficheros de esp. XML
"qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 <name_VM>.qcow2 "
"cp plantilla-vm-p3.xml <name_VM>.xml"
Modificar el archivo <name_VM>.xml
"sudo brct1 addbr LAN1"
"sudo brct1 addbr LAN2"
"sudo ifconfig LAN1 up"
"sudo ifconfig LAN2 up"
-arrancar:
"sudo virsh define <name_VM>.xml"
"sudo virsh start <name_VM>"
"sudo virsh console <name_VM>"
"xterm -rv -sb -rightbar -fa  monospace -fs  10 -title  's1' -e  'sudo virsh console s1'&"
-parar:
-destruir:
"""


#!/usr/bin/python

import logging
from lxml import etree

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pfinalp1')
logger.debug('mensaje debug1')
logger.debug('mensaje debug2')

"Usar maquinas virtuales(Practica 2)"

""