# Introduction to Superconducting QuantumCircuits

## 2.1 Quantization of an Electrical Circuit
### 2.1.1 The Lumped-Element Circuit Model

### 2.1.1.1 Constitutive Relations
At any instant $t$, the classical state of a dipole can be fully determined by knowing a single dynamical variable. 
Voltage $V(t)$- voltage drop across the dipole
Current $I(t)$- current flowing through dipole

These two variables are connected by a constitutive relation, which can be:
Linear - ohm's law
Non-linear - depends on the dipole's characteristics

It is often convenient to describe the dipole in terms of:
	Charge $Q(t)$ and its time derivative $\dot Q = I(t)$ 
	Flux $\Phi(t)$ and its time derivative $\dot \Phi = V(t)$ 

Capacitance elements -Capacitors
Voltage depends on charge: $V=Q/C$
Energy stored depends only on charge: $$E = \int V(Q)dQ$$
Inductive elements -Inductors
Current $i$ depends on flux: $I = \Phi/L$ (linear) or $I = I_0\sin(\Phi/\varphi_0)$ (non-linear)
Energy stored depends only on flux: $$ E = \int I(\Phi)d\Phi$$ 
### 2.1.1.2 Defining the Spanning Tree of a Circuit
To solve a circuit, a set of independent variables must be defined based on the constitutive relations of the circuit elements. Graph theory provides a way to simplify a planar network of dipoles (only resistors or only capacitors) into a single equivalent dipole.

Node method for finding independent variables:
	Identify nodes connected to at least two elements with distinct constitutive relations and assign an electrical potential to each.
	Define a set of independent fluxes ($\Phi_1,\Phi_2,...,\Phi_n$) by constructing a spanning tree. Which is a structure that connects all nodes without forming loops preferably passing through inductors only.

Equations of motion and Kirchhoff's node law
	Kirchhoff's node law states that the sum of currents entering a node equals the sum of currents leaving it, ensuring charge conservation.
	Charge conservation holds well in meals at frequencies below their plasma frequency, which is typically in the deep UV range, far beyond microwave frequencies used in superconducting circuits.

### 2.1.1.3 A Simple Example
![[Pasted image 20250219143358.png]]
The points A and B are nodes of the circuit and are characterized by electrical potentials $V_A$ and $V_B$. Point C connects three purely resistive elements, and thus the elements of this point can be reduced to a single equivalent dipole of resistance:$$R_{eq} = R_1 + \frac{R_2R_3}{R_2+R_3}$$
The spanning tree connecting node $A$ and $B$ defines here a single independent flux variable $\Phi$, the flux threading the inductance $L$. We write the equation of motion of the circuit by writing Kirchhoff's law at node $A$ and using the constitutive relations of each element (eq 2.4 in figure 2.1)
$\dot\Phi(t)=V_A(t)-V_B(t), \quad i_L(t)=\Phi/L$ is the current flowing through the inductor branch, $i_C(t)=C\ddot\Phi$ the current flowing in the capacitor branch, and $i_R(t)=\dot\Phi/R_{eq}$ 


### 2.1.2 Quantization of a Lumped Element Circuit
For a circuit to exhibit quantum mechanical behavior, two key conditions must be met:

Absence of Dissipation:
	All metallic components must have zero resistance at the circuit's operating frequency and temperature
	This is achieved using superconducting materials, where electron pairs (Cooper pairs) form a special ground state with an excitation gap of $2\Delta$
	This gap prevents dissipation and reduces the system's degrees of freedom, allowing circuits made of $\sim 10^{12}$ atoms to behave quantum mechanically

Cooling to Supress Thermal Fluctuations:
	The thermal energy of the system must be much lower than the circuit's transition energy
	Ex: A 5 GHz xircuit should operate at $\sim20$ mK 
	This is achieved using a dilution refrigerator
	Additionally, Wires connected to control and readout ports must be carefully cooled and electromagnetically filtered to prevent unwanted heat transfer to the system.

