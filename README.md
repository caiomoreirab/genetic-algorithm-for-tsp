# **Traveling Salesman Problem (TSP) Solver using Genetic Algorithm**

Este projeto implementa um solucionador para o **Problema do Caixeiro Viajante (TSP)\*\* utilizando um **Algoritmo Genético (GA)**. Ele permite carregar instâncias do problema em formato `.tsp\` e encontrar uma rota otimizada para minimizar a distância total percorrida.

## 🚀 **Funcionalidades**
- Suporte a arquivos `.tsp` no formato **TSPLIB**.
- Implementação de um Algoritmo Genético personalizável.
- Operador de mutação avançado: **Scramble Mutation**.
- Resultados detalhados, incluindo a melhor rota encontrada e sua distância total.

## 🛠️ **Tecnologias Utilizadas**
- \*\*Python\*\* (versão 3.8+)
- [\*\*Mealpy\*\*](https://github.com/thieu1995/mealpy): Biblioteca de algoritmos de otimização.
- [\*\*SciPy\*\*](https://scipy.org/): Para cálculo de distâncias euclidianas.
- [\*\*NumPy\*\*](https://numpy.org/): Para manipulação de arrays.

## 📂 \**Estrutura do Projeto**
```
.
├── main.py             # Script principal para execução do GA
├── ch150.tsp           # Exemplo de instância TSP
├── README.md           # Documentação do projeto
└── requisitos.txt      # Dependências do projeto
```

## 🧑‍💻 **Como Executar o Projeto**

### **Pré-requisitos**
1. Certifique-se de ter o Python 3.8+ instalado.
2. Instale as dependências com o comando:
   ```
   pip install -r requirements.txt
   ```

### **Execução**
1. Insira sua instância do problema TSP no formato `.tsp`.
2. Altere o nome do arquivo na variável `filename` no código, se necessário.
3. Execute o script:
   ```
   python main.py
   ```

**O resultado exibirá:**
- A melhor rota encontrada.
- A distância total dessa rota.

**Exemplo de saída:**
```
Solution (Route): [0, 5, 12, 7, ..., 0]
Total Distance: 12543.67
```

## 📋 **Formato do Arquivo TSP**
O projeto suporta arquivos no formato **TSPLIB**, como o exemplo abaixo:
```
NAME : ch150
TYPE : TSP
DIMENSION : 150
NODE_COORD_SECTION
1 20833.3333 17100.0000
2 20900.0000 17066.6667
...
EOF
```
Certifique-se de que o arquivo contém os trechos `NODE_COORD_SECTION` e `EOF`.

## ⚙️ **Algoritmo Genético: Configurações**
- **População**: 50 indivíduos
- **Épocas**: 10.000
- **Probabilidade de cruzamento**: 90%
- **Probabilidade de mutação**: 5%
- **Seleção**: Torneio (com parâmetro k=0.4)

### **Operadores Personalizados**
- **Crossover**: Multipontos.
- **Mutação**: Scramble Mutation.

## 🛠️ **Personalização**

### **Operador de Mutação**
A mutação padrão foi substituída por uma mutação do tipo \*\*Scramble\*\*.
Para usar outra estratégia, modifique a função \`scramble_mutation\`.

### **Critérios de Parada**
Atualmente, o algoritmo para após 10.000 épocas. Para outros critérios, modifique o parâmetro `epoch` ou implemente condições de convergência.

## 📊 **Resultados e Visualização**
Embora este projeto não inclua visualizações, você pode utilizar bibliotecas como o **Matplotlib** para traçar o percurso da rota encontrada.

**Exemplo de gráfico:**
```python
import matplotlib.pyplot as plt

# Plota as cidades e a rota
route = g_best.solution
x = [cities[int(i)][0] for i in route]
y = [cities[int(i)][1] for i in route]
plt.plot(x + [x[0]], y + [y[0]], marker='o')
plt.title("Melhor Rota Encontrada")
plt.show()
```

## 📈 **Possíveis Melhorias**
- Implementação de operadores de crossover mais avançados, como **Order Crossover (OX)**.
- Adição de **elitismo** para preservar as melhores soluções ao longo das gerações.
- Integração com algoritmos híbridos (ex.: Busca Local após o GA).

## 📜 **Licença**
Este projeto está licenciado sob uma licença do **MIT**.

## 🤝 **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**.

---

Desenvolvido com 💻 por Caio Moreira
