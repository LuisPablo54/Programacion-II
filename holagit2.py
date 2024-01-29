# Importa la biblioteca NumPy con el alias np
import numpy as np

# Imprime el valor máximo positivo que se puede representar con el tipo de dato float
print(np.finfo(float).max)

# Imprime el valor mínimo positivo que se puede representar con el tipo de dato float
print(np.finfo(float).min)

# Imprime el valor del epsilon de la máquina para el tipo de dato float
print(np.finfo(float).eps)
