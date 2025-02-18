# Josephson Junctions, Superconducting Circuits, and Qubit for Quantum Technologies

_________________________________________________________________________
## 1.1 Josephson Effect

## 1.1.1 First Josephson Equation

First, assume that the supercurrent depends on the density of Cooper pairs in the superconductors forming the junction, $|\Psi_1|² = n^*_{s,1}$ and $|\Psi_2|² = n^*_{s,2}$. Furthermore, since the coupling between the two superconductors is "weak", we can also assume that the supercurrent density between the two superconducting electrodes does not change $|\Psi|²$. It is reasonable to expect that the supercurrent density depends on the phases of the wave functions. In a bulk superconductor, the supercurrent density is proportional to tha gauge-invariant phase gradient $\gamma(\mathbf{r},t)$:
$$
J_s(\mathbf{r},t) = \frac{q^*n^*_s\hbar}{m^*}\gamma(\mathbf{r},t) 
$$
where
$$
\gamma(\mathbf{r},t) = \nabla \theta - \frac{2\pi}{\Phi_0} \mathbf{A}(\mathbf{r},t)
$$
where $\Phi_0=h/(2e)$ is the flux quantum, $\mathbf{A}$ is the potential vector, $m^*$ and $q^*$ are the charge and the mass of the superelectrons.

Assumptions: 
Current density is uniformly distributed -> the junction area is sufficiently small.
Consider two weakly connected superconductors and the phase gradient in the superconducting electrode undergoes negligible variation.
	This holds when the Cooper pair density in the electrodes is greater than in the coupling region
The gauge-invariant phase difference:
$$
\varphi(r,t) = \int_1^2 \gamma(r,t) = \int_1^2 \left(\nabla \theta - \frac{2\pi}{\Phi_0} \mathbf{A}(\mathbf{r},t)  \right)d\mathbf{l}
$$
$$
= \theta_2(r,t) -\theta_1(r,t) -  \frac{2\pi}{\Phi_0} \int_1^2\left( \mathbf{A}(\mathbf{r},t)  \right)d\mathbf{l}
$$
with the integration path along the flow direction of the current. 
The supercurrent is a $2\pi$ -periodic function of the phase difference:
$$
J_s(\varphi) = J_c\sin\varphi + \sum_{m=2}^\infty J_m \sin(m\varphi)
$$
The dominant, and often the sufficient part - (Current Phase Relation(CPR)):
$$
J_s(\varphi) = J_c\sin\varphi 
$$
From 1D to 3D
$$
J_s (y,z,t) =J_c(y,z)\sin\varphi(y,z,t)
$$
for when the current travels in x-direction

A tunnel Joseph junction represents a sort of bottleneck for the current density in the superconducting channel, being the Josephson critical current, i.e., the maximum Josephson current that can flow without triggering a voltage state, far smaller than the usual depairing current in superconducting electrodes. This makes the junction the primary region where superconducting behavior deviates from ideality.


## 1.1.2 Second Josephson equation

The second Josephson equation describes the relationship between the voltage across the Josephson Junction (JJ) and the phase difference of the superconducting wave functions. Starting from the time derivative of the gauge-invariant phase difference, it is shown that:
$$
\frac{\partial \varphi}{\partial t} = \frac{2\pi}{\Phi_0}V
$$
Where V is the voltage drop across the junction, and $\Phi_0=h/(2e)$ is the magnetic flux quantum. This equation implies that if a constant voltage is applied to the junction, the phase difference increase linearly with time:
$$
\varphi(t) = \varphi_0 + \frac{2\pi}{\Phi_0}Vt
$$
As a result, the Josephson current oscillates at a frequency (in this case):
$$
\nu = V/\Phi_0 \approx 483MHz/\mu V
$$
This means the JJ can work as a voltage-controlled oscillator capable of producing very high frequencies (-500GHz at 1mV). When an external frequency $\nu$ is applied to the junction, discrete voltage steps appear in its current-voltage ($I-V$) characteristics. The phenomenon is known as the <b>ac josephson effect</b>, confirmed by Shaprio in 1963.

### 1.1.3 Estimation of the Maximum Josephson Current Density

