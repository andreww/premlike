# Measure performance in typical use cases
import time
import numpy as np
import premlike

# Calculate pressure and gravity in a tight loop
# just above ICB (this corresponds to the IVP solver
# in my slurry code)

nsteps = 1000
t0 = time.perf_counter()
for r in np.linspace(1225.0, 1425.0, nsteps):
    premlike.PREM.pressure(r/1000)
    premlike.PREM.gravity(r/1000)
t1 = time.perf_counter()
print(f"Total time for {nsteps} calculations of pressure and gravity was {t1-t0} seconds")