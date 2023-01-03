print('cs20b029')
import numpy as np, matplotlib.pyplot as plt

time = np.linspace(0, 1, 1000)
carrier = 10 * np.sin(2 * np.pi * 10 * time)
modulator = 5 * np.sin(2 * np.pi * 5 * time)
amodulation = 10 * np.sin(2 * np.pi * 10 * time + 5 * np.sin(2 * np.pi * 5 * time))

plt.subplot(3, 1, 1)
plt.plot(time, carrier)
plt.title('Carrier')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(time, modulator)
plt.title('Modulator')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(time, amodulation)
plt.title('AModulation')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
