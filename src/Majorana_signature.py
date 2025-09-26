"""Finding the parameter sweet spot for the many body PMM system"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from operators import dL, dL_dag, dR, dR_dag

epsL, epsR = sp.symbols('ϵ_L,ϵ_R') #Onsite energies
t, Delta = sp.symbols('t,Δ') #tunneling and pairing amplit
U = sp.symbols('U') #Coulomb interaction


def create_Hamiltonian():
    """Create the Hamiltonian for the system.
    H = H_onsite + H_tunnel + H_pairing + H_coulomb

    """
    H_onsite = epsL * dL_dag * dL + epsR * dR_dag * dR
    H_tunnel = t * (dL_dag * dR + dR_dag * dL)
    H_pairing = Delta * (dR * dL + dL_dag * dR_dag)
    H_coulomb = U * (dL_dag * dL) * (dR_dag * dR)

    H = H_onsite + H_tunnel + H_pairing + H_coulomb
    return H

### Create a function that takes in parameters and returns Hamiltonian as a numpy array
def H_matrix(epsL_val, epsR_val, t_val, Delta_val, U_val):
    H = create_Hamiltonian()
    H = H.subs({epsL:epsL_val, epsR:epsR_val, t:t_val, Delta:Delta_val, U:U_val})
    H_matrix = np.array(sp.Matrix(H).evalf(), dtype=complex)
    return H_matrix


### Use this for parameter sweeps and to keep track of eigenvalues WITH corresponding eigenvectors

### Fist Get analytical sweet spot for U
def Compute_U(epsL,epsR,Delta,t):
    p1 = (Delta**2-t**2 + epsL*epsR)
    p2 = (epsL + epsR + 2*np.sqrt(t**2 + (epsL - epsR)**2))
    p3 = 2*(t**2 - epsL*epsR)
    return p1*p2/p3