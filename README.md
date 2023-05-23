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

## Importing our Case Study

Next, download our model, investor_verification.nm, and property list, properties.props. Once in the graphical UI, import the model with Model -> Open Model, and point it to investor_verification.nm. Similarly, go to Properties -> Open properties list, and point it to properties.props.

## Running the Case Study

Paths in our model can be sampled through the bottom tab Simulator, and Properties can be verified through the bottom tab Properties.

