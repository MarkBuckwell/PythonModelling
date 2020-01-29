# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:57:32 2020

@author: mbuck
"""

# A basic model of a spiking resistive RAM (RRAM)/memristor device, or neuron.
# This model is rather functional, in that it may generate a train of spikes,
# but phenomenologically, it requires refining into alignment with real process.
# The principle here is that charge accuumulation initiates a spike, i.e. the
# the axon membrance starts depolarising, or the RRAM begins resetting. Given
# sufficient further accumuation, the axon will repolarise (but will not yet
# hyperpolarise), or the RRAM will return to its 'resting' state. In both
# cases, the accumulated charge is reset and the process begins again. There
# is also some random noise added in to spice things up.
import matplotlib.pyplot as plt
import numpy as np
import random

# Values are, at the moment, quite arbitrary.
Iset = float(0.25) # Constant bias current.
R = float(100) # Initial resistance, taken to be a generic 'on' state.
time = np.arange(0, 20, 0.05) # Sampling time for spike train.
Vout = np.zeros(len(time)) # Output voltage.
QthreshR = float(0.5) # Threshold charge to start a reset.
QthreshS = float(0.6) # Threshold charge to start a set.
Drate = float(1.1) # Charge dissipation rate on forming.
Qt = 0 # Accumulated charge.
iQ = 0 # Charging index.

# Iterate through the sampling time to generate the output voltage at each
# timepoint.
for t in range(len(time)):
    Qtime = time[iQ] # Charging time.
    Vout[t] = (R / Iset) + random.randint(0, 50)
    if Qt < QthreshR and Qt < QthreshS:
        Qt = Iset * Qtime
        iQ = iQ + 1
    elif Qt >= QthreshR and Qt < QthreshS:
        R = R * Drate
        Qt = Iset * Qtime
        iQ = iQ + 1
    elif Qt >= QthreshR and Qt >= QthreshS:
        R = 100
        Qt = 0
        iQ = 0
        
        
# Plot the voltage against time.
fig = plt.plot(time, Vout)
plt.xlabel('Time/s')
plt.ylabel('Voltage/V')