### 2.1.2.1 Definition of the Conjugate Variables
For an arbitrary circuit composed of non dissipative elements, one obtains the equation of motion by first identifying the independent variables and writing the Lagrangian of the system: $$\mathcal L = K(\dot\Phi_1, \dot\Phi_2,...,\dot\Phi_n) - U(\Phi_1,\Phi_2,...,\Phi_n)$$
where $K$ is the capacitive energy and $U$ is the inductive energy of the circuit. The conjugate momenta of our system are given by: $$\mathcal Q_i \equiv \frac{\partial \mathcal L}{\partial \dot\Phi_i}$$
Finally we obtain the Hamiltonian of the system:
$$\mathcal H = \sum\dot\Phi_i \mathcal Q_i -\mathcal L$$
$$\dot\Phi_i = \frac{\partial\mathcal H}{\partial \mathcal Q_i}$$
$$\mathcal {\dot Q_i}=-\frac{\partial \mathcal H}{\partial \Phi_i}$$
The principle of correspondence of Dirac stipulates that one can quantize the system by introducing operators $\hat \Phi_i$ and $\hat Q_i$, which obey the commutation relations $$\Big[\hat \Phi_i,\hat Q_i\Big]=i\hbar$$
### 2.1.2.2 From the Capacitance Matrix to the Hamiltonian of the Circuit
![[Pasted image 20250219161730.png]]
Consider the figure. Point $A$,$B$ and $C$ are nodes of the circuit that are characterized by electrical potentials $V_A$, $V_B$ and $V_C$. We define a spanning tree by choosing the flux $\Phi_1$ and $\Phi_2$ shown in the figure and connecting these three nodes.
The inductive energy of the system is:$$U = \frac{\Phi_1²}{2L_1} + \frac {\Phi_2²}{2L_2}$$
The capacitive energy is:
$$K = \frac 1 2 C_1(V_A-V_C)² + \frac 1 2 C_2(V_B-V_C)²+ \frac 1 2 C_3(V_A-V_B)²+\frac 1 2 C_gV_A^2 + \frac 1 2 C_g V_B²^2 + \frac 1 2 C_g V_C^2$$
It is possible to write the capacitance energy as $K=\frac 1 2 V^ TCV$ where $V^T =(V_A,V_B,V_C)$ and $C$ as a $3 \times 3$ matrix:
$$
C =
\begin{bmatrix}
C_1+C_3+C_g & -C_3 & -C_1\\
-C_3 & C_2+C_3+C_g & -C_2\\
-C_1 & -C_2 & C_1+C_2+C_g
\end{bmatrix}
$$
Using the definitions $\dot\Phi_1 = V_C -V_A, \dot\Phi_2 = V_B -V_C$ and Millman theorem for ground voltage $V_g = V_A+V_B+B_C \equiv 0$ we have$$\begin{cases} V_A = -\frac{2}{3} \dot{\Phi}_1 - \frac{1}{3} \dot{\Phi}_2 \\ V_B = +\frac{1}{3} \dot{\Phi}_1 + \frac{2}{3} \dot{\Phi}_2 \\ V_C = +\frac{1}{3} \dot{\Phi}_1 - \frac{1}{3} \dot{\Phi}_2 \end{cases}$$
Thus one can define a passage matrix P that expresses V as $V=P\dot\Phi$, and we get
$$
\mathcal L = \frac 1 2\dot\Phi^T \tilde C \dot \Phi - \frac 1 2 \Phi^TL^{-1}\Phi
$$
where $L^{-1}$ is a matrix with the diagonal elements $1/L_i$ and the non-diagonal as 0, and $\tilde C = P^TCP$. Conjugate momenta: $Q \equiv \tilde C \dot\Phi$. And thus the Hamiltonian:$$\mathcal H = \frac 1 2 Q^T\tilde C ^{-1}\dot \Phi + \frac 1 2 \Phi^T L^{-1}\Phi$$ 
### 2.1.2.3 Coupling Between Two Resonators
The Hamiltonian above can be greatly simplified if one assumes that $C_3,C_g \ll C-1,C_2$. Then $\tilde C^{-1}$ becomes:$$\tilde C^{-1} \approx \frac 1 {C_1C_2} \begin{pmatrix}
C_2+C_3+ \frac2 3 C_g & C_3 + \frac 1 3 C_g \\
C_3+ \frac 1 3 C_g & C-1+C_3 + \frac 2 3 C_g
\end{pmatrix}$$
By grouping the quadratic terms of each independent variable with its conjugate, we can write $\mathcal H$ as the sum of two harmonic oscillators with a coupling term $V$
$$\mathcal H = \mathcal H_1 + \mathcal H_2 + V$$
where 
$$\mathcal H_1 = \hbar \omega_1(a_1^\dagger a_1 + \frac 1 2 )$$
$$\mathcal H_2 = \hbar \omega_2(a_2^\dagger a_2 + \frac 1 2 )$$
$$
\omega_i^2 = \frac 1 L_i [\tilde C^{-1}]_{ii}
$$
and $$V = \hbar \eta \sqrt{\omega_1\omega_2}(a_1-a_1^\dagger)(a_2^\dagger-a_2)$$
where $\eta = \frac{C_3+\frac 1 3 C_g}{C_1C_2}$


