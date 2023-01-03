print('cs20b029')
import numpy as np, matplotlib.pyplot as plt

time = np.linspace(0, 1, 1000)            # time vector
am = 5; ac= 9; fm = 2.5; fc = 35            # amplitude and frequency of modulator and carrier
carrier = ac * np.sin(2 * np.pi * fc * time) # Ac * cos(2*pi*fc*t)
modulator = am * np.sin(2 * np.pi * fm * time) # Am * cos(2*pi*fm*t)
# Amplitude Modulation
amodulation = (ac + modulator) * np.sin(2 * np.pi * fc * time) # Am = (Ac + m(t)) * cos(2*pi*fc*t)

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
# set the whole title to "AM_CNlab1"
plt.suptitle('AM_CNlab1')
plt.show()
