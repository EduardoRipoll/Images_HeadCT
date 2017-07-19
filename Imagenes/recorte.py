# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:03:08 2017

El siguiente programa toma como input imagenes 512x512 y como output imagenes recortadas 217x262 renombradas,
para su procesamiento en una CNN donde en todas las imagenes se quiere recortar siempre la misma región
@author: Eduardo
"""

from PIL import Image
i=1

while True:
    
    imagen = Image.open("head ("+str(i)+").jpg")

# Define tupla con región
    caja = (148, 96, 365, 358)

# Obtener de la imagen original la región de la caja
    region = imagen.crop(caja)  

# Guarda la imagen obtenida con el formato JPEG.
    region.save("cabeza_"+str(i)+".jpg")
    
    i+=1