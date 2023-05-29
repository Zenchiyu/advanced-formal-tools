# Advanced Formal Tools: Project 7. Probabilistic Model Checking with PRISM: Investor in Market case study

Members:
- NGUYEN Stéphane Liem
- RAHMAN Tansen

The goal of this project is to explore the domain of probabilistic model checking, which consists of leveraging probabilistic models to analyse programs.

Equipped with the [PRISM probabilistic model checker](http://www.prismmodelchecker.org), we can define and verify properties of models of small distributed applications (e.g., cyber physical systems) and/or concurrent programs.

PRISM was created and is actively maintained by:
- Dave Parker (University of Oxford)
- Gethin Norman (University of Glasgow)
- Marta Kwiatkowska (University of Oxford) 

In the report, we first define the mathematical background and formalism. We then explain how this data and models are represented and encoded in the PRISM tool and PRISM language. We finally explore a case study given on the PRISM site, extend it, and analyze some properties.

<!---
<p align="center">
  <img src="./presentations/presentation_2/images/market_time_series.png" />
</p>
--->
<div align='center'>
  Market value of a stock for different initial market value 
  <img src="./src/images/market_dynamics.gif" />
</div>

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
├── documentation
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

- The `documentation` folder contains our report as well as our final presentation slides.
- The `src` folder contains our final PRISM model, PRISM properties file and related codes to plot our results. This folder also contains two examples `mdp_example` (a Markov Decision Process) and `mdp_example_given_policy` (a Markov Reward Process representing the MDP example in which a policy is given).
- The `logbooks` folder records, in its `README.md`, details of what we did every week in this project.
- The `presentations` folder contains folders for each presentation. These folder include the presentation slides as well as a version of our case study and related codes.

## PRISM Installation


Our project is based on PRISM version 4.7 and the installation instructions are detailed in [the PRISM's website](https://www.prismmodelchecker.org/manual/InstallingPRISM/Instructions). For instance, they state that:

> PRISM is known to run on Linux, Windows and Mac OS X, both 64-bit and 32-bit versions.

> You will need Java, version 9 or above (get it, for example from Oracle or AdoptOpenJDK). To run binary versions of PRISM, you only need the Java Runtime Environment (JRE), not the full Java Development Kit (JDK).

> To compile PRISM from source, you need the Java Development Kit (JDK), GNU make and a C/C++ compiler (e.g. gcc/g++). For compilation under Windows, you will need Cygwin.

Their README from their [github](https://github.com/prismmodelchecker/prism) also adds some explanation.


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

## Running the Case Study from the CLI

The following commands, if adapted with the correct paths for the model, properties and outputs, should give you the CSV files of our results.

The following command should give our `all_res.csv` results:
```
prism investor_verification.nm properties.props -prop 1,2,5,6 -const p_bar=0:0.1:1,interest=0,v_init=0:1:10,tmax=12,max_stocks=12 -exportresults all_res.csv:csv
```

The other results were obtained using
```
prism investor_verification.nm properties.props -prop 1 -const p_bar=0:0.1:1,interest=0.5,v_init=0:1:10,tmax=12,max_stocks=12 -exportresults max_avg_reward_interest_0_5.csv:csv

prism investor_verification.nm properties.props -prop 1 -const p_bar=0:0.1:1,interest=1,v_init=0:1:10,tmax=12,max_stocks=12 -exportresults max_avg_reward_interest_1.csv:csv

prism investor_verification.nm properties.props -prop 1 -const p_bar=0:0.1:1,interest=-0.5,v_init=0:1:10,tmax=12,max_stocks=12 -exportresults max_avg_reward_interest_minus_0_5.csv:csv

prism investor_verification.nm properties.props -prop 1 -const p_bar=0:0.1:1,interest=-1,v_init=0:1:10,tmax=12,max_stocks=12 -exportresults max_avg_reward_interest_minus_1.csv:csv
```

If there are any errors, it might come from path issues.

## References
[1] FOREJT, V., KWIATKOWSKA, M., NORMAN, G., AND PARKER, D. Automated Verification Techniques for Probabilistic
Systems. In Formal Methods for Eternal Networked Software Systems, M. Bernardo and V. Issarny, Eds., vol. 6659.
Springer Berlin Heidelberg, Berlin, Heidelberg, 2011, pp. 53–113. Series Title: Lecture Notes in Computer Science.

[2] HANSSON, H., AND JONSSON, B. A Logic for Reasoning about Time and Reliability. Formal Aspects of Computing
6 (Feb. 1995).

[3] KWIATKOWSKA, M., NORMAN, G., AND PARKER, D. PRISM 4.0: Verification of Probabilistic Real-Time Systems. In
Computer Aided Verification, G. Gopalakrishnan and S. Qadeer, Eds., vol. 6806. Springer Berlin Heidelberg, Berlin,
Heidelberg, 2011, pp. 585–591. Series Title: Lecture Notes in Computer Science.

[4] KWIATKOWSKA, M., NORMAN, G., AND PARKER, D. Probabilistic Model Checking and Autonomy. Annual Review
of Control, Robotics, and Autonomous Systems 5, 1 (2022), 385–410. _eprint: https://doi.org/10.1146/annurev-control-042820-010947


