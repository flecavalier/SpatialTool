#!/usr/bin/env python
# encoding: utf-8
from pyo import *
import Variables as vars

#*************************************************************************************
# 22/05/2017 - Francis Lecavalier
# Suppression des fonctions bidons et ajout de fonctions appelant la nouvelle fonction OSCMove de "Surface.py".
# Les boules et leurs positions seront modifiées dans le fichier "Surface.py", afin de compartimenter
# davantage OSCServer.
#*************************************************************************************

class OSCServer:
    def __init__(self, port=1000):
        self.port = port
        #Dictionnaire avec fonctions associées à chaque message OSC reçu.
        self.bindings = {"/stickL/x": self.stickLeftXMove, "/stickL/y": self.stickLeftYMove, "/stickR/x": self.stickRightXMove, "/stickR/y": self.stickRightYMove, "/keyL1": self.onKeyL1, "/select": self.onSelectButton} # FL 04/09/17
        #Objet OscListener de Pyo permet de gérer l'OSC dans un thread indépendant de l'audio. On peut donc gérer l'OSC même si le moteur audio n'est pas démarré
        
        self.listen = OscListener(self._oscrecv, port)
        self.listen.start()
                
#        print "go!"
    # Fonction appelée à chaque fois qu'on message OSC est reçu
    def _oscrecv(self, address, *args):
        #print address, args
        # Si le message OSC est listé dans notre dictionnaire, on appele la fonction associée
        if address in self.bindings:
            # junXion retourne des tuples commes arguments OSC, même si on n'envoie qu'une seule valeur. On va donc chercher la première valeur du tuple (un float)
            self.bindings[address](args[0])
            
    # FL START 22/05/17
    def stickLeftXMove(self, data):
#        print "Left X: " + str(data)
        surface = vars.getVars("Surface")
        surface.OSCMove(0, x=data)
    
    def stickLeftYMove(self, data):
#        print "Left Y: " + str(data)
        surface = vars.getVars("Surface")
        surface.OSCMove(0, y=data)
        
    def stickRightXMove(self, data):
#        print "Right X: " + str(data)
        surface = vars.getVars("Surface")
        surface.OSCMove(1, x=data)
        
    def stickRightYMove(self, data):
#        print "Right Y: " + str(data)
        surface = vars.getVars("Surface")
        surface.OSCMove(1, y=data)
    #FL END 22/05/17
    
    # FL START 04/09/2017
    def onSelectButton(self, data):
        surface = vars.getVars("Surface")
        surface.modeChange()
    #FL END
    
    #JR 27 mai 2017
    def onKeyL1(self, data):
        print str(data)
