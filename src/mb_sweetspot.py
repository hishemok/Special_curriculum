"""Finding the parameter sweet spot for the many body PMM system"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from operators import dL, dL_dag, dR, dR_dag

epsL, epsR = sp.symbols('ϵ_L,ϵ_R') #Onsite energies
t, Delta = sp.symbols('t,Δ') #tunneling and pairing amplit
U = sp.symbols('U') #Coulomb interaction

def check_eigenvalues():
    """Compare the analytical and numerical eigenvalues of the Hamiltonian."""
    H_onsite = epsL * dL_dag * dL + epsR * dR_dag * dR
    H_tunnel = t * (dL_dag * dR + dR_dag * dL)
    H_pairing = Delta * (dR * dL + dL_dag * dR_dag)
    H_coulomb = U * (dL_dag * dL) * (dR_dag * dR)

    H = H_onsite + H_tunnel + H_pairing + H_coulomb
    H = sp.simplify(H)
    eigvals = H.eigenvals()

    ### Analytical eigenvalues from block diagonalization
    S = epsL + epsR + U
    E_even = [(S + sp.sqrt(S**2 + 4*Delta**2))/2, (S - sp.sqrt(S**2 + 4*Delta**2))/2]
    E_odd  = [((epsL + epsR) + sp.sqrt((epsL - epsR)**2 + 4*t**2))/2, ((epsL + epsR) - sp.sqrt((epsL - epsR)**2 + 4*t**2))/2]

    ### Check equality
    all_eigvals = E_even + E_odd
    for val in all_eigvals:
        found = any(sp.simplify(val - ev) == 0 for ev in eigvals.keys())
        assert found, f"Eigenvalue {val} not found in numerical eigenvalues."
    
    
    return E_even, E_odd 

Even, Odd = check_eigenvalues()

#Check parameters for sweet spot
"""Sweet spot conditions:
[E_even]_min = [E_odd]_min
"""

def Compute_U(epsL,epsR,Delta,t):
    p1 = (Delta**2-t**2 + epsL*epsR)
    p2 = (epsL + epsR + 2*np.sqrt(t**2 + (epsL - epsR)**2))
    p3 = 2*(t**2 - epsL*epsR)
    return p1*p2/p3

eps_vals = np.linspace(0.01, 2, 100)
t_val = 2
Delta_val = 1

gs_even = []
ex_even = []
gs_odd = []
ex_odd = []


for i, eps in enumerate(eps_vals):
    U_val = Compute_U(eps,eps,Delta_val,t_val)


    even0 = float(Even[0].subs({epsL:eps, epsR:eps, U:U_val, Delta:Delta_val}).evalf())
    even1 = float(Even[1].subs({epsL:eps, epsR:eps, U:U_val, Delta:Delta_val}).evalf())
    odd0  = float(Odd[0].subs({epsL:eps, epsR:eps, t:t_val}).evalf())
    odd1  = float(Odd[1].subs({epsL:eps, epsR:eps, t:t_val}).evalf())

    gs_even.append(min(even0, even1))
    ex_even.append(max(even0, even1))
    gs_odd.append(min(odd0, odd1))
    ex_odd.append(max(odd0, odd1))


plt.figure(figsize=(12, 12))
plt.subplot(3,1,1)
plt.plot(eps_vals, gs_even, label=r'$GS_{even}$', linestyle='-')
plt.plot(eps_vals, ex_even, label=r'$EX_{even}$', linestyle='--')
plt.plot(eps_vals, gs_odd, label=r'$GS_{odd}$', linestyle='-')
plt.plot(eps_vals, ex_odd, label=r'$EX_{odd}$', linestyle='--')
# plt.xlabel(r'$ϵ$ (with $ϵ_L=ϵ_R, t=1, Δ=1$)')   
plt.ylabel('Eigenvalues')
plt.title(r'Eigenvalues vs $ϵ$ at the Sweet Spot $(ϵ_R=ϵ_L, t=1, Δ=1)$')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.legend()
plt.grid()

plt.subplot(3,1,2)
GS_gap = np.array(ex_even) - np.array(gs_even)
plt.plot(eps_vals, GS_gap, label=r'$GS_{odd} - GS_{even}$', color='purple')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
# plt.xlabel(r'$ϵ$ (with $ϵ_L=ϵ_R, t=1, Δ=1$)')   
plt.ylabel(r'$GS_{odd} - GS_{even}$')
plt.title(r'Gap between $GS_{odd}$ and $GS_{even}$ vs $ϵ$ at the Sweet Spot $(ϵ_R=ϵ_L, t=1, Δ=1)$')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.legend()
plt.grid()
plt.tight_layout()
# plt.show()

plt.subplot(3,1,3)
#Lowest excited state - largest ground state
gs_even = np.array(gs_even)
gs_odd = np.array(gs_odd)
ex_even = np.array(ex_even)
ex_odd = np.array(ex_odd)

ex_low = np.minimum(ex_even, ex_odd)
gs_high = np.maximum(gs_even, gs_odd)

EX_gap = ex_low - gs_high

plt.plot(eps_vals, EX_gap, label=r'$min(EX) - max(GS)$', color='green')
# plt.axhline(0, color='black', linestyle='--', linewidth=0
# plt.xlabel(r'$ϵ$ (with $ϵ_L=ϵ_R, t=1, Δ=1$)')   
plt.ylabel(r'$min(EX) - max(GS)$')
plt.title(r'Gap between $min(EX)$ and $max(GS)$ vs $ϵ$ at the Sweet Spot $(ϵ_R=ϵ_L, t=1, Δ=1)$')
# plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('Figures/manybody_sweetspot.png', dpi=300)
plt.show()