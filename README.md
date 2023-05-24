# Advanced Formal Tools: Project 7. Probabilistic Model Checking with PRISM

Members:
- NGUYEN Stéphane Liem
- RAHMAN Tansen

The goal of this project is to explore the domain of probabilistic model checking, which consists of leveraging probabilistic models to analyse programs.

Equipped with the PRISM probabilistic model checker, we can define and verify properties of models of small distributed applications (e.g., cyber physical systems) and/or concurrent programs.

We first define the mathematical background and formalism. We then explain how this data and models are represented and encoded in the PRISM tool and PRISM language. We finally explore a case study given on the PRISM site, extend it, and analyze some properties.

## PRISM Installation

PRISM is known to run on Linux, Windows and Mac OS X, both 64-bit and 32-bit versions.

You will need Java, version 9 or above (get it, for example from Oracle or AdoptOpenJDK). To run binary versions of PRISM, you only need the Java Runtime Environment (JRE), not the full Java Development Kit (JDK).

To compile PRISM from source, you need the Java Development Kit (JDK), GNU make and a C/C++ compiler (e.g. gcc/g++). For compilation under Windows, you will need Cygwin. See below for more information and steps:

https://www.prismmodelchecker.org/manual/InstallingPRISM/Instructions

## Importing our Case Study into PRISM

From the `src` folder, download our:
 - model: `investor_verification.nm`
 - property list: `properties.props`

Once in the graphical UI, import:
 - the model with `Model` $\rightarrow$ `Open Model`, and point it to `investor_verification.nm`
 - the properties with `Properties` $\rightarrow$ `Open properties list`, and point it to `properties.props`

## Running the Case Study from the GUI

There are 4 different tabs at the bottom:
- `Model`: where you can modify the model
- `Simulator`: where you can simulate paths in the model and can even pick which state you want next.
- `Properties`: where you can design properties, verify them, export the results, plot the results.
- `Log`: where you can see possible warnings about deadlocks and also see the output of different other tools
from the tabs at the top of the tool (e.g `Model` $\rightarrow$ `Compute` $\rightarrow$ `Steady-State probabilities`).

Once the properties are imported, you should see different formulas inside the `Properties` box in the `Property` tab.
There are different ways to verify a property after right-clicking on it such as:
- `Verify`: verifies a property using some iterative algorithm for a single combination of parameter values (or constants)
- `Simulate`: same but by sampling many trajectories within the system instead of using the iterative algorithm
- `Experiments`:
	- verifies a property for many combinations of parameter values (or constants),
either using an iterative algorithm or using sampled paths.
	- can export the results into CSV
	- can directly plot inside PRISM (but limited capabilities)
	

