# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:03:53 2021

@author: alonso
"""

from PIL import Image as img;

#class image :
 #   def __init__ (self, rute):
 #       self.rute = rute
 #       self.imagen = img.open(rute)
 #   def img2data (self):
 #       data = asarray(self.imagen)
 #       return data
 #   def replace_data (self, data, message):
 #       new_data = data
 #       i= 0
 #       for pixel in new_data:
 #           for color in pixel:
 #               color = color + message[i]
                
class message  :
    def __init__(self,text):
        self.binlist=[]
        self.text=text
        self.tex2bin(self.text)  
    def tex2bin (self,text):
        for letter in text:
            encode_letter=letter.encode()
            hexa_letter=encode_letter.hex()
            int_letter=int(hexa_letter, base=16)
            bin_letter=bin(int_letter)[2:]
            self.binlist.append(bin_letter)
        return True
