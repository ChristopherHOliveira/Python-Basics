# valor de pi
pi = 3.14159

# entrada do raio da esfera
r = float(input("""Digite o raio da esfera (cm):
>>> """))

# entrada da densidade do material da esfera:
den = float(input("""
Digite a densidade do material (g/cm³):

|  Ar   ~0.001225 g/cm³  |--Exemplos 
|  Aerogel  ~0.02 g/cm³  |
|  Água     ~0.99 g/cm³  |
|  Alumínio  ~2.9 g/cm³  |
|  Ouro     ~19.3 g/cm³  |

>>> """))

# fórmula do volume:
vol = (4/3)*pi*r**3

# fórmula da massa:
mass = den*vol

# saída:
print(f"O volume da esfera de raio {r}cm é: {vol:.2f}cm³. A massa da esfera é: {mass:.2f}g.")
