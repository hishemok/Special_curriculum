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