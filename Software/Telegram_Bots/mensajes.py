########################################################################
#
# Plantilla de mensajes basicos del bot de Telegram
# Ing. Mauricio Martinez Montero
# LabDet, Criogenia. Instituto de Ciencias Nucleares, UNAM.
#
# Pequeña plantilla que contiene los mensajes y que se encarga de devolver 
# el mensaje correspondiente a los botones declarados en el programa
# principal 'main' 
#
#
########################################################################

# Mensajes para responeder en kali bot
msg_uno="Dentro de esta funcion podemos poner algun un mensaje de texto en pantalla. \
    \n\nPor ejemplo: \
    \n\nInformacion sobre lo que este bot puede hacer por ti \
    \n\nMensajes de ayuda, sobre como utilizar el bot.\
    \n\nEl resultado de algun analisis.  \
    \n\nPedir algun tipo de informacion al usuario, etc"
    
msg_dos='Este es un ejemplo usando una funcion que devuelve una tabla usando Pandas, en donde tenemos renglones (0,1,2) y columnas (a,b,c).\n\n'

msg_tres="sigo pensando aun que podemos hacer en este boton. Que se te ocurre, escribelo abajo ;)"

# Diccionario en el que vamos a asocioar los botones declarados en el main
# con  los mensajes que queremos que se desplieguen al ser accionados.

mensajes={'boton1':msg_uno,\
         'boton2':msg_dos,\
         'boton3':msg_tres}

# Funcion que devolvera el contenido del mensaje cuando se haya accionado un boton
def output_mensajes(boton):
    # esta funcion solo devueve strings pero puede devolver cualquier cosa que 
    # sea programada dentro de ella 
    return mensajes[boton]
