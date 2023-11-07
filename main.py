import numpy as np
import matplotlib.pyplot as plt



# Función de interpolación lineal en dos dimensiones
def interpolacion_lineal_2d(x1, y1, x2, y2, x, y, q11, q12, q21, q22):
  """
  Esta función realiza una interpolación lineal en dos dimensiones. 
  Toma como entrada los puntos de referencia (x1, y1), (x2, y2) y 
  los valores de esos puntos (q11, q12, q21, q22), así como las 
  coordenadas (x, y) en las que se desea realizar la interpolación.
  """

  # Cálculo del valor interpolado
  denominador = (x2 - x1) * (y2 - y1)
  primero = q11 * (x2 - x) * (y2 - y)
  segundo = q21 * (x - x1) * (y2 - y)
  tercero = q12 * (x2 - x) * (y - y1)
  cuarto = q22 * (x - x1) * (y - y1)

  # Fórmula principal de interpolación lineal
  resultado = (1 / denominador) * (primero + segundo + tercero + cuarto)
  return resultado


# Función para generar ruido Perlin en dos dimensiones

def octava_perlin_2d(frecuencia, amplitud, largo):
    #Se crea matriz ceros
    onda = np.zeros((largo, largo))
  
    longitud = largo // frecuencia
    for i in range(0, largo, longitud):
        for j in range(0, largo, longitud):
            # Crear los nodos de la onda
          onda[i, j] = (amplitud / 2) - (np.random.rand() * amplitud)
            # Interpolación entre nodos
          if i >= longitud and j >= longitud:
                for x in range(i - (longitud - 1), i):
                    for y in range(j - (longitud - 1), j):
                        x1, y1 = i - longitud, j - longitud
                        x2, y2 = i, j
                        onda[x, y] = interpolacion_lineal_2d(x1, y1, x2, y2, x,     
                        y,onda[x1,y1], onda[x1, y2], onda[x2, y1], onda[x2, y2])
    return onda

largo = 256
ruido_perlin2D = np.zeros((largo, largo))
n_octavas = 7

# Generar octavas de ruido Perlin en 2D y agregarlas
for i in range(1, n_octavas + 1):
    frec_actual = 2 ** i
    octava_2d = octava_perlin_2d(frec_actual, largo / frec_actual, largo)
    ruido_perlin2D += octava_2d

# Preparar los ejes X y Y
x = np.linspace(0, 1, largo)
y = np.linspace(0, 1, largo)
x, y = np.meshgrid(x, y)

# Preparar el terreno en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, ruido_perlin2D, cmap='terrain') 
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()

'''
Para cambiar colores reemplazar valor cmap por: terrain, ocean, gray, magma, plasma.
'''