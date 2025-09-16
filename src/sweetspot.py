import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

ϵ_L, ϵ_R, t, Δ, E = sp.symbols('ϵ_L ϵ_R t Δ E')
H = sp.Matrix([ [ϵ_L - E, t        , 0         ,          Δ],
                [t      , ϵ_R - E  , - Δ       ,          0],
                [0      , -Δ       , -ϵ_L - E  ,         -t],
                [Δ      , 0        , -t        ,   -ϵ_R - E]])


eigvals = H.eigenvals()
print("Eigenvalues: ", eigvals)

t_array = np.linspace(0.1, 2, 10)
E_vals = []
for t_val in t_array:
    H_val = H.subs({ϵ_L:0, ϵ_R:0, t:t_val, Δ:1, E:0})
    eigvals = H_val.eigenvals()
    E_vals.append(sorted([float(ev) for ev in eigvals.keys()]))


plt.figure()
plt.plot(t_array, [E[0] for E in E_vals], label='E1')
plt.plot(t_array, [E[1] for E in E_vals], label='E2')
plt.plot(t_array, [E[2] for E in E_vals], label='E3')
plt.plot(t_array, [E[3] for E in E_vals], label='E4')
plt.axvline(x=1, color='r', linestyle='--', label='Sweet Spot (t=Δ)')
plt.xlabel('t (with Δ=1)')
plt.ylabel('Eigenvalues')
plt.title('Eigenvalues vs t at the Sweet Spot (ϵ_L=ϵ_R=0, Δ=1)')
plt.legend()
plt.grid()
plt.show()



# eigvecs = H.eigenvects()
# print("Eigenvectors: ", eigvecs)


# eigvals = H.eigenvals()
# print("Eigenvalues: ", eigvals)

# # Give value to the parameters
# H_val = H.subs({ϵ_L:0, ϵ_R:0, t:1, Δ:1, E:0})
# eigvals = H_val.eigenvals()

# def find_eigvecs_eigvals(H, ϵ_L, ϵ_R, t, Δ, E):
#     eigvals = H_val.eigenvals()
#     eigvecs = H_val.eigenvects()
#     H_val = H.subs({ϵ_L: ϵ_L, ϵ_R: ϵ_R, t: t, Δ: Δ, E: E})
#     return eigvals, eigvecs

