import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de los años y los valores corregidos
years = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                  2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

values_corrected = np.array([21808.7, 23462.1, 24906.7, 29250.2, 33610.5, 35578, 34037.2, 
                             37425.1, 43154, 45873.8, 49259.2, 52224.3, 52883.7, 57507.7, 
                             59986.9, 62342, 66554.8, 74424.9, 82295, 93163.9, 102015.8])

# Creamos la función de interpolación lineal
linear_interp = interp1d(years, values_corrected, kind='linear', fill_value='extrapolate')

# Predecimos los valores para 2024 y 2025
years_future = np.array([2024, 2025])
predicted_values = linear_interp(years_future)

# Unimos los años y valores históricos con los pronósticos
all_years = np.concatenate([years, years_future])
all_values = np.concatenate([values_corrected, predicted_values])

# Graficamos toda la serie de datos
plt.figure(figsize=(10, 6))
plt.plot(all_years, all_values, 'o-', label='Datos corregidos y pronóstico', color='blue')
plt.axvline(2024, color='gray', linestyle='--', alpha=0.6)
plt.axvline(2025, color='gray', linestyle='--', alpha=0.6)
plt.xlabel('Año')
plt.ylabel('Valor (Millones de quetzales)')
plt.title('Pronóstico de ingresos para 2024 y 2025 usando interpolación lineal')
plt.legend()
plt.grid(True)
plt.show()

# Mostramos los valores pronosticados
for year, value in zip(years_future, predicted_values):
    print(f'Pronóstico para {year}: {value:.2f} millones de quetzales')
