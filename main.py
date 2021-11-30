# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:03:53 2021

@author: alonso
"""

from PIL import Image as img;
from numpy import asarray
import math

class image :
    def __init__ (self, route):
        self.route = route
        self.imagen = img.open(route)
    def img2data (self):
        data = asarray(self.imagen)
        return data
    def replace_data (self, data, message,binlist):
        i=0
        j=0
        k=0
        while i < len(binlist):
            k=0
            while k < 3 :
                data[j][k] += binlist[i]
                k +=1
                i +=1
            j+=1
        return data
    def Save_new_image(self,route):
        new_image=img.fromarray(self.data)
        new_image.save("moded.png")
        return True
    def extract_message(data, message_len):
        binlist = []
        for pixel in range(math.ceil(message_len/3)):
            for color in pixel:
                binlist.append(int(bin(color)[-1]))
        return binlist
        
    
        
            
class message  :
    def __init__(self,text):
        self.binlist=[]
        self.bitlist=[]
        self.text=text
        self.tex2bin(self.text)  
    def tex2bin (self,text):
        for letter in text:
            encode_letter=letter.encode()
            hexa_letter=encode_letter.hex()
            int_letter=int(hexa_letter, base=16)
            bin_letter=bin(int_letter)[2:]
            self.binlist.append(bin_letter)
            self.bitlist=[int(bit) for byte in self.binlist for bit in byte]
            
        return True