### 2.1.3 Transmission Lines
Contrary to lumped element circuits, the physical dimensions of transmission lines are comparable to the wavelength $\lambda$ of the original signal. Thus, a transmission line is a distributed-parameter  network, where voltage and the currents can vary in magnitude and phase over its length.

### 2.1.3.1 Definition of the propagation Wave Amplitudes
![[Pasted image 20250220140314.png]]
A transmission line can be modeled as a series of discrete lumped elements where inductance per unit cell is $L_u$ and capacitance to ground per unit cell is $C_u$.
Using Kirchoffs laws and taking the continuum limit $(L_u/u \rightarrow L, C_u/u \rightarrow C)$, the voltage $V(x,t)$ and current $I(x,t)$ satisfy the wave equations:$$\partial_x V=-L\partial_tI$$$$-C\partial_tV = \partial_xI$$
To solve these equations, propagation wave amplitudes $\mathcal A_\rightarrow$ (right-moving) and $\mathcal A_\leftarrow$ (left-moving) are introduced: $$\mathcal A_\rightarrow = \frac 1 2 \left(\frac V {\sqrt Z_0} + I\sqrt{Z_0}\right)$$ $$\mathcal A_\rightarrow = \frac 1 2 \left(\frac V {\sqrt Z_0} - I\sqrt{Z_0}\right)$$
where $Z_0 = \sqrt{L/C}$ is the characteristic impedance of the transmission line. The propagation velocity is: $$c= \frac 1 {\sqrt{LC}}$$
The wave solution takes the form:
$$\mathcal A_\rightarrow(x,t) = \mathcal A_{out} (x-ct),\quad \mathcal A_\leftarrow(x,t) = \mathcal A_{in} (x+ct) $$
where $\mathcal A_{in}$ and $\mathcal A_{out}$ are arbitrary functions describing incoming and outgoing waves.
Finally, the instantaneous power is directly related to  the wave amplitudes:
$$\mathcal P(x,t) = I(x,t) \times V(x,t) = \mathcal A_{out}^2 - \mathcal A_{in}^2
$$
This formulation is useful for analyzing signal propagation and power transfer in superconducting quantum circuits.

### 2.1.3.2 Fourier Components of Propagation Wave Amplitudes
Since the equations are linear, it is possible to look at individual Fourier components of $A^{\rightarrow/\leftarrow}(x,t)$ at any given point in space $x$
$$
A^{\rightarrow/\leftarrow}(x,t) = \sum_k A^{\rightarrow/\leftarrow}_k(x)e^{-i\omega_k t} +c.c.
$$
We will consider monochromatic waves only, thus dropping the sum and index $k$ systematically. We write $$A^{\rightarrow/\leftarrow}(x,t) = A^{\rightarrow/\leftarrow}(x)e^{-i\omega t}+c.c.$$
Assuming $\mathcal A_{in}=0$ we get
$$
\mathcal P (x,t) = \mathcal A^2_{out} = (A^{\rightarrow}(x)e^{-i\omega t}+c.c.)²=2|A^\rightarrow(x)|^2 + ((A^\rightarrow(x))²e^{-2i\omega t} +c.c.)
$$
From this we can find $$\langle P(x)\rangle=2|A^\rightarrow(x)|^2$$

