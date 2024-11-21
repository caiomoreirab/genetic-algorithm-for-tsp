import numpy as np
from mealpy import GA
from mealpy.utils.space import PermutationVar
from scipy.spatial.distance import euclidean
from random import sample


# Função para carregar coordenadas do arquivo TSP
def load_tsp_file(filename):
    cities = []
    with open(filename, 'r') as file:
        section = False
        for line in file:
            if line.strip() == "NODE_COORD_SECTION":
                section = True
            elif line.strip() == "EOF":
                break
            elif section:
                parts = line.strip().split()
                if len(parts) >= 3:
                    cities.append((float(parts[1]), float(parts[2])))
    return cities




# Função para calcular a distância total de uma rota (solução)
def total_distance(solution, cities):
    #print(solution)
    #input()
    distance = 0
    for i in range(len(solution) - 1):
        city_a = cities[int(solution[i])]  # Garantir que o índice seja inteiro
        city_b = cities[int(solution[i + 1])]  # Garantir que o índice seja inteiro
        distance += euclidean(city_a, city_b)
    # Voltar para a cidade inicial
    distance += euclidean(cities[int(solution[-1])], cities[int(solution[0])])
    return distance  #retorna uma distancia total  >> exemplo: 52532.74341278401 




# Função objetivo para o TSP
def objective_function(solution):
    return total_distance(solution, cities)



# Função que gera uma permutação aleatória das cidades (solução inicial)
def init_permutation_solution(n_cities):
    print(n_cities)
    input()
    return np.random.permutation(n_cities).tolist()

# Função de mutação do tipo Scramble
def scramble_mutation(solution):
    idx1, idx2 = sorted(sample(range(len(solution)), 2))
    sublist = solution[idx1:idx2]
    np.random.shuffle(sublist)  # Embaralhar os elementos
    solution[idx1:idx2] = sublist
    return solution

# Carregar as coordenadas das cidades do arquivo
filename = 'ch150.tsp'  # Ajuste este nome de acordo com seu arquivo
cities = load_tsp_file(filename)

# Definição do problema (usando permutações das cidades)
n_cities = len(cities)
problem_dict = {
    "bounds": PermutationVar(np.arange(n_cities)),  # Definido para permutações das cidades
    "obj_func": objective_function,
    "minmax": "min",
}

# Configuração do modelo GA com os parâmetros fornecidos
model = GA.BaseGA(
    epoch=10000,
    pop_size=50,
    pc=0.9,
    pm=0.05,
    selection="tournament",
    k_way=0.4,
    crossover="multi_points"
)

# Inicializar soluções (população) como permutações aleatórias
model.create_solution = lambda: init_permutation_solution(n_cities)
# Sobrescrevendo a função de mutação com a mutação Scramble
model.mutation = scramble_mutation

# Resolver o problema
g_best = model.solve(problem_dict)

# Exibir a solução final e a distância total
print(f"Solution (Route): {g_best.solution}")
print(f"Total Distance: {g_best.target.fitness}")

