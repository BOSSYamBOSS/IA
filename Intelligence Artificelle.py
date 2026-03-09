from random import *
from json  import *



change_rate = 10

def new_layer(previous_layer, number_neurons, role, index=0):return [
        role(
            [uniform(0, 0.5) for i in range(len(previous_layer))],
            previous_layer,
            index,
            _,
            uniform(-10, 10)
        )
        for _ in range(number_neurons)
    ]



def loaded_layer(previous_layer, number_neurons, index, weights, biaises, role):
    return [
        role( weights[_], previous_layer, index, _, biaises[_] )
        for _ in range(number_neurons)
    ]



class input_neuron:
    def __init__(self, index, value, layer=0):
        self.value = value
        self.name = f"L{layer} N°{index+1}"

class middle_neuron(input_neuron):
    def __init__(self, weights, inputs, layer, index, biais):
        super().__init__(index, 0, layer)
        self.weights = weights
        self.inputs = inputs
        self.biais = biais

class output_neuron(input_neuron):
    def __init__(self, weights, inputs, layer, index, biais):
        super().__init__(index, 0, layer)
        self.weights = weights
        self.inputs = inputs
        self.biais = biais



class structure:
    structure = []
    def update_inputs(self, input_values):
        for value, neuron in zip(input_values, self.structure[0]):
            neuron.value = value

    def save_structure(self, file_name):
        number_layers = len(self.structure) - 1
        number_neurons_par_layer = [len(layer) for layer in self.structure[1:]]
        weights = [[neuron.weights for neuron in layer] for layer in self.structure[1:]]
        biaises = [[neuron.biais   for neuron in layer] for layer in self.structure[1:]]
        input_values = [neuron.value for neuron in self.structure[0]]

        structure = [
            number_layers,
            number_neurons_par_layer,
            weights,
            biaises,
            input_values
        ]
        with open(file_name, "w") as file:
            dump(structure, file, indent=4)

    def recognize(self, new_inputs, inputs=None):
        if new_inputs:
            self.update_inputs(inputs)
        for layer in self.structure[1:]:
            for neuron in layer:
                neuron.value = sum([input.value * weight for input, weight in zip(neuron.inputs, neuron.weights) ]) + neuron.biais

        results = self.structure[-1]
        results2 = [neuron.value for neuron in results]
        maximum = max(results2)
        if maximum - 500 > 0:
            results2 = [val+500-maximum for val in results2]
        results3 = [e ** val for val in results2]
        return results2.index(max(results2)), results3

class new_structure(structure):
    def __init__(self, number_layers, number_neurons_per_layer, input_values):
        self.structure = []
        input_layer = [input_neuron(value, index) for index, value in enumerate(input_values)]
        self.structure.append(input_layer)
        for layer in range(1, number_layers):
            this_layer = new_layer(self.structure[-1], number_neurons_per_layer[layer], output_neuron if layer==number_layers-1 else middle_neuron, layer)
            self.structure.append(this_layer)

class loded_structure(structure):
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            structure = load(file)
            number_layers, number_neurons_per_layer, weights, biaises, input_values = structure

        self.structure = []
        input_layer = [input_neuron(value, index) for index, value in enumerate(input_values)]
        self.structure.append(input_layer)
        for layer in range(1, number_layers):
            this_layer = loaded_layer(self.structure[-1], number_neurons_per_layer[layer], layer, weights[layer], biaises[layer], output_neuron if layer==number_layers-1 else middle_neuron)
            self.structure.append(this_layer)



def train(IA, answer, trained=0):
    global change_rate

    result, results = IA.recognize(False)
    structure = IA.structure

    total = sum(results)

    results = [round(100 * val/total,  2) for val in results]


    if result == answer:
        change_rate -= 0.15
    else:
        change_rate += 0.1
        for layer in structure[1:]:
            for neuron in layer:
                neuron.biais += uniform(-1, 1) * change_rate
                for index in range(len(neuron.weights)):
                    neuron.weights[index] += uniform(-0.3, 0.3) * change_rate

    if results[answer] < 90 and trained < 900:
        return train(IA, answer, trained + 1)

    print(result, " : ", results[result], " %")
    print(answer, " : ", results[answer], " %")
    print()
    print()
    return structure



number_0 = [
    0, 1, 1, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 0, 1, 0,
    0, 1, 1, 1, 0
]

number_1 = [
    0, 0, 1, 0, 0,
    0, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 1, 1, 1, 0
]

number_2 = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
    1, 0, 0, 0, 0,
    1, 1, 1, 1, 1
]

number_3 = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 1,
    0, 0, 1, 1, 1,
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]

number_4 = [
    1, 0, 0, 0, 0,
    1, 0, 0, 0, 0,
    1, 0, 1, 0, 0,
    1, 1, 1, 1, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0
]

e = 2.7
IA = new_structure(3, [25, 30, 10], number_0)
for i in range(10):
    change_rate = 10
    print()
    print()
    print()
    for number, inputs in enumerate([number_0, number_1, number_2, number_3, number_4]):
        IA.update_inputs(inputs)
        IA.structure = train(IA, number, 0)
        IA.save_structure(f"IA_{number}.json")