### 2.1.3.3 Semi-Infinite transmission Line
A semi-infinite transmission line is a transmission line that extends indefinitely in one direction and is terminated at $x=0$ by a system $S$. The incoming $\mathcal A_{in}$ and outgoing $\mathcal A_{out}$ waves are related by boundry conditions imposed by $S$.
At $x=0$ the voltage and current are expressed as:
$$V(0,t)=\sqrt{Z_0}(\mathcal A_{out}(t) +\mathcal A_{in}(t)) $$
$$
I(0,t) = \frac 1 {Z_0} (\mathcal A_{out}(t) - \mathcal A_{in}(t))
$$
Open circuit termination $I(0,t) = 0$ -> no current flows, so the wave is fully reflected with $A_{out}(t)=A_{in}(t)$.
Short circuit termination $V(0,t) = 0$ -> No voltage appears, so the wave reflects with a phase inversion $A_{out}(t) = - A_{in}(t)$.
If there is no incoming wave $A_{in}=0$, the system behaves like a resistor that does not dissipate energy as heat but instead carries energy away as propagating waves.

### 2.1.4 Quantization of a Transmission Line
In Hamiltonian dynamics, systems are inherently reversible and dissipationless. However, irreversibility and dissipation emerge when the number of degrees of freedom approaches infinity. 
Quantum modeling of dissipation:
	The Caldeira-Leggett decomposition models a dissipative system using an infinite collection of LC resonators
	An ideal semi-infinite transmission line can also represent dissipation, as any signal sent down the line never returns, leading to information loss and entropy creation
Thus, while individual circuit elements may be non-dissipative, dissipation can still be effectively modeled using these approaches.


### 2.1.4.1 Hamiltonian of a Transmission Line
In order to illustrate this point, lets consider a transmission line of length $\Lambda$ formed by a series of $N$ cells as shown in the figure: ![[Pasted image 20250220145812.png]]
We assume periodic boundary conditions such that $V_N = V_0$. For each cell of size $u$, the inductive (potential) energy can be written as $U_n = \frac{\Phi_n^2}{2L_u}$ and the capacitive (kinetic) energy as $K_n = \frac 1 2 C_u V_n^ 2$ 
Using $\dot \Phi_{n+1}=V_{n+1}-V_n$, one can write $$V_i = \sum_{J=1}^i \dot \Phi_j + V_0$$
By summing all equations together and using Millman theorem $(\sum_{n=0}^{N-1} V_n = 0)$, we get $$V_0 = - \sum_{n=1}^{N-1}=-((N-1)\dot \Phi_1 + (N-2)\dot \Phi_2 +...+\dot\Phi_{N-1} + (N-1)V_0)$$
These equations define a passage matrix $\mathbf P$ that expresses the vector $\mathbf V = (V_0,...,V_{N-1})$ as a function of $\mathbf{ \dot \Phi} = (\dot \Phi_1,...,\dot \Phi_N)$, i.e. $\mathbf V = \mathbf{P\dot\Phi}$. Thus the Lagrangian can be written as,$$\mathcal L = \frac 1 2 C_u \dot \Phi^T\mathbf P^T \mathbf P \dot \Phi - \frac 1 {2L_u} \Phi^T \Phi$$
The conjugate momenta of the system: $\mathbf Q =(Q_1,...,Q_N)\sim \frac{\partial \mathcal L}{\partial \mathbf{\dot \Phi}}$ and the Hamiltonian is thus
$$\mathcal H = \frac 1 {2C_u}\mathbf Q^T
\begin{pmatrix}
2 & -1 & 0 & ... & -1\\
-1 & 2 & -1 & \ddots & \vdots \\
0 & -1 & \ddots & \ddots & 0 \\
\vdots & \ddots & \ddots & 2 & -1\\
-1 & ... & 0 & -1 & 2
\end{pmatrix} \mathbf Q + \frac 1 {2L_u}\mathbf \Phi^T \mathbf \Phi$$

