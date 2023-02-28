# 

## Week 0 & 1: 20.02.2023 - 26.02.2023 & 27.02.2023 - 05.03.2023

Getting started, getting an idea of probabilistic model checking.
### Resources consulted:
* [PRISM website](https://www.prismmodelchecker.org/): Installation of PRISM, discovered that PRISM can be applied on a wide range of probabilistic models:
    - discrete-time Markov chains (DTMCs)
    - continuous-time Markov chains (CTMCs)
    - Markov decision processes (MDPs)
    - probabilistic automata (PAs)
    - probabilistic timed automata (PTAs)
    - partially observable Markov decision processes (POMDPs)
    - partially observable probabilistic timed automata (POPTAs) 

and discovered that PRISM uses BDDs and MTDDs (Multi terminal decision diagrams)
> PRISM incorporates state-of-the art symbolic data structures and algorithms, based on BDDs (Binary Decision Diagrams) and MTBDDs (Multi-Terminal Binary Decision Diagrams)

* [Brief look at PRISM syntax for modelling a PTA: Probabilistic Timed Automata](https://www.prismmodelchecker.org/talks/dave-cav11.pdf): Can intuitively define a PTA (at least the one in the presentation slide)

* [Tutorial Part 1](https://www.prismmodelchecker.org/tutorial/die.php): Getting started with PRISM on simple dice example (DTMC: Discrete Time Markov Chain).
**PRISM** have at least these:

    **Model**
    - Can define easily a basic DTMC model in PRISM from the graphical representation of the DTMC model.
    - Can add basic rewards counting the number of steps. Therefore, can ask (in the property tab) what is the average number of steps we get a dice number.
    - Need to specify what kind of model it is: DTMC ? MDP (Markov Decision Process) ? etc.

    **Simulator**
    - Can simulate/sample paths in the DTMC
    - Can choose manually which transition to take
    - Can reset the path
    - Can choose the number of steps to take in the system.

    **Properties**
    - Can ask what is the probability that a property is true.
    - Can verify/check whether the probability, e.g bigger or equal to some value is true.
    - Can ask what is the expected cumulative reward (see expected return without discount in reinforcement learning) with some conditions.
    - Can plot via "Experiments" for example the probabilities that a property is true with different values of a variable. Can export the graph, modify legends etc. Can also use simulations to estimate empirically the probabilities instead of their iterative algorithm (dependent on what kind model we have)

    **Options**
    - Can change solution methods (e.g MDP solution method from Value Iteration to Policy Iteration or to Linear Programming etc.)
    - Can change "accuracy"/"stopping condition" by changing termination criteria and termination epsilon.

* [(Theory) PCTL](https://en.wikipedia.org/wiki/Probabilistic_CTL): brief look at what it is. Essentially, it is CTL extended to real time probabilistic models. PCTL is used to **check DTMC** models.
    - More flexibility than ALL paths or EXIST one path due to the **probabilities**.
    - More flexibility if want to verify that properties **hold within some time period/unit** (e.g 4 seconds).

* [(Theory) PCTL more formal details and explanation on why it's an extension of CTL](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=ed5c504d718ec782b0c1db81d5fd6c36f268aee4): See section 3 for properties expressible with PCTL.

* [P operator in PRISM](https://www.prismmodelchecker.org/manual/PropertySpecification/ThePOperator):
    - `P bound [ pathprop ]` informally expresses "the probability that path property pathprop is satisfied by the paths from state s meets the bound bound" (quote from the link)
    - Specifying properties in PRISM does not require users to explicitely specify what model checking to use.

* [PRISM FAQ, Max model size](https://www.prismmodelchecker.org/manual/FrequentlyAskedQuestions/PRISMModelling#max_model_size):
    - The number of states can be around $10^7$
    - Variable ordering matters:
    > Because PRISM is a symbolic model checker, the amount of memory required to store the probabilistic model can vary (sometime unpredictably) according to several factors. One example is the order in which the variables of your model appear in the model file. In general, there is no definitive answer to what the best ordering is but the following heuristics are a good guide.

### Current objective(s):
* Understand some limitations of PRISM (about property verification or efficiency/optimization/performance etc.) (e.g order of the lines in the model description affects efficiency due to the construction of BDDs or MTBDDs ([See FAQ of PRISM](https://www.prismmodelchecker.org/manual/FrequentlyAskedQuestions/PRISMModelling#max_model_size))) 

* More case studies than just Dice example from tutorial

### Next goal(s):
* Limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into explicit models)
* Theory: start reading [PRISM lectures](https://www.prismmodelchecker.org/lectures/pmc/)
* PRISM: start reading the other tutorials and the manual
* More PRISM case studies and [survey](https://www.prismmodelchecker.org/papers/arcras-pmc.pdf).

## Issues:
* Installation on Windows 10 due to Java version: Not fixed yet but no issue installing on linux.
