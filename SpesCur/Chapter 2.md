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