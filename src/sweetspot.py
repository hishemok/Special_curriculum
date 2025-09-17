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

eps_array = np.linspace(-2, 2, 100)
E_vals = []
for eps in eps_array:
    H_val = np.array(H.subs({ϵ_L:eps, ϵ_R:0, t:1, Δ:1, E:0})).astype(np.complex128)
    eigvals = np.linalg.eigvals(H_val)
    E_vals.append(sorted(eigvals))


E_vals = np.array(E_vals)
plt.figure()
linestyles = ['--', '-', '-', '--']  
labels = ['E1', 'E2', 'E3', 'E4']
for k in range(E_vals.shape[1]):  
    plt.plot(eps_array, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
plt.axvline(x=0, color='r', linestyle='--', label='Sweet Spot (ϵ_L=ϵ_R=0, t=Δ)')
plt.xlabel('ϵ_L (with ϵ_R=0, t=1, Δ=1)')
plt.ylabel('Eigenvalues')
plt.title('Eigenvalues vs ϵ_L at the Sweet Spot (ϵ_R=0, t=1, Δ=1)')
plt.legend(['E1', 'E2', 'E3', 'E4', 'Sweet Spot (t=Δ)'])
plt.grid()
plt.show()


eps_array = np.linspace(-2, 2, 100)
E_vals = []
for eps in eps_array:
    H_val = np.array(H.subs({ϵ_L:eps, ϵ_R:eps, t:1, Δ:1, E:0})).astype(np.complex128)
    eigvals = np.linalg.eigvals(H_val)
    E_vals.append(sorted(eigvals))


E_vals = np.array(E_vals)
plt.figure()
linestyles = ['--', '-', '-', '--']  
labels = ['E1', 'E2', 'E3', 'E4']
for k in range(E_vals.shape[1]):  
    plt.plot(eps_array, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
plt.axvline(x=0, color='r', linestyle='--', label='Sweet Spot (ϵ_L=ϵ_R=0, t=Δ)')
plt.xlabel('ϵ_L, ϵ_R (with t=1, Δ=1)')
plt.ylabel('Eigenvalues')
plt.title('Eigenvalues vs ϵ_L, ϵ_R at the Sweet Spot (t=1, Δ=1)')
# plt.legend(['E1', 'E2', 'E3', 'E4', 'Sweet Spot (t=Δ)'])
plt.legend()
plt.grid()
plt.show()








t_Delta = np.linspace(-2, 2, 100)
E_vals = []
for t_delta in t_Delta:
    tval = t_delta
    Delta_val = 1
    H_val = np.array(H.subs({ϵ_L:0, ϵ_R:0, t:tval, Δ:Delta_val, E:0})).astype(np.complex128)
    eigvals = np.linalg.eigvals(H_val)
    E_vals.append(sorted(eigvals))

E_vals = np.array(E_vals)
plt.figure()
linestyles = ['--', '-', '-', '--']  # 4 different styles
labels = ['E1', 'E2', 'E3', 'E4']
for k in range(E_vals.shape[1]):  # loop over eigenvalue branches
    plt.plot(t_Delta, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
X = [-1,1]
for x in X:
    plt.axvline(x=x, color='r', linestyle='--', label='Sweet Spot (t=Δ)')
plt.xlabel('t (with Δ=1, ϵ_L=ϵ_R=0)')
plt.ylabel('Eigenvalues')
plt.title('Eigenvalues vs t at the Sweet Spot (ϵ_R=0, ϵ_L=0, Δ=1)')
plt.legend()
plt.grid()
plt.show()


#grid
t_vals = np.linspace(-2, 2, 50)
Delta_vals = np.linspace(-2, 2, 50)
E_vals = np.zeros((len(t_vals), len(Delta_vals), 4), dtype=np.complex128)
for i, t_val in enumerate(t_vals):
    print(f"Calculating row {i+1} of {len(t_vals)}")
    for j, Delta_val in enumerate(Delta_vals):
        H_val = np.array(H.subs({ϵ_L: 0, ϵ_R: 0, t: t_val, Δ: Delta_val, E: 0})).astype(np.complex128)
        eigvals = np.linalg.eigvals(H_val)
        eigvals_sorted = np.sort(eigvals)[:4]  
        E_vals[i, j, :] = eigvals_sorted

T, D = np.meshgrid(t_vals, Delta_vals, indexing="ij")
plt.figure(figsize=(10, 8))
plt.contourf(T, D, E_vals[:, :, 2] - E_vals[:, :, 1], levels=100, alpha=0.6)
plt.colorbar(label='Eigenvalue')
plt.xlabel('t')
plt.ylabel('Δ')
plt.title('Groundstate eigenvalues grid at the Sweet Spot (ϵ_L=ϵ_R=0)')
plt.axline((0, 0), slope=1, color='r', linestyle='--', label='Sweet Spot (t=Δ)')
plt.axline((0, 0), slope=-1, color='r', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