Finding the critical current density $J_c$ in a superconductor-insulator-superconductor (SIS) junction. 
![[Pasted image 20250211141125.png]]
The supercurrent density is derived from the time-dependent macroscopic wave function:
$$
\Psi(r,t) = \Psi(r)exp[-i(E_0/\hbar)t]
$$
where $\Psi(r)$ indicates the amplitude. Let's consider the insulating region. We consider the potential to be zero, outside the region and $V_0 > E_0$ inside the region. Assuming only elastic tunneling (the superelectrons conserve energy, so the time evolution is the same inside and outside the barrier). Thus, we only need the time-independent Schrodinger eq:
$$
-\frac{\hbar²}{2m*}\nabla²\Psi(r) = (E_0-V_0)\Psi(r)
$$
Assumptions:
	1. uniform tunneling barrier
	2. Small junction area $(A=LW)$, so the Josephson current density can be considered uniform within $A$.
The problem then turns into a 1D problem:
$$
\Psi(x) = A\cosh(\kappa x) + B\sinh(\kappa x)
$$
Taking into considerations the boundry conditions, and inserting the wave function expression into the supercurrent density equation, we get:
$$
J_s = \frac{q*}{m*}\text{Im}\{A^*B\}
$$
we obtain the supercurrent density: $J_s = J_c\sin(\theta_2-\theta_1)$, where
$$
J_c \simeq -\frac{e \kappa \hbar}{m} \sqrt{n_1^*n_2^*}e^{-2\kappa d}
$$
assuming $V_0$ is of the order of a few eV, which gives decay length $1/\kappa$, less than a nanometer, so $\kappa d \gg 1$, if $d$ is just a few nanometers. $q^*=-2e$ and $m^*=2m$. 

### 1.1.4 Anomalous Josephson Effect
The current-phase relation (CPR) describes the dependence of the supercurrent $I_s(\phi)$ on the phase difference $\phi$ across a Josephson Junction (JJ). While the simplest case follows the sinusoidal form $I_s(\phi) = I_c\sin(\phi)$, real junctions often exhibit more complex behavior.
Some general properties of the CRP include:
1. $I_s(\phi)$ is $2\pi$-periodic due to the phase periodicity of the superconducting order parameter.
2. Time-reversal symmetry ensures $I_s(\phi)=-I_s(-\phi)$, though this can be broken in certain systems, leading to spontaneous currents.
3. No supercurrent flows when the phase difference is an integer multiple of $2\pi$ -> $I_s(2\pi n)=0$
4. Combined with the above properties, $I_s(\phi)$ myst also vanish at $\phi = \pi n$ allowing considerations of $0<\phi<\pi$.
The general form of the CPR can be expressed as a Fourier series:
$$
I_s(\phi) = \sum_{n\geq 1}[ I_n \sin(n\phi) + J_n\cos(n\phi)] 
$$
where $I_n$ scales with the barrier transparency and accounts for higher-order Andreev reflections. If time-reversal symmetry (TRS) is preserved, the $J_n$ terms vanish.
Beyond the simple sinusoidal form, junctions with unconventional superconducting pairing of ferromagnetic barriers can exhibit a second-harmonic contribution:
$$
I_s(\phi) = I_1\sin(\phi) + I_2 \sin(2\phi)
$$
which affects the Josephson free energy and can lead to various junction types:
1. 0-junction $\tilde{\phi}=0$ if $|I_1/2I_2|> 1$ and $I_2 > 0$
2. $\pi$-junction $\tilde{\phi}=\pi$ for negative $I_c$, relevant in superconductor-ferromagnet-superconductor (SFS) junctions.
3. $\phi$-junction $\tilde{\phi} \neq 0,\pi$ where the phase shift depends on $I_1$ and $I_2$ 
4. $\phi_0$-junction where CPR is shifted by a constant $\phi_0$:$I_s(\phi) = I_c\sin(\phi-\phi_0)$
		resulting in a finite current at $\phi=0$, leading to phase batteries and spontaneous supercurrents.

Anomalous CPRs can arise due to external magnetic/electric fields, spin-orbit coupling, or unconventional superconductivity, with applications in spintronics and quantum technologies.

### 1.1.5 Short JJ: The Resistively and Capacitively Shunted Junction (RCSJ) Model
The Resistively and Capacitively Shunted Junction (RCSJ) Model describes the full time-dependent behaviour of a JJ by incorperating both supercurrent and quasiparticle currents, which arise when voltage $V>0$ and temperature $T>0$. It models the junction as an electrical circuit consisting of:
	1. A capacitance $C$ determined by the junction's oxide layer and area
	2. A resistance $R$, which depends on voltage and temperature and accounts for dissipation
	3. A Josephson inductance $L_J = L_c/\cos(\varphi)$
	4. A thermal noise current source $I_{th}$
	5. A bias current $I_b$

