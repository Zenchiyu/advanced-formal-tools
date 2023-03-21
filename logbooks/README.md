# Logbooks

(S): Stéphane Nguyen
(T): Tansen Rahman

(S&T): Both

## Week 0 & 1: 20.02.2023 - 26.02.2023 & 27.02.2023 - 05.03.2023

Getting started, getting an idea of probabilistic model checking.
### Resources consulted:
* (T)[Project 6: CTL model checker without "pre"](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.469.1817&rep=rep1&type=pdf): Reading the paper before choosing which project to take.

> The goal of this project is to formalise and implement a simple CTL model checker without "pre".
Resources:
CTL Model Checking Based on Forward State Traversal: A paper describing a CTL model checking algorithm based on forward state traversal.

We decided to move forward with PRISM as it was more interesting and had less of an initial learning curve.

* (S&T)[PRISM website](https://www.prismmodelchecker.org/): Installation of PRISM, discovered that PRISM can be applied on a wide range of probabilistic models:
    - discrete-time Markov chains (DTMCs)
    - continuous-time Markov chains (CTMCs)
    - Markov decision processes (MDPs)
    - probabilistic automata (PAs)
    - probabilistic timed automata (PTAs)
    - partially observable Markov decision processes (POMDPs)
    - partially observable probabilistic timed automata (POPTAs) 

and discovered that PRISM uses BDDs and MTDDs (Multi terminal decision diagrams)
> PRISM incorporates state-of-the art symbolic data structures and algorithms, based on BDDs (Binary Decision Diagrams) and MTBDDs (Multi-Terminal Binary Decision Diagrams)

* (S)[Brief look at PRISM syntax for modelling a PTA: Probabilistic Timed Automata](https://www.prismmodelchecker.org/talks/dave-cav11.pdf): Can intuitively define a PTA (at least the one in the presentation slide)

* (S&T)[Tutorial Part 1](https://www.prismmodelchecker.org/tutorial/die.php): Getting started with PRISM on simple dice example (DTMC: Discrete Time Markov Chain).
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

* (S)[(Theory) PCTL](https://en.wikipedia.org/wiki/Probabilistic_CTL): brief look at what it is. Essentially, it is CTL extended to real time probabilistic models. PCTL is used to **check DTMC** models.
    - More flexibility than ALL paths or EXIST one path due to the **probabilities**.
    - More flexibility if want to verify that properties **hold within some time period/unit** (e.g 4 seconds).

* (S)[(Theory) PCTL more formal details and explanation on why it's an extension of CTL](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=ed5c504d718ec782b0c1db81d5fd6c36f268aee4): See section 3 for properties expressible with PCTL.

* (S)[P operator in PRISM](https://www.prismmodelchecker.org/manual/PropertySpecification/ThePOperator):
    - `P bound [ pathprop ]` informally expresses "the probability that path property pathprop is satisfied by the paths from state s meets the bound bound" (quote from the link)
    - Specifying properties in PRISM does not require users to explicitely specify what model checking to use.

* (S)[PRISM FAQ, Max model size](https://www.prismmodelchecker.org/manual/FrequentlyAskedQuestions/PRISMModelling#max_model_size):
    - The number of states can be around $10^7$
    - Variable ordering matters:
    > Because PRISM is a symbolic model checker, the amount of memory required to store the probabilistic model can vary (sometime unpredictably) according to several factors. One example is the order in which the variables of your model appear in the model file. In general, there is no definitive answer to what the best ordering is but the following heuristics are a good guide.

* (T)Presentation slides

### Current objective(s):
* Understand some limitations of PRISM (about property verification or efficiency/optimization/performance etc.) (e.g order of the lines in the model description affects efficiency due to the construction of BDDs or MTBDDs ([See FAQ of PRISM](https://www.prismmodelchecker.org/manual/FrequentlyAskedQuestions/PRISMModelling#max_model_size))) 

* More case studies than just Dice example from tutorial

### Next goal(s):
* Limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
* Theory: start reading [PRISM lectures](https://www.prismmodelchecker.org/lectures/pmc/)
* PRISM: start reading the other tutorials and the manual
* More PRISM case studies and [survey](https://www.prismmodelchecker.org/papers/arcras-pmc.pdf).

## Issues:
* Installation on Windows 10 due to Java version: Not fixed yet but no issue installing on linux.

## Week 2: 06.03.2023 - 12.03.2023

### Resources consulted:
* (S) [Quick peak at computation engines](http://www.prismmodelchecker.org/manual/ConfiguringPRISM/ComputationEngines)

* (S) [Quick peak at PCTL in the PRISM lectures](https://www.prismmodelchecker.org/lectures/pmc/05-dtmc%20model%20checking.pdf): Took a brief look at the syntax and `Prob(X φ)`

* (S&T) [Quick peak at some case studies](http://www.prismmodelchecker.org/casestudies/index.php). Discovered that we can "combine two such processes in asynchronous parallel composition" in order to create for example multiple philoshophers without rewriting everything because philosophers behave similarly. Many interesting applications, such as randomized code, detecting security breaches.

### Current objective(s):
* Same as previously but with a bigger focus on case studies.

### Next goal(s):
* Limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
* ~~Theory: start reading [PRISM lectures](https://www.prismmodelchecker.org/lectures/pmc/)~~ (Deemed less important. We must focus on an interesting case study with real life applications)
* PRISM: start reading the other tutorials and the manual
* More PRISM case studies and [survey](https://www.prismmodelchecker.org/papers/arcras-pmc.pdf).

## Week 3: 13.03.2023 - 19.03.2023

### Resources consulted:
* (S)[PRISM filters](http://www.prismmodelchecker.org/manual/PropertySpecification/Filters): We can get the set of states, check from multiple states instead of just the initial state. How to specify multiple initial states in the model ?
* (S)[PRISM many expressions](http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Expressions): negation, if and only if, implication, log, modulo etc.
* (S)[PRISM limitation, no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

```
[reply]  receiver=2 & y1=0 -> 1/(maxr+1) : (receiver'=3) & (y1'=0) // reply and make random choice
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*1)
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*2)
	                    etc.
                         + 1/(maxr+1) : (receiver'=3) & (y1'=2*127)
```
where `maxr` was 127.
* (S&T)[PRISM publications (both internal and external)](https://www.prismmodelchecker.org/publ-lists.php)
* (S&T)[PRISM benchmark suite](https://www.prismmodelchecker.org/benchmarks/): List of possible interesting properties one can check for different models.


### Current objective(s):
* Look into game case studies using PRISM-games extension. See [PRISM-games](https://www.prismmodelchecker.org/games/).
* Pick an interesting case study the above or from general [PRISM publications](https://www.prismmodelchecker.org/publ-lists.php).
* Look into ideas of our own case study. Possible game theory problem, such as markets with buyers and sellers. Can investigate properties like what is the probability that x product is sold out?
* Find more limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
    - Can we have reward distributions ?
    * Known limitation: [no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

```
[reply]  receiver=2 & y1=0 -> 1/(maxr+1) : (receiver'=3) & (y1'=0) // reply and make random choice
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*1)
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*2)
	                    etc.
                         + 1/(maxr+1) : (receiver'=3) & (y1'=2*127)
```

### Next goal(s):

* More on reward distributions ? [Reward based properties](http://www.prismmodelchecker.org/manual/PropertySpecification/Reward-basedProperties)
* Non determinism vs probabilistic ? [MDP non determinism](https://www.prismmodelchecker.org/lectures/biss07/04-mdps.pdf)
* State-space explosion and "solutions" [Advanced topics](https://www.prismmodelchecker.org/lectures/biss07/11-advanced%20topics.pdf) 

## Week 4: 19.03.2023 - 26.03.2023

### Resources consulted:
* (S)[Turned-Based stochastic game definition](https://www.prismmodelchecker.org/papers/arcras-pmc.pdf): We saw very briefly that a Turned-based stochastic game is an extension of a Markov Decision Process for multiple players where some states from the MDP "uniquely belong" to some players. In other words, a player can only play/make decisions in some states.

* (S&T)[Futures Market Investor case study](https://www.prismmodelchecker.org/casestudies/investor.php): Tansen found this MDP case study. It might be interesting to extend it or take inspiration from it.
    - Adding more rewards
    - Adding more investors, multiplayer (maybe Turned-based stochastic game in PRISM-games)
    - etc.

We modified the case study to introduce:
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] (is_done=0) -> (is_done'=1 );
endmodule
```
and
```
rewards
    [done] true : v;  // reward from transition [done]
endrewards
```
see files in `../presentation_2` folder and the next bullet point.

* (S) PRISM limitation; no direct way to check a property on a transition based on a transition label: No direct way for example to ask what is the expected cumulative reward/return from the initial state until reach an absorbing state but where we don't know its explicit expression. Where we only know the transition label from which we can reach this absorbing state.

One way is to add a variable that will be used to track the absorbing state via the transition label:
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] (is_done=0) -> (is_done'=1 );
endmodule
```


### Current objective(s):
* Look into game case studies using PRISM-games extension. See [PRISM-games](https://www.prismmodelchecker.org/games/).
* Pick an interesting case study the above or from general [PRISM publications](https://www.prismmodelchecker.org/publ-lists.php).
* Look into ideas of our own case study. Possible game theory problem, such as markets with buyers and sellers. Can investigate properties like what is the probability that x product is sold out?
* Find more limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
    - Can we have reward distributions ?
    * Known limitation: [no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

```
[reply]  receiver=2 & y1=0 -> 1/(maxr+1) : (receiver'=3) & (y1'=0) // reply and make random choice
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*1)
	                    + 1/(maxr+1) : (receiver'=3) & (y1'=2*2)
	                    etc.
                         + 1/(maxr+1) : (receiver'=3) & (y1'=2*127)
```
    * No direct way to check a property on a transition based on a transition label

### Next goal(s):

* More on reward distributions ? [Reward based properties](http://www.prismmodelchecker.org/manual/PropertySpecification/Reward-basedProperties)
* Non determinism vs probabilistic ? [MDP non determinism](https://www.prismmodelchecker.org/lectures/biss07/04-mdps.pdf)
* State-space explosion and "solutions" [Advanced topics](https://www.prismmodelchecker.org/lectures/biss07/11-advanced%20topics.pdf) 


