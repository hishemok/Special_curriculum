import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Set plotting parameters
plt.rcParams.update({'font.size': 14, 'figure.figsize': (8, 6), 'lines.linewidth': 2})



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
labels = [r'$E_1$', r'$E_2$', r'$E_3$', r'$E_4$']
for k in range(E_vals.shape[1]):  
    plt.plot(eps_array, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
plt.axvline(x=0, color='r', linestyle='--', label=r'Sweet Spot $(ϵ_L=ϵ_R=0, t=Δ)$')
plt.xlabel(r'$ϵ_L$ (with $ϵ_R=0, t=1, Δ=1$)')
plt.ylabel('Eigenvalues')
plt.title(r'Eigenvalues vs $ϵ_L$ at the Sweet Spot $(ϵ_R=0, t=1, Δ=1)$')
plt.legend()
plt.grid()
plt.savefig('Figures/singlebody_sweetspot_eps.png', dpi=300)
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
labels = [r'$E_1$', r'$E_2$', r'$E_3$', r'$E_4$']
for k in range(E_vals.shape[1]):  
    plt.plot(eps_array, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
plt.axvline(x=0, color='r', linestyle='--', label=r'Sweet Spot $(ϵ_L=ϵ_R=0, t=Δ)$')
plt.xlabel(r'$ϵ_L, ϵ_R$ (with $t=1, Δ=1$)')
plt.ylabel('Eigenvalues')
plt.title(r'Eigenvalues vs $ϵ_L, ϵ_R$ at the Sweet Spot $(t=1, Δ=1)$')
# plt.legend(['E1', 'E2', 'E3', 'E4', 'Sweet Spot (t=Δ)'])
plt.legend()
plt.grid()
plt.savefig('Figures/singlebody_sweetspot_epsLR.png', dpi=300)
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
labels = [r'$E_1$', r'$E_2$', r'$E_3$', r'$E_4$']
for k in range(E_vals.shape[1]):  # loop over eigenvalue branches
    plt.plot(t_Delta, E_vals[:, k].real, linestyle=linestyles[k], label=labels[k])
X = [-1,1]
for x in X:
    plt.axvline(x=x, color='r', linestyle='--', label=r'Sweet Spot $(t=Δ)$')
plt.xlabel(r'$t$ (with $Δ=1, ϵ_L=ϵ_R=0$)')
plt.ylabel('Eigenvalues')
plt.title(r'Eigenvalues vs $t$ at the Sweet Spot $(ϵ_R=0, ϵ_L=0, Δ=1)$')
plt.legend()
plt.grid()
plt.savefig('Figures/singlebody_sweetspot_t.png', dpi=300)
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
plt.title(r'Groundstate eigenvalues grid at the Sweet Spot $(ϵ_L=ϵ_R=0)$')
plt.axline((0, 0), slope=1, color='r', linestyle='--', label=r'Sweet Spot $(t=Δ)$')
plt.axline((0, 0), slope=-1, color='r', linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig('Figures/singlebody_sweetspot_grid.png', dpi=300)
plt.show()



"""---------------- Eigenvectors ----------------"""
H_val = np.array(H.subs({ϵ_L:0, ϵ_R:0, t:1, Δ:1, E:0})).astype(np.complex128)
eigvals, eigvecs = np.linalg.eig(H_val)

zero_mode_indices = np.argsort(np.abs(eigvals))[:2]
modes = np.abs(eigvecs[:, zero_mode_indices])

plt.figure(figsize=(10, 5))

color_1 = 'tab:blue'
color_2 = 'tab:red'
plt.bar(np.arange(4)-0.1, modes[:, 0], width=0.5, color=color_1, label='Zero Mode 1')
plt.bar(np.arange(4)+0.1, modes[:, 1], width=0.5, color=color_2, label='Zero Mode 2')
plt.xticks(np.arange(4), [r'$d_L$', r'$d_R$', r'$d_L$†', r'$d_R$†'])
plt.xlabel('Components')
plt.ylabel('Amplitude')
plt.legend()
plt.suptitle("Zero-mode eigenvector components at the sweet spot")
plt.savefig('Figures/singlebody_sweetspot_zero_modes.png', dpi=300)
plt.show()