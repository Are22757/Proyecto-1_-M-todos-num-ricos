import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de los años y los valores de ingresos tributarios
years = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                  2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

values = np.array([20280.7, 21974, 23310, 27238.1, 31543.3, 33358.1, 31811.7, 
                   34772, 40292.2, 42819.8, 46335.5, 49096.9, 49730.7, 54109.5, 
                   56684.1, 58835.6, 62593.6, 60279.4, 78019.1, 88579, 95547.8])

# Usamos interpolación lineal entre los años 2019, 2020, y 2021
linear_interp = interp1d([2019, 2021], [62593.6, 78019.1], kind='linear')

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
plt.ylabel('Ingresos tributarios (Millones de quetzales)')
plt.title('Interpolación Lineal para Modificar el Dato Atípico del 2020 (Ingresos tributarios)')
plt.legend()
plt.grid(True)
plt.show()

print(f'Valor interpolado para 2020: {interpolated_value_2020:.2f}')
