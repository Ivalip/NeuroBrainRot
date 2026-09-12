class Neuron:
    def __init__(self, k, b):
        self.k = k
        self.b = b
    def convert(self, x):
        return [-1 if i == 0 else i for i in x]
    def solve(self, x):
        converted_x = self.convert(x)
        S = sum([xn*kn for xn,kn in zip(self.k,converted_x)]) - self.b
        self.activate(S)
    def activate(self, S):
        self.out = True if S == 0 else False

n_list = [Neuron([1,1,1,1,1,1,-1], 7), #0
    Neuron([1]*7, -3), #1
    Neuron([1,1,2,1,1,2,1], 1), #2
    Neuron([1,1,1,1,-2,-2,1], 9), #3
    Neuron([1]*7, 1), #4
    Neuron([1,-2,1,1,-2,1,1], 9), #5
    Neuron([1,-1,1,1,1,1,1], 7), #6
    Neuron([1]*7, -1), #7
    Neuron([1]*7, 7), #8
    Neuron([1,1,1,1,-2,1,1], 8) #9
]

c = [
[1,1,1,1,1,1,0], #0
[0,1,1,0,0,0,0], #1
[1,1,0,1,1,0,1], #2
[1,1,1,1,0,0,1], #3
[0,1,1,0,0,1,1],
[1,0,1,1,0,1,1],
[1,0,1,1,1,1,1],
[1,1,1,0,0,0,0],
[1,1,1,1,1,1,1],
[1,1,1,1,0,1,1],
[0,0,0,0,0,0,0]
]

for j in range(len(c)):
    print(f'Число {j}: {c[j]}.')
    res = []
    flag = 0
    for i in range(len(n_list)):
        n_list[i].solve(c[j])
        if (n_list[i].out):
            print(f"Введённое число: {i}")
            break
        elif (i == len(n_list)-1):
            print("Число неопознано")
    print()