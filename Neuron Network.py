### IMPORTS ###
from random import *
#from math import *
from json import *



FILE = "chiffres.json"
with open(FILE, "r") as file:
    try: a = load(file)
    except: exit()


### CLASSES ###
class layer:
    def __init__(self, nbr, layerIndex):
        self.layer = []
        self.name = f"Layer {layerIndex}"
        if layerIndex == 1:
            for i in range(nbr):
                self.layer.append(neuron1(1, i))
        else:
            for i in range(nbr):
                self.layer.append(neuron(structure[-1], len(structure)+1, i))
        structure.append(self.layer)

class neuron1:
    def __init__(self, v, index):
        self.value = v
        self.name = f"Neuron L1 N{index+1}"

class neuron:
    def __init__(self, input, layer , index):
        self.value = 0
        self.biais = 0
        self.inputs = [ [n, 1] for  n in input ]
        self.name = f"Neuron L{layer} N{index+1}"

    def update(self):
        self.value = self.biais
        for ind, object in enumerate(self.inputs):
            weight = object[1]
            self.value += object[0].value * weight



### Functions ###
with open(FILE, "r") as file:
    donnees = load(file)

    if not donnees:
        exit()

    if len(donnees) < 2:
        structure = []

        nbr_layers = int(input("nbr layers  :\n"))
        nbr_neurons = [int(input(f"nbr neurons in layer {i + 1}:\n")) for i in range(nbr_layers)]
        for i in range(nbr_layers): layer(nbr_neurons[i], i + 1)
        print([[n.name for n in layer] for layer in structure])

        data = donnees[0]
        donnees = {"data" : data, "structure" : structure}

    else:
        data, structure = donnees["data"], list(donnees["structure"])
        for index, LAYER in enumerate(structure):
            LAYER = layer(len(LAYER)-1, index+1)
        for i, (input, neur) in enumerate(zip(data[0], structure[0])):
            neur = neuron1(input, i)


def changeLayer(layer, loss):
    for neuron in layer:
        for input in neuron.inputs:
            input[1] += (-1) ** randint(0, 1) * loss  # weights
        neuron.biais += (-1) ** randint(0, 1) * loss / 5  # biais
        print(neuron.name, neuron.value)

def update(answer):
    for layer in structure[1:]:
        print()
        for neuron in layer:
            neuron.update()
            print(neuron.name, neuron.value)

    result = structure[-1][0].value
    print(result)
    loss = (result - answer) / 100
    for layer in structure[1:]:
        changeLayer(layer, loss)

def train(donnees):
    for donnee in donnees:
        for i in range(50):
            update(donnee)



### Main ###
train(data)