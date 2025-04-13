# Exercicio da tensão de resistores em série com uma CA

import matplotlib.pyplot as plt
import numpy as np

vrms = 220
freq = 100
per = 1/freq
quarto_de_per = per/4
vpico = vrms*np.sqrt(2) # valor pico a pico

tempo = np.linspace(0,3*per,300)

v_fonte = vpico*np.sin(2*np.pi*freq*tempo) # valor da fonte

# definindo resistência
r1 = 10000
r2 = 6000 
resist_equivalente = r1+r2

i = v_fonte/resist_equivalente # corrente
i_pico = vpico/resist_equivalente # corrente pico

#Tensões
v1 = r1 * i
v2 = r2 * i 

# Tensões pico
vp_r1 = r1*i_pico
vp_r2 = r2*i_pico


#plotando gráfico 1 (10k ohms)
plt.figure(1, figsize=(12, 8))
plt.plot(tempo, v1, label="Tensão no resistor (V)", color="orange")
plt.title("Tensão no resistor de 10k ohms")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.xticks(np.arange(0, tempo[-1] + quarto_de_per, quarto_de_per))
plt.yticks(np.arange(-vp_r1, vp_r1 + 1, vp_r1 / 4))
plt.legend()

#plotando gráfico 2 (6k ohms)
plt.figure(2, figsize=(12, 8))
plt.plot(tempo, v2, label="Tensão no resistor (V)", color="orange", )
plt.title("Tensão no resistor de 6k ohms")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.xticks(np.arange(0, tempo[-1] + quarto_de_per, quarto_de_per))
plt.yticks(np.arange(-vp_r2, vp_r2 + 1, vp_r2 / 4))
plt.legend()


plt.show()