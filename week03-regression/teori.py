import numpy as np
import matplotlib.pyplot as plt

# Data
diameter_pizza = np.array([6, 8, 10, 14, 18])
harga_pizza = np.array([7, 9, 13, 17.5, 18])

# Estimasi parameter
beta_0 = 1.82
beta_1 = 0.974

# Model regresi
harga_prediksi = beta_0 + beta_1 * diameter_pizza

# Membuat plot
plt.scatter(diameter_pizza, harga_pizza, label='Data Asli')
plt.plot(diameter_pizza, harga_prediksi, color='red', label='Model Regresi')
plt.xlabel('Diameter Pizza (inci)')
plt.ylabel('Harga Pizza (dolar)')
plt.title('Simple Linear Regression: Hubungan Diameter Pizza dengan Harga Pizza')
plt.legend()
plt.grid(True)
plt.show()
