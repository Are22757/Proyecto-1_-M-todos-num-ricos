import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de los años y los valores no tributarios y transferencias
years = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                  2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

values = np.array([1468.7, 1487.5, 1571, 1976.7, 2040.3, 2188.9, 2214.2, 2625.4, 
                   2849, 3035.3, 2194.8, 3120.2, 3126.9, 3393.9, 3299.5, 3503.6, 
                   3957.6, 3783.9, 4093.2, 4461, 6378.2])

# 1. Interpolación para 2013 (entre 2012 y 2014)
linear_interp_2013 = interp1d([2012, 2014], [3035.3, 3120.2], kind='linear')
interpolated_value_2013 = linear_interp_2013(2013)

# 2. Interpolación para 2016 (entre 2015 y 2017)
linear_interp_2016 = interp1d([2015, 2017], [3126.9, 3299.5], kind='linear')
interpolated_value_2016 = linear_interp_2016(2016)

# 3. Interpolación para 2019 (entre 2018 y 2020)
linear_interp_2019 = interp1d([2018, 2020], [3503.6, 3783.9], kind='linear')
interpolated_value_2019 = linear_interp_2019(2019)

# Reemplazamos los valores atípicos con los valores interpolados
values_corrected = values.copy()
values_corrected[10] = interpolated_value_2013  # 2013
values_corrected[13] = interpolated_value_2016  # 2016
values_corrected[16] = interpolated_value_2019  # 2019

# Graficamos los datos originales y corregidos
plt.figure(figsize=(10, 6))
plt.plot(years, values, 'o-', label='Datos originales', color='blue')
plt.plot(years, values_corrected, 's--', label='Datos corregidos', color='red')
plt.axvline(2013, color='gray', linestyle='--', alpha=0.6)
plt.axvline(2016, color='gray', linestyle='--', alpha=0.6)
plt.axvline(2019, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('Año')
plt.ylabel('No tributarios y transferencias (Millones de quetzales)')
plt.title('Corrección de datos atípicos con trazadores lineales')
plt.legend()
plt.grid(True)
plt.show()

# Mostramos los valores interpolados
print(f'Valor interpolado para 2013: {interpolated_value_2013:.2f}')
print(f'Valor interpolado para 2016: {interpolated_value_2016:.2f}')
print(f'Valor interpolado para 2019: {interpolated_value_2019:.2f}')
