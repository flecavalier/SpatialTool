#!/usr/bin/env python
# encoding: utf-8
from pyo import *

# Fonctions bidons pour fins de tests
def function1(data):
    print "Left X: " + str(data)
    
def function2(data):
    print "Left Y: " + str(data)
    
def function3(data):
    print "Right X: " + str(data)
    
def function4(data):
    print "Right Y: " + str(data)
    
class OSCServer:
    def __init__(self):
        #Dictionnaire avec fonctions associées à chaque message OSC reçu.
        self.bindings = {"/stickL/x": function1, "/stickL/y": function2, "/stickR/x": function3, "/stickR/y": function4}
        #Objet OscListener de Pyo permet de gérer l'OSC dans un thread indépendant de l'audio. On peut donc gérer l'OSC même si le moteur audio n'est pas démarré
        self.listen = OscListener(self._oscrecv, 5555)
        self.listen.start()
        
    # Fonction appelée à chaque fois qu'on message OSC est reçu
    def _oscrecv(self, address, *args):
        # print address, args
        # Si le message OSC est listé dans notre dictionnaire, on appele la fonction associée
        if address in self.bindings:
            # junXion retourne des tuples commes arguments OSC, même si on n'envoie qu'une seule valeur. On va donc chercher la première valeur du tuple (un float)
            self.bindings[address](args[0])
                 
s = Server().boot()
osc = OSCServer()
s.gui(locals())