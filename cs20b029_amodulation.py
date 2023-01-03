print('cs20b029')
import numpy as np, matplotlib.pyplot as plt

time = np.linspace(0, 1, 1000)
print(time)
am = 5; ac= 10; fm = 3; fc = 40
carrier = ac * np.sin(2 * np.pi * fc * time)
modulator = am * np.sin(2 * np.pi * fm * time)
# Amplitude Modulation
amodulation = (ac + modulator) * np.sin(2 * np.pi * fc * time)

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


# sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10 
# used to change the default python version to python3