### 2.1.4.2 Representation of the Hamiltonian in the Fourier space
The hamiltonian above can easily be diagnolized by introducing a unitary transformation $U$ such that
$$u_{kn}= \frac 1 {\sqrt{N}}exp[i(2k\pi n/N)]Q_n $$
where $k,n$ are integers comprised between $1$ and $N$. Applying the unitary operator $U$ on operators $Q_n$ and $\Phi_n$ define a new set of non-hermitian operators
$$\tilde Q_k = \sum_{n=1}^N u_{kn}Q_n$$
$$\tilde \Phi_k = \sum_{n=1}^N u_{kn}\Phi_n$$
These operators follow commutation relations of conjugate variables $$\left[\tilde\Phi_k,\tilde Q_k^+\right]=i\hbar\delta_{kk'}$$
When $k=k'$, $exp[i(2\pi j(k-k')/N)]=1$ and the sum $\sum_{n=1}^Nexp[i(2\pi n(k-k')/N)]=N$, while if $k\neq k'$ then the sum is equal to $0$. The Hamiltonian can be written as $$\mathcal H = \sum_{k=1}^N \frac{2-2\cos[2\pi k/N]}{2C_u}\tilde Q_k^+\tilde Q_k + \frac 1 {2L_u}\tilde \Phi_k^+\tilde \Phi_k = \sum_{k=1}^N \frac {\hbar \omega_k}{2}(q_k^+q_k +\varphi_k^+\varphi_k)$$
where $$\omega_k = \sqrt{\frac{2-2\cos(2k\pi/N)}{L_uC_u}}$$
and $$[\varphi_k,q_{k'}^+]=i\delta_{kk'}$$
### 2.1.4.3 Transmission Line Viewed as an External Bath
For each mode, it is possible to introduce creation and annihilation operators
$$a_k^\rightarrow = \frac 1 {\sqrt 2} (\varphi_k + iq_k)$$
$$a_k^\leftarrow = \frac 1 {\sqrt 2} (\varphi_k - iq_k)$$
$$(a_k^\rightarrow)^+ = \frac 1 {\sqrt 2} (\varphi_k^+ - iq_k^+)$$
$$(a_k^\leftarrow)^+ = \frac 1 {\sqrt 2} (\varphi_k^+ + iq_k^+)$$
the commutation relations:$$[a_k^\rightarrow,(a_{k'}^\rightarrow)^+]=\delta_{kk'}$$ $$[a_k^\leftarrow,(a_{k'}^\leftarrow)^+]=\delta_{kk'}$$
if $N$ is even, the system has $N/2$ eigenenergies. Each mode is doubly degenerate and thus 
$$
\mathcal H = \sum_{k=1}^{N/2}\hbar\omega_k((a_k^\rightarrow)^+a_k^\rightarrow+(a_k^\leftarrow)^+a_k^\leftarrow)
$$
as we increase the size $\Lambda$ of the transmission line, the density of the modes increases. As we decrease the size of the unit cell, the bandwith $\sqrt{1/L_uC_u}$ increases. One can therefore safely consider that $k \ll N$ in a realistic situation. This allows to make the approximation that $\cos[x] \approx 1-x²/2$ and thus $$\omega_k \approx \sqrt{\frac 1 {L_uC_u}}\frac{2k\pi}{N}$$ Using $\sqrt{1/L_uC_u}=\sqrt{1/\mathcal L \mathcal C u²}=c/u$ and $\Lambda = Nu$ we get $$\omega_k = k.\frac{2\pi c}{N}$$

### 2.1.4.4 Link Between Propagation Amplitudes and Photon Operators
The connection between photon operators and the propagation amplitudes introduced in the previous section is directly obtained by comparing the incoming power carried by the influx of photons with a well-defined wavevector $k$ to the modulus of the Fourier transform of the propagation amplitude using $$\langle P\rangle = 2|A_k^\rightarrow|²=\frac c \Lambda \hbar \omega_k\langle a_k^{\rightarrow +} a_k^\rightarrow\rangle  $$
where $$A_k^\rightarrow = \sqrt{\frac c {2\Lambda} \hbar \omega_k}a_k^\rightarrow$$

### 2.1.5 Transmission line resonators
### 2.1.5.1 Scattering Matrix
An interface of two transmission lines with different characteristic impedance $Z_1 |Z_2$. The transmission line is separated into two separate regions, the keft side and the right side. When an incoming wave impinges on the interface, the propagation wave amplitude can be transmitted and/or reflected partially. We thus write the scattering matrix S.
$$
\begin{pmatrix}
A_L^\leftarrow\\
A_L^\rightarrow
\end{pmatrix}
=
\overbrace{
\begin{pmatrix}
r_\hookleftarrow & t_\leftarrow\\
t_\rightarrow & t_\rightarrow
\end{pmatrix}}^{S}
\begin{pmatrix}
A_L^\rightarrow\\
A_L^\leftarrow
\end{pmatrix}
$$
We calculate the scattering coefficients by writing Kirchhoff equations of voltage and current at the interface assuming $A_R^\leftarrow=0$.
$$
V(x^-,t) = V(x^+,t)=\sqrt Z_1 (A_L^\rightarrow + A_L^\leftarrow) = \sqrt Z_2 A_R^\rightarrow
$$
$$
I(x^-,t) = I(x^+,t) = (A_L^\rightarrow - A_L^\leftarrow)/\sqrt Z_1 = A_R^\rightarrow/\sqrt Z_2
$$
which we solve to get:
$$
t_\rightarrow = \frac{2\sqrt{Z_1Z_2}}{Z_1+Z_2}
$$
$$
r_\hookleftarrow = \frac{Z_2-Z_1}{Z_1+Z_2}
$$
Similarily, two other coefficients can be established by a swap operation $Z_1\leftrightarrow Z_2$ 
![[Pasted image 20250227115102.png]]

### 2.1.5.2 Calculating Transmission and Reflection Coefficients for Simple Lumped Elements
lets consider the circuit above. The transmission line is now intersected by a lumped element system $S$. For instance, we consider in (figure above 2.5-b)) a transmission line intersected by an impedance $Z$ in series. We get 
$$
I(x^-,t) = I(x^+,t) = \frac 1 {\sqrt{Z_0}} (A_L^\rightarrow-A_L^\leftarrow) = \frac{A_r^\rightarrow}{\sqrt Z_0}
$$
$$
ZI(x,t) = V(x^-,t) -V(x^+,t) = \sqrt Z_0 [(A_L^\rightarrow+A_L^\leftarrow) - A_R^\rightarrow]
$$
using the definitions of the scattering matrix we get
$$r=z/(2+z)\quad t=2/(2+z)$$
with $z=Z/Z_0$- If the scatterer is a capacitor $Z=1/(-i\omega C)$ we get
$$t=\frac 2 {2+1/(-i\omega CZ_0)} \quad r = \frac{1/(-i\omega CZ_0)}{2+1/(-i\omega CZ_0)}$$
Another interesting case to consider is a shorting circuit elements as shown in (Fig 2.5 c)) where $$V(x^-,t)=V(x^+,t) = \sqrt{Z_0}A_R^\rightarrow$$
$$V(x^\pm,t)=\frac Z {\sqrt{Z_0}}(A_L^\rightarrow - A_L^\leftarrow) -\frac Z {\sqrt{Z_0}}A_R^\rightarrow $$
thus: $$r=-1/(2z+1) \quad t=2z/(2z+1)$$

### 2.1.5.3 $\lambda/2$ Resonators with Symmetrical Terminations
A half-wavelength $\lambda/2$ resonator with symmetrical terminations ensures full transmission at the resonant frequency $\omega_r =\frac{\pi c}{L_{res}}$ due to coherent interference, eliminating reflections. The transmission coefficient is given by: $$\tau = \frac{t² e^{\pi i \omega/\omega_r(1+i/Q_{int})}}{1-r²e^{2\pi i \omega /\omega_r(1+i/Q_{int})}}$$
where $Q_{int}$ represents internal losses in the resonator.
Key relationships:
The energy leakage rate $\kappa$ is related to the transmission coefficient and round-trip frequency:$$\kappa=2\frac{\omega_r}{2\pi}|t|²$$
The external quality factor $Q_{ext}$ is given by:$$Q_{ext}=\frac{\omega_r}\kappa = \frac \pi {|t|²}$$
If the scatterer is a capacitor with capacitance $C$, then:
$$|t|²\approx 4C²\omega_r^2Z_0^2$$
$$Q_{ext}=\frac \pi{4C²\omega_r^2Z_0^2}$$
Transmission behaviour:
When $Q_{int}=\infty$ (no internal losses), full transmission occurs at $\omega=\omega_r$ with unit amplitude and phase shift of $\pi$
As $Q_{ext}/Q_{int}$ increases, the maximum transmission decreases, causing a reduction in the resonator's efficiency.


### $\lambda/4$ Resonators with Short Circuit Termination
A quarter-wavelength $\lambda/4$ resonator is a transmission line segment of length $L_{res}=\lambda/4$, terminated by a short circuit. At the resonant frequency $\omega_r=\frac{\pi c}{2L_{res}}$, a phase shift is observed due to coherent interference of reflected waves. The reflection coefficient is given by:
$$\rho = r- \frac{r² e^{\pi i \omega /\omega_r(1+i/Q_{int})}}{1+re^{\pi i \omega/\omega_r(1+Q_{int})}}$$
Energy leakage and external quality factor:
The energy leakage $\kappa$ is related to the round-trip frequency and the transmission coefficient:$$\kappa=\frac{\omega_r}{2\pi}|t|²$$
The external quality factor is given by:$$Q_{ext}=\frac{2\pi}{|t|²}$$
Three coupling regimes based on $Q_{ext}/Q_{int}$:
1. Overcoupled regime $Q_{ext} \ll Q_{int}$(blue curve):
	1. The reflection amplitude $|\rho|\approx 1$ accross all frequencies.
	2. The phase of $\rho$ changes abruptly at resonance and undergoes a $2\pi$ shift
2. Critically coupled regime $Q_{ext}=Q_{int}$ (green curve):
	1. Reflection amplitude reaches nearly zero at resonance
	2. A discontinuity in phase causes a $\pi$ phase shift
3. Undercoupled $Q_{ext} > Q_{int}$ (red curve):
	1. The resonance appears as a dip in reflection amplitude $|\rho|$
	2. Phase shift is less than $\pi$
	3. This regime makes reflection measurements difficult due to minimal change in amplitude and phase resonance

![[Pasted image 20250304133818.png]]

### 2.1.5.5 Expression for the Local Current and/or Voltage in the Resonator as a Function of Propagation Wave Amplitudes
se boka- bare et par formler

### 2.1.6 Quantization of Transmission Line Resonators
### 2.1.6.1 $\lambda/2$ Resonators with Open Circuit Terminations
A $\lambda/2$ resonator is a transmission line resonator of length $L_{res}$ with open-circuit terminations at both ends. Unlike lumped-element resonators, it supports an infinite number of modes.

Properties:
The characteristic impedance $$Z_0 = \sqrt{\frac L C }$$
where $L$ and $C$ are the inductance and capacitance per unit length
The flux functions $\Phi(x)$ is related to voltage as $V=\partial_t \Phi$
The lagrangian is $$
L = \frac 1 2 \int_0^{L_{res}}\left(C\dot \Phi ² - \frac 1 L (\partial_x\Phi)²\right)dx
$$
Mode decomposition:
The boundary conditions enforce that the current $I(x)=0$ at both ends, leading to a cosine mode expansion for $\Phi(x)$$$\Phi(x)=\sum_{j=1}^\infty\Phi_j\cos\left(\frac {\pi j x}{L_{res}}\right)$$
substituting this into the Lagrangian gives the Hamiltonian $$H = \sum_{j=1}^\infty\left(\frac{Q_j^2}{CL_{res}} + \frac{\pi² j²}{4LL_{res}}\Phi_j^2\right)$$
where $Q_j$ is the conjugate momentum of $\Phi_j$

Quantum representation:
Using creation and annihilation operators, the Hamiltonian becomes: $$H = \hbar\omega_j(a_j^\dagger a_j + \frac 1 2 )$$
where $\omega_j = j\omega_r = j \frac {\pi c}{L_{res}}$ and $c= \frac 1 {\sqrt{LC}}$

Current expression: $$I(x)
= \sum_{j=1}^\infty \delta I_0 \sqrt j \sin (\frac{\pi j x}{L_{res}})(a_j^\dagger + a_j)
$$
where $\delta I_0 = \frac {\omega_r \pi}{\hbar Z_0}$
Voltage expression: $$V(x)
= -i\sum_{j=1}^\infty \delta V_0 \sqrt j \cos (\frac{\pi j x}{L_{res}})(a_j -  a_j^\dagger)
$$
where $\delta V_0 = \frac {\omega_r \pi Z_0}{\hbar}$ 

A$\lambda/2$ resonator with open-circuit terminations supports an infinite number of resonant modes, with quantized energy levels and wavefunctions that define its current and voltage distributions.


### 2.1.6.2 Determining the Current Operator by Filter Function Formalism
$$
\delta I(x) = \sqrt{ \int_{d\omega} \frac{\hbar\omega}{4\pi Z_0} (|f_\rightarrow |² (\omega,x) +|f_\leftarrow |² (\omega,x)) }
$$


### 2.2 Superconducting Qubits
### 2.2.1 Using the Non-linearity of Josephson Junctions
![[Pasted image 20250304141600.png]]
A circuit formed by linear components, such as capacitors and inductors, behaves as a harmonic oscillator, and not as a qubit. A non-liner element is therefore essential in order to differentiate the transitions between states $\ket 0$ and $\ket 1$ and other higher-lying eigenstates. In superconducting circuits,this non-linearity is obtained by adding several JJ's to the circuit. JJ's are formed by two superconducting island separated by a thin insulating layer (see fig) that allows tunneling of Cooper pairs. Josephson relations: $$I = I_0 \sin(\Phi/\varphi_0) \quad V=\dot \Phi$$
where $\Phi$ is the flux threading the junction, $I_0$ is the critical current of the junction and $\varphi=\hbar/2e$ is the reduced magnetic flux quantum.
Energy:$$E = -E_J\cos(\Phi/\varphi_0)$$ where $E_J = I_0\varphi_0$ is the Josephson energy

### 2.2.2 The Charge Qubit
The Cooper pair box (CPB) is the simplest superconducting qubit, consisting of two superconducting islands connected by a single JJ, with a capacitance $C_J$ and Josephson energy $E_J$. One island is biased electrostatically by a voltage source $V_g$​ through a capacitor $C_g$

### 2.2.2.1 Solving the Cooper Pair Box Hamiltonian
The CPB Hamiltonian is derived by analyzing the circuit composed of superconducting islands, a JJ, and a gate capacitor. The total energy of the system includes an inductive term, given by the Josephson energy, and a capacitive term expressed in terms of the charge and gate voltage. The system's Lagrangian is formulated based on these energies, and from it, the conjugate momentum is derived to obtain the Hamiltonian. 
Rewriting in terms of charge number $n$ and phase $\phi$ the Hamiltonian becomes:$$H = 4E_C(n-n_g)²-E_j\cos(\hat \phi)$$
where $E_C$ is the charging energy and $n_g$ is the reduced gate charge controlled by the gate voltage. The Hamiltonian is expressed in the charge basis, where the cosine term couples adjacent charge states.
Numerical diagonalization of this Hamiltonian reveals the system's energy levels, which depends on the ratio $E_J/E_C$. When $E_J \gg E_C$, charge dispersion decreases, leading to flatter energy levels, meaning the qubit behaves more like a transmon qubit rather than a charge qubit. The gate voltage $V_g$ allows tuning the qubit's transition energy.

