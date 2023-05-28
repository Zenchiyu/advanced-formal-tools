# Advanced Formal Tools: Project 7. Probabilistic Model Checking with PRISM: Investor in Market case study

Members:
- NGUYEN Stéphane Liem
- RAHMAN Tansen

The goal of this project is to explore the domain of probabilistic model checking, which consists of leveraging probabilistic models to analyse programs.

Equipped with the PRISM probabilistic model checker, we can define and verify properties of models of small distributed applications (e.g., cyber physical systems) and/or concurrent programs.

We first define the mathematical background and formalism. We then explain how this data and models are represented and encoded in the PRISM tool and PRISM language. We finally explore a case study given on the PRISM site, extend it, and analyze some properties.

<!---
<p align="center">
  <img src="./presentations/presentation_2/images/market_time_series.png" />
</p>
--->
<p align="center">
  <img src="./src/images/market_dynamics.gif" />
</p>

## Structure of project

```
├── logbooks
│   ├── image.png
│   └── README.md
├── presentations
│   ├── presentation_1
│   │   └── ...
│   ├── presentation_2
│   │   └── ...
│   ├── presentation_3
│   │   └── ...
│   └── presentation_4
│       └── ...
├── README.md
├── report
│   └── ...
└── src
    ├── images
    │   ├── all_res.PNG
    │   └── max_avg_reward_different_interest.PNG
    ├── investor_verification.nm
    ├── market_time_series.py
    ├── mdp_example.nm
    ├── mdp_example_given_policy.nm
    ├── properties.props
    ├── properties_mdp_example.props
    ├── properties_mdp_example_given_policy.props
    ├── read_all_res.py
    ├── results
    │   ├── all_res.csv
    │   ├── max_avg_reward_interest_0_5.csv
    │   ├── max_avg_reward_interest_1.csv
    │   ├── max_avg_reward_interest_minus_0_5.csv
    │   └── max_avg_reward_interest_minus_1.csv
    └── surface_plot_results.py
```

- The `report` folder contains as the name suggests, our report.
- The `src` folder contains our final PRISM model, PRISM properties file and related codes to plot our results. This folder also contains two examples `mdp_example` (a Markov Decision Process) and `mdp_example_given_policy` (a Markov Reward Process representing the MDP example in which a policy is given).
- The `logbooks` folder records, in its `README.md`, details of what we did every week in this project.
- The `presentations` folder contains folders for each presentation. These folder include the presentation slides as well as a version of our case study and related codes.

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

One can also try a simple MDP example we created with:
 - model: `mdp_example.nm`
 - property list: `properties_mdp_example.props`

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
	

