import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de los años y los valores
years = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                  2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

values = np.array([21808.7, 23462.1, 24906.7, 29250.2, 33610.5, 35578, 34037.2, 
                   37425.1, 43154, 45873.8, 49259.2, 52224.3, 52883.7, 57507.7, 
                   59986.9, 62342, 66554.8, 64065.6, 82295, 93163.9, 102015.8])

# Usamos interpolación lineal entre los años 2019, 2020, y 2021
linear_interp = interp1d([2019, 2021], [66554.8, 82295], kind='linear')

# Calculamos el valor interpolado para 2020
interpolated_value_2020 = linear_interp(2020)

# Reemplazamos el valor de 2020 con el valor interpolado
values_corrected = values.copy()
values_corrected[17] = interpolated_value_2020

# Graficamos los datos originales y corregidos
plt.figure(figsize=(10, 6))
plt.plot(years, values, 'o-', label='Datos originales', color='blue')
plt.plot(years, values_corrected, 's--', label='Datos corregidos', color='red')
plt.axvline(2020, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('Año')
plt.ylabel('Valor (Millones de quetzales)')
plt.title('Interpolación Lineal para Modificar el Dato Atípico del 2020')
plt.legend()
plt.grid(True)
plt.show()

print(f'Valor interpolado para 2020: {interpolated_value_2020}')
