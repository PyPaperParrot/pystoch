# PyStoch

This package designed for stochastic processes simulation and their analysis. 

## Package's architecture
- pystoch
    - __init__.py
	- SDEprocesses
		- __init__.py
		- explicit.py
		- implicit.py
	- SDEsystems.py
	- analysis.py
	- exceptions.py
- setup.py
- README.md
- LICENSE

## Processes
This package provide uers with tools for generating some common discrete-time stochastic models. Models were taken from **S. Stepanov. "Stochastic world"**.

**SDEprocesses** module contains one-dimensional processes:
* SDE in general form
* LogWalk
* Orstein-Ulenbek process
* Brownian trap
* Brownian bridge
* Feller process

in implicit and explicit forms.


**SDEsystems** module contains systems of SDE:
* Damped Oscillator
* Linear system in general form
* Correlated wandering

**analysis** module contains some analysis tools for SDE analysis