![[Pasted image 20250212132302.png]]

Dynamical Behaviour and Langevin Equation
By applying Kirchhoff's laws and using the Josephson equations, the phase dynamics is governed by the Langevin equation:
$$
C \frac{\hbar}{2e}\frac{d²\varphi}{dt²} + \frac{\hbar}{R2e} \frac{d\varphi}{dt} + I_c\sin\varphi = I_b +I_{th}(t)
$$
This can be normalized using characteristic frequency $\omega_c= \frac{2e}{\hbar}I_cR$:
$$
\beta_c \frac{d²\varphi}{d\tilde{t}²} + \frac{d\varphi}{d\tilde{t}} + \sin\varphi = i_b + i_{th}(\tilde{t})
$$
where $\beta_c$ is the Stewart-McCumber damping parameter, and the system exhibits a Washboard potential:
$$
U(\varphi,i_b) = E_{J0}{1-\cos\varphi -i \varphi}
$$
Mechanical Analogy and IV Characteristics
The Josephson phase behaves like a damped, driven pendulum, where:
2. Voltage $V$ corresponds to angular velocity of the pendulum
3. Bias current $I_b$ acts as an external torque
4. Capacitance $C$ is equivalent to the moment of inertia
5. Resistance $R$ determines the damping

Depending on the damping regime, the IV characteristics differ
	Overdamped junction (high friction, low kinetic energy) -> Non-hysteretic IV Curve
	Underdamped junction (low friction, high kinetic energy) -> hysteric IC curve


![[Pasted image 20250212132322.png]]

Switching and Retrapping Currents
Switching current $I_0$ - Bias current at which the JJ transitions to voltage state
Retrapping current $I_R$ - Current at which the system returns to a zero-voltage state
In overdamped current $I_0 = I_r$. In underdamped cases, $I_r < I_0$ with relation $I_r/I_0 \sim 4/(\pi\sqrt{\beta_c})$ 
Thermal fluctuations can cause switching below the expected $I_c$, affecting the transition dynamics

### 1.1.5.1 Temperature Effects
The noise term $I_{th}$ follows statistical properties related to thermal flucuations, where its strength is determined by the ratio of thermal energy $k_BT$ to the Josephson coupling energy $E_{J0}$. These fluctuations make the escape from a metastable state stochastic, requiring repeated simulations to analyze distributions of switching times. 

Thermal Activation(TA) allows the phase particle to escape from a potential minimum even when a barrier is present, with an escape rate given by the Kramers approximation. Numerical simulations confirm that the average switching time scales exponentially with decreasing noise. 

At very low temperatures, macroscopic quantum tunneling (MQT) can dominate the escape process, with a rate independent of temperature but dependent on the potential barrier. The crossover temperature $T_{cr}$ marks the point where TA and MQT rates are equal, highlighting a transition from thermally driven escape to quantum tunnerling. This crossover is illustrated in simulations, showing TA and MQT switching times converging at a noise amplitude corresponding to approximately 30mK.

### 1.1.5.2 Magnetic Field Effects
How an externally applied magnetic field influence a short Josephson Junction (SJJ), where the field generated by the Josephson current is negligible compared to the external field. The system's dimensions must remain smaller than the Josephson penetration depth to maintain this approximation. 

When a magnetic field is applied in the junction plane, it penetrates the electrodes within a characteristic effective thickness. The relation between the magnetic field and the Josephson phase difference is derived using Maxwell's equations and the phase difference equation. By integrating along different paths in the system, phase gradient is shown to be proportional to the applied magnetic field. 

In a rectangular SJJ, the phase difference increases linearly with position under a uniform external field, leading to an oscillatory behavior in the supercurrent density. This results in a periodic modulation of the Josephson current, forming a Fraunhofer diffraction pattern for the critical current. The derived expression shows that the critical current decreases as the applied magnetic flux increases.

Key observations:
1. At zero magnetic field, the phase difference is constant, and the Josephson current is maximized
2. At half a flux quantum, the phase oscillates over half a period, reducing the current.
3. At one flux quantum, a full oscillation occurs, canceling the total Josephson current
4. At 1.5 flux quantum, partial cancellation coccurs, leading to further current reduction
These results highlight the Fraunhoder-like dependece of the Josephson Current on the magnetic field, demonstating how external fields modulate superconducting transport properties.

### 1.1.6 Long JJ: The Sine-Gordon Model
The behaviour of a long Josephson Junction (LJJ) where a magnetic field is applied in the x-direction, the phase varies along the y-direction, and a bias current flows in the negative z-direction. The system obeys Amperes law, leading to the stationary sine-Gordon equation (SSGE):
$$
\frac{d²\varphi}{dy²} = \frac{1}{\lambda²_J}\sin\varphi(y)
$$
where $\lambda_J$ is the Josephson penetration depth, which characterizes how the magnetic field is screened.
For the time-dependent cases, the sine-Gordon equation (SGE) is:

$$
\frac{d²\varphi}{dy²} - \frac{1}{\bar{c}}\frac{d²\varphi}{d²t²} - \frac{1}{\lambda²_J}\sin\varphi = 0
$$
with Swihart velocity $\bar{c}$ setting the speed of the electromagnetic wave propagation in the junction.
The SGE allows for solitonic solutions such as:
	1. Kinks: stable $2\pi$-phase jumps, traveling while maintaining shape, producing voltage steps and microwave radiation
	2. Kink-antikink and kink-kink collisions: Interavtions between solitons
	3. Plasma waves: small amplitude oscillations with a dispersion relation
	4. Breathers: Oscillatory, unstable solutions that do not produce a measurable magnetic flux.
The Lorentz force affects moving fluxons, leading to voltage pulses due to Lorentz contractions.
An equivalent circuit model for LJJs is also derived, using Kirchhoff's laws to describe the dynamics of current and voltage in the junctions.


### 1.1.7 The Superconducting Quantum Interference Device (SQUID)
A superconducting Quantum Interference Device consists of a superconducting loop interrupted by to JJ, forming a dc-SQUID when biased with an external current. Its operation is based on two fundamental quantum phenomena: 
	Flux quantization in the superconducting loop
	Josephson effect
The device functions as an extremely sensitive flux-to-voltage converter, detecting magnetic flux with a periodic dependence on the flux quantum $\Phi_0$
![[Pasted image 20250212150903.png]]
Key equations and Principles:
1. The total flux through the loop, incorporating the phase drops across the JJ, follows:$$
\frac{2\pi \Phi}{\Phi_0} = \oint_C \Delta \theta dl = 2\pi n + \varphi_2 -\varphi_1
$$
2. The total supercurrent is given by: $I_s = I_{c1}\sin\varphi_1 + I_{c2}\sin\varphi_2$ 
	For identical junctions $(I_c = I_{c1}=I_{c2})$$$I_s=2I_c \cos(\pi\Phi/\Phi_0)\sin\varphi$$
3. The maximum supercurrent is non-negligible, the total flux satisfies:$$\Phi/\Phi_0=\Phi_{ext}/\Phi_0 + \beta_L\cos(\varphi)\sin(\pi\Phi/\Phi_0)$$ where $\beta_L = \frac{2LI_C}{\Phi_0}$
4. The maximum supercurrent depends on the external flux:$$I_s^{max}(\Phi_{ext})=2I_c\left|\cos\left(\frac{\pi\Phi}{\Phi_0}\right) \right|$$
Hysteresis and Quantum State Transitions:
SQUIDs can operate in a hysteric mode, where flux jumps by one quantum $\Phi_0$ as the applied flux changes, leading to multiple stable and unstable states
Increasing the external flux causes transitions between states with different numbers of flux quantua
This hysteresis loop behaviour enables SQUIDs to be used in quantum measurement applications

RCSJ Model (Restively and Capacitively Shunted Junction Model)
1. The Josephson phases $\varphi_1$ and $\varphi_2$ evolve dynamically according to: $$\beta_c \frac{d²\varphi_k}{dt²} + \frac{d\varphi_k}{dt} = - \frac{\partial U_{SQUID}}{\partial \varphi_k}$$ where $U_{SQUID}$ includes contributions from the magnetic energy, Josephson energy and bias currents.
2. In asymmetric SQUIDs (with different junction parameters), asymmetric factors $(\alpha_I,\alpha_R,\alpha_C,\alpha_L)$ must be considered, leading to a more complex set of coupled equations.
3. Thermal fluctuations become significant when the thermal energy $k_BT$ is comparable to the Josephson energy $E_J$ or the characteristic magnetic energy $E_M$, affecting SQUID stability and noise characteristics

Applications:
Due to the extreme flux sensitivity, SQUIDs are widely used in:
	Magnetometry (measuring very weak magnetic fields)
	Quantum Computing (as readout devices for superconducting qubits)
	Medical imaging (MEG: Magnetoencephalography)
	Geophysics and material science
	


## 1.2 Josephson Devices

### 1.2.1 JJ Fabrication Technology
JJs are created by joining two superconducting materials, typically using planar thin-film technology to integrate them with other circuit elements like resistors and capacitors. The choice of superconducting material depends on the application and available fabrication techniques. 
For superconducting qubits, Al-based JJs are commonly used due to their low dissipation and compatibility with qubit requirements. The Dolan technique, involving shadow evaporation, is preferred to minimize noise and defects in qubit fabrication.

### 1.2.2 Voltage standard
The Josephson effect enables the realization of an international voltage standard by linking a DC voltage to an applied frequency through universal constants. This is known as the inverse AC Josephson effect.

A JJ subjected to both a DC voltage $V_0$ and an RF voltage  $V_1\sin(2\pi f_1 t)$ experiences a phase evolution given by:
$$
\phi = \phi_0 + \frac{2\pi}{\Phi_0}V_0 t + \frac{V_1}{\Phi_0 f_1}\cos(2\pi f_1 t)
$$
where $\Phi_0​=2.067833831×10^{−15}$ Wb is the flux quantum.
Applying the first Josephson Eq:
$$I = I_c \sin\phi$$
expands into a series involving Bessel functions $J_n(x)$:
$$
I = I_c\sum_{n=0}^\infty (-1)^nJ_n\left(\frac{V_1}{\Phi_0 f_1}\right) \sin\left(\phi_0 + \frac{2\pi}{\Phi_0} V_0 t - 2\pi n f_1 t \right)
$$
At specific DC voltages: 
$$
V_n = n\Phi_0 f_1, \quad n = 0,\pm1,\pm2
$$
a net DC current appears in the junction. These constant-voltage current steps, called Shapiro steps, provide a direct and precise relation between frequency and voltage

Practical considerations:
1. RF frequency requirements: For clean Shapiro steps, the RF frequency $f_1$ must exceed the plasma frequency $f_p = \sqrt{J_c/(2\pi C)}$, ensuring the RF current flows through the junction capacitance.
2. Voltage Scaling: Each step corresponds to small voltages (few $\mu$V), but large arrays of JJs in series allow practical voltage standards up to 10V.
The precision surpasses older Weston cell standards (accuracy $10^{-6}$) with Josephson based standards achieving $10^{-11}$, making them the foundation for modern voltage metrology.

### 1.2.3 SQUIDs
A superconducting Quantum Interference Device is an extremely sensitive electronic device based on JJs. The dc-SQUID, the most common type, consists of a superconducting loop with two identical JJs. When a bias current $I$ is applied, the voltage across the SQUID  oscillates periodically with the external magnetic flux threading the loop. This flux-dependent voltage oscillation is key to SQUID's applications as magnetic field sensors.

1. Responsivity  of the SQUID. The change in voltage with respect to magnetic flux is given by: $$V_\Phi \equiv \frac{\delta V}{\delta \Phi}\Bigg|_I \approx \frac R L $$ where $R$ is the junctions's shunt resistance and $L$ is the SQUID loop inductance. Increasing $R$ and decreasing $L$ enhances sensitivity. Increasing $R$ and decreasing $L$ enhances sensitivity: $$\delta V \approx \frac R L \delta \Phi$$
2. Noise Considerations. The noise from thermal fluctuations in the resistors leads to a magnetic flux noise spectral density: $$S_\Phi(f) = \frac{4k_BTR}{V²_\Phi} \approx \frac{16k_BTL^2}{R}$$For realistic values $L = 200$pH, $R=6\Omega$ and $T = 4.2$k, the noise is around $1.2\mu \Phi_0/\sqrt{Hz}$ approaching the quantum limit.
3. Magnetic sensitivity. To maximize sensitivity to magnetic fields, the loop area should be large. However, increasing loop area increases inductance, which conflicts with the earlier requirement for high sensitivity. This is resolved using a superconducting transformer, which transfers the field to smaller loop while maintaining sensitivity around $1fT/\sqrt{Hz}$

### 1.2.4 Classical Digital Circuits
Not important


## 1.3 Towards Quantum computing with superconducting Qubits

### 1.3.1 Bloch Sphere Representation
A superconducting qubit, built using JJs, is a two level quantum system that can be represented as a superposition of two states. The Bloch sphere provides a geometric representation of the qubit's quantum state, where the north and south poles correspond to the basis states $\ket{0}$ and $\ket 1$, respectively. The Bloch vector, given by $\ket \Psi = \alpha \ket 0 + \beta \ket 1$ has a unit length of pure states. 
![[Pasted image 20250217160138.png]]
The z-axis represents the qubit's quantization axis, while the x-y plane represents transverse components. The quantum state can be parameterized using angles $\theta$ and $\phi$, with:
$$\ket \psi = \cos(\theta/2)\ket 0 + e^{i\phi}\sin(\theta/2)\ket 1 $$
In a rotating reference frame, the Bloch vector appears stationary, simplifying visualization. The density matrix $\rho = \ket \psi \bra \psi$ is expressed in terms of Pauli Matrices, and its trace condition distinguishes pure $Tr(\rho²)=1$ and mixed states $0 \leq Tr(\rho²) < 1$. The Bloch sphere's surface represents pure states, while its interior represents mixed states.  

### 1.3.2 Qubit Control
In this section, we will introduce how superconducting qubits are manipulated to implement quantum algorithms. The transmons variant of superconducting qubits re the most extensively utilized mean for implementing quantum programs. However, the techniques presented can be extended to all categories of superconducting qubits. The single-qubit and two-qubit operations together form the basis of many of the medium-scale superconducting quantum processors that exist today. We write everything in the computational basis $\{\ket 0, \ket 1\}$, where $\ket 0$ is the $+1$ eigenstate of $\sigma_z$ and $\ket 1$ is the $-1$ eigenstate. To indicate the rotation operator of a qubit state (rotation around x-axis by $\theta$ angle), we use the notation:
$$
X_\theta = R_X (\theta) = e^{-i \frac \theta 2 \sigma_x} = \cos(\theta/2) - i\sin(\theta/2)\sigma_x
$$
and we use the shorthand notation "X" for a full $\pi$ rotation about the x-axis.

### 1.3.3 Boolean Logic Gates in Classical Computers
In classical boolean logic, bits can take one of two values: 0 -False, 1- True. 
Single-bit gates:
	Identity gate- leaves bit unchanged
	NOT gate - flips the bit (0->1,1->0), reversible
Two-bit gate:
	AND: outputs 1 if both inputs are 1, otherwise outputs 0
	OR: outputs 1 if at least one is 1
	NAND: combines NOT and AND, outputs 0 only when both inputs are 1
	NOR: combines NOT and OR, outputs 1 only when both are 0
	XOR: Exclusively OR, outputs 1 if inputs are different, otherwise 0
	XNOR (NOT XOR), outputs 1 if inputs are the same

Most two-bit gates are irreversible
Universality  in Boolean Logic:
	A universal gate set can perform any boolean logic operation
	EX:
		NOT+AND form a universal set
		NAND and NOR are individually universal, meaning Boolean function can be built using only NAND or NOR gates
	The choice of gate set impacts implementation efficiency

![[Pasted image 20250217173503.png]]


### 1.3.4 Quantum Logic Gates Used in Quantum Computers
Quantum logic operations, like classical Boolean logic, can be implemented using a small set of fundamental gates. However, unlike classical bits, qubits can exist in superpositions of states $\ket 0$ and $\ket 1$ and can be represented on the Bloch sphere

Single-qubit gates:
Single-qubit gates perform rotations of the Bloch vector, transforming one quantum state into another. These gates include:
	Identity gate: Leaves qubit unchanged
	Pauli Gates (X,Y,Z): Rotate the qubit by $\pi$ around the respective axis
	S and T gates: perform $\pi/2$ and $\pi/4$ rotations around the z-axis
	Hadamard Gate: Creates superpositions by rotating around an axis in the x-z plane. 

Two-qubit gates:
Two-qubit gates apply unitary operations to one qubit based on the state of the other.
	Controlled NOT (CNOT): Flips the target qubit if the control qubit is $\ket 1$
	Controlled phase (CPHASE or CZ): Applies a Z gate to the target qubit if the control qubit is $\ket 1$
	iSWAP Gate: Can be constructed from CNOT and single-qubit gates

Entanglement and universality
Some two-qubit gates, like CNOT and CPHASE, create entanglement, generating states that cannot be factored into suparate qubit components. These entangling gates along with single-qubit gates, form a universal quantum gate set, capable of implementing any quantum algorithm.

Reversibility and Unitarity
Unlike classical irreversible gates, quantum gates are reversible because they are based on unitary operations $U$, meaning their inverse $U^\dagger$ can always restore the original state.
Thus, quantum gates provide the foundation for quantum computation, enabling complex operations like superposition, entanglement and universal quantum logic.

![[Pasted image 20250217174540.png]]


### 1.3.5 Classical Versus Quantum Gates

The gate-sequences in quantum algorithms have certain similarities to those used in classical computing, with a few differences.

The classical NOT gate flips a bit (0 <-> 1)
The quantum X (often called "guantum NOT gate")gate swaps the amplitudes of the qubits wavefunction.  It behaves like a classical NOT gate only when applied to $\ket 0$ and $\ket 1$.

All Quantum gates are unitary and thus reversible
Classical logic gates like NAND and NOR are not reversible and have no direct quantum counterpart.

Irreversible processes, such as measurement and energy loss, are describes using amplitude damping and phase damping.

Quantum circuits are written left to right, but mathematically applied right to left

A universal classical gate set include NAND or NOR
A universal quantum gate set consists of:
	Arbitrary single-qubit rotations
	At least one entangling two-qubit gate
Any two-qubit gate can be decomposed into a sequence of CNOT gates using Krauss-Cirac decomposition.

### 1.3.5.1 Minimum Gate Sets
A universal quantum gate set is
$$
\mathcal G_0 = [X_\theta,Y_\theta,Z_\theta,Ph_\theta,CNOT]
$$
where $Ph_\theta = e^{i\theta}$ applies an overall phase $\theta$ to a single qubit. 
Another gate set:
$$
\mathcal G_1 = [H,S,T,CNOT]
$$
H-Hadamard, S-Phase, T-$\pi/8$ phase gate, CNOT: Entangling gate.

The Solovay-Kitaev theorem ensures that any arbitrary single-qubit gate can be approximated using only $\mathcal G_1$, with an error $\epsilon$ as $O(log^g(1/\epsilon))$.

Different quantum processors have native gates that are easier to implement based on their hardware
Gate synthesis and gate compilation optimize the gate sequence to reduce the total operation time (circuit depth).

Hadamard gate can be constructed from $\mathcal G_0$ gates as:
$$H = Ph_{\pi/2}Y_{\pi/2}Z_\pi$$
In superconducting quansum processors, $X_\theta,Y_\theta,Z_\theta$ are typically native gates.


### 1.3.6 Further Developments for Superconducting Qubits
Superconducting qubits are a proising platform for medium-scale quantum processors, and research continues:

Quantum Annealing:
Superconducting qubits are used in quantum annealing , which finds the ground state of a Hamiltionian to solve optimization problems
D-wave has developed quantum annealing processors with over 2000 qubits, based on flux qubit-designs

3D Cavity-Based Superconducting Qubits:
These encode quantum information in photonic modes of a cavity, using cat states for enhanced coherence.
High-quality cavities improve coherence times and reduce hardware overhead for error correction.
This architecture has enabled error-corrected qubits with extended lifetimes.

Error Correction Challenges:
Despite improvements in qubit lifetimes and gate fidelity, error correction remains essential for scaling up quantum processors.
The surface code has been successfully demonstrated with superconducting qubits, but achieving a logical qubit that outlives its physical qubits is still a challenge.
Fault-tolerant universal computation requires additional techniques, such as state distillation to implement a T gate.
Gate teleportation has been demonstrated, but full state distillation and injection into a logical state is an open problem.

Future Directions:
New Quantum error-correcting codes are being explored to improve fault tolerance.
Remote entanglement is a key goal for distributing quantum computation.
The major challenge ahead is a key goal for distributed quantum computation.
The major challenge ahead is achieving quantum computational supremacy, where a quantum processor performs a task beyond classical capabilities.
Recent advances using 9 tunable transmons are moving toward this goal with full supremacy expected at hundreds of qubits.




### Note:
Cooper pairs: pair of electrons bound together at low temperatures in a certain manner

