import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

def linear_through_origin(x: None, m: None):
    return m * x

times = np.array([11.6, 8.3, 6.3, 4.5, 4.0, 3.4])  # unit seconds
forces = np.array([0.3, 0.4, 0.5, 0.7, 0.8, 0.9])  # unit Newtons

displacement = 100*10**(-3) # unit m
area = (100*10**(-3))**2  # unit m^2
height = 1.6*10**(-3)  # unit m

velocity = displacement / times

dudx = velocity / height

shear_stress_list = forces / area

plt.scatter(dudx, shear_stress_list, zorder=3)
plt.plot(dudx, shear_stress_list, "b--")
plt.xlabel("$\\tau$")
plt.ylabel("Velocity gradient")
plt.show()

params, _ = curve_fit(linear_through_origin, dudx, shear_stress_list)

slope = params[0]

print(f"{slope=}")