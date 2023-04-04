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

### Resources consulted or work done:
* (S)[Turned-Based stochastic game definition](https://www.prismmodelchecker.org/papers/arcras-pmc.pdf): We saw very briefly that a Turned-based stochastic game is an extension of a Markov Decision Process for multiple players where some states from the MDP "uniquely belong" to some players. In other words, a player can only play/make decisions in some states.

* (S&T)[Futures Market Investor case study](https://www.prismmodelchecker.org/casestudies/investor.php): Tansen found this MDP case study. It might be interesting to extend it or take inspiration from it.
    - Adding more rewards
    - Adding more investors, multiplayer (maybe Turned-based stochastic game in PRISM-games)
    - etc.

We (S&T) modified the case study to introduce:

```
module my_done_module
    is_done : [0..1] init 0; 
    [done] is_done=0 -> (is_done'=1);
    // Move the absorbing state to this one below where we don't get any reward !
    [absorb] is_done=1 -> (is_done'=1);
endmodule
```
and
```
rewards
    [done] true : v;  // reward from transition [done]
endrewards
```
see files in `../presentation/presentation_2` folder and the next bullet point.

(T) also modified
```
// bar on the investor
module barred
    
    b : [0..1] init 1; // initially cannot bar
    // b=0 - not barred and b=1 - barred

    [invest] true  -> (b'=0); // do not bar this month
    [invest] (b=0) -> (b'=1); // bar this month (cannot have barred the previous month) 

endmodule
```
to
```
// bar on the investor
module barred

    b : [0..1] init 1; // initially cannot bar
    // b=0 - not barred and b=1 - barred

    [invest] (b=1) -> (b'=0); // do not bar this month
    [invest] (b=0) -> 0.3: (b'=1) + 0.7: (b'=0); // bar this month (cannot have barred the previous month) 
    
endmodule
```
but (S) changed it to:
```
// bar on the investor
module barred

    b : [0..1] init 1; // initially cannot bar
    // b=0 - not barred and b=1 - barred

    [invest] (b=1) -> (b'=0); // do not bar this month
    [invest] (b=0) -> p_bar: (b'=1) + (1-p_bar): (b'=0); // bar this month (cannot have barred the previous month) 
    
endmodule
```
and added constants that can be used in the [experiments](https://www.prismmodelchecker.org/manual/RunningPRISM/Experiments).
```
const double p_bar;
const int v_init;
```
and changed `v : [0..10] init 10` into `v : [0..10] init v_init;`

* (S) PRISM limitation; no direct way to check a property on a transition based on a transition label: No direct way for example to ask what is the expected cumulative reward/return from the initial state until reach an absorbing state but where we don't know its explicit expression. Where we only know the transition label from which we can reach this absorbing state.

One way is to add a variable that will be used to track the absorbing state via the transition label:
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] true -> (is_done'=1 );
endmodule
```
However, if we also have this:
```
rewards
    [done] true : v;  // reward from transition [done]
endrewards
```
It would create infinite rewards because of the absorbing state having the "done" transition that has a transition reward attached to it.
Therefore, we have to replace our `my_done_module` by:
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] is_done=0 -> (is_done'=1);
    // Move the absorbing state to this one below where we don't get any reward !
    [absorb] is_done=1 -> (is_done'=1);
endmodule
```
We can then verify some properties using `is_done`.

* (S) Provided a Python code plotting a time series for the Futures Market Investor:

![img](../presentations/presentation_2/images/market_time_series.png)

* (S) Provided a Python code showing a surface plot replicated the one in the case study (after exporting PRISM experiment as a list in CSV):

![img](../presentations/presentation_2/images/prism_results.PNG)

Surface plot from the case study:

![img](../presentations/presentation_2/images/investor-case-study-results.PNG)

### Current objective(s):
* Look into game case studies using PRISM-games extension. See [PRISM-games](https://www.prismmodelchecker.org/games/).
* Extend the Futures Market Investor case study
* Find more limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
    - Can we have reward distributions ?
    - Known limitation: No direct way to check a property on a transition based on a transition label
    - Known limitation: [no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

### Next goal(s):

* More on reward distributions ? [Reward based properties](http://www.prismmodelchecker.org/manual/PropertySpecification/Reward-basedProperties)
* Non determinism vs probabilistic ? [MDP non determinism](https://www.prismmodelchecker.org/lectures/biss07/04-mdps.pdf)
* State-space explosion and "solutions" [Advanced topics](https://www.prismmodelchecker.org/lectures/biss07/11-advanced%20topics.pdf) 

## Issues:
* (S) PRISM warning us that we had deadlocks with 
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] (is_done=0) -> (is_done'=1 );
endmodule
```
We fixed it by writing `true` (includes `(is_done=1)`) instead of `(is_done=0)` alone. However, no need to use these if we use (which is what we're using):
```
module my_done_module
    is_done : [0..1] init 0; 
    [done] is_done=0 -> (is_done'=1);
    // Move the absorbing state to this one below where we don't get any reward !
    [absorb] is_done=1 -> (is_done'=1);
endmodule
```
because `is_done` is always $0$ at the beginning then changes to $1$. From $1$, we can never go back to $0$ so it's fine. The "absorb" transition is the only one used from the absorbing states having `is_done=1`.

* (S) `Rmax=?[F is_done=1]` giving infinite rewards in our modified Futures Market Investor case study. Might be because there's some [non-zero proba that we never end up in a state with this property](http://www.prismmodelchecker.org/manual/FrequentlyAskedQuestions/PRISMProperties#inf_rewards). However, `Rmax=?[C<=t]` works/gives values (using the iterative algorithm; Value Iteration) that correspond to the case study (see probability to bar at $0.3$ for initial value $v=10$. The maximum expected sale price is 9.5):

![img](../presentations/presentation_2/images/RmaxCumulativeVI.PNG)


However, if we use "simulation", it will lead to different values:

![img](../presentations/presentation_2/images/RmaxCumulative.PNG)

PRISM warned us by saying `Warning: For simulation, nondeterminism in MDP is resolved uniformly (resulting in DTMC).` Therefore, we shouldn't use "simulations"
for these kind of tasks (because there's no reinforcement learning involved).

## Week 5: 27.03.2023 - 02.04.2023

### Resources consulted or work done:
* (S&T) Brainstormed ideas for extending the Futures Market Investor:
    - (S) Investor can reinvest into the market.
    - (S) We can change the end condition to a time limit, so we can look at properties in respect to some time metric.
    - (T) We can add some time reward to the investments.
    - (S&T) We can add another investor and analyze properties using PRISM-games.
    - (T) We can implement an actual future, where two investors/players need to agree on a price now, and execute the trade later.
    - (T) We can also implement rollover in order to potentially increase their return.
    - (T) We will need to add some conditions to avoid a zero-sum game case where nothing in the market occurs, since the players will never be able to agree on a price.
    - (T) We could add commissions for buying/selling stock -> changes to non-zero sum game.

* (S) Implemented some of the above ideas (see `../presentations/presentation_3/` folder):
    - Can have more than one investment/delivery within time horizon. This extension breaks "If in a given month the investor does not reserve, then at the very next month the market can temporarily bar the investor from reserving. But the market cannot bar the investor in two consecutive months."
    - The market cannot bar initially and cannot bar the investor in two consecutive months. **The market can bar even if the investor reserved the previous month !**
    - Time horizon. Fixed number of months until reaches absorbing state.
    - Variable tracking the month.
    - Can also deliver last month

    ![img](../presentations/presentation_3/images/investing_every_month_no_barring.PNG)

### Current objective(s):
* Look into game case studies using PRISM-games extension. See [PRISM-games](https://www.prismmodelchecker.org/games/).
* Extend the Futures Market Investor case study
* Find more limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
    - Can we have reward distributions ?
    - Known limitation: No direct way to check a property on a transition based on a transition label
    - Known limitation: [no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

### Next goal(s):

* More on reward distributions ? [Reward based properties](http://www.prismmodelchecker.org/manual/PropertySpecification/Reward-basedProperties)
* Non determinism vs probabilistic ? [MDP non determinism](https://www.prismmodelchecker.org/lectures/biss07/04-mdps.pdf)
* State-space explosion and "solutions" [Advanced topics](https://www.prismmodelchecker.org/lectures/biss07/11-advanced%20topics.pdf) 

## Week 6: 03.04.2023 - 09.04.2023

### Resources consulted or work done:

* (S) Verified some properties based on current extended market investor model:
    - We already had `Rmax=? [ C<=t ]`
    - `Rmax=? [ F is_done=1 ]` now works ! So we can use it instead of the previous formula even though the previous one can be used to check implicitely the number of steps.
    - `Pmin=? [F<=(2*tmax+1) is_done=1]` is it unreachable in the worst case within this amount of steps ? Can we complete all the months within this amount of steps ? (Note that tmax was the maximum number of months). It might be better to rename `tmax`.
    - `Rmin=? [ F is_done=1 ]` What is the minimum reward you can accumulate until reach the end ? (This needs to be fixed because there's a warning in PRISM stating: `Warning: PRISM hasn't checked for zero-reward loops. Your minimum rewards may be too low...`)
    - `Pmin=? [F<=(3*tmax+1) is_done=1]` What is the worst probability to reach the end state within 3 tmax + 1 steps (recall that we have the transitions labelled: `invest`, `month`, `delivery` and `done` (once at the end if do not take into account the infinite loop with the absorbing state). The maximum number of steps is when an investor tries to invest every month).
    - `Pmax=? [F<=(2*tmax+1) is_done=1]` What is the best probability to reach the end state within 2 tmax + 1 steps ? If it's a probability of $1$, then it's possible to reach it within the described number of steps.
    - `Pmax=? [F<=tmax is_done=1]` What about within tmax steps ?  If the probability is $0$, it's impossible to finish earlier.

* (S) Started to think about multiple reward structures and nested properties. What are the limitations in terms of nested properties ? Can we reuse a result obtained by verifying another property ?

### Current objective(s):
* Look at multiple modules & reward structures.
* Is it possible to have a reward property giving some value inside a P property ? 
* Look into game case studies using PRISM-games extension. See [PRISM-games](https://www.prismmodelchecker.org/games/).
* Extend the Futures Market Investor case study
* Find more limitations of PRISM:
    - What about big models ? Can we import data "into PRISM language" ? (Maybe dive into [explicit models](http://www.prismmodelchecker.org/manual/Appendices/ExplicitModelFiles))
    - Can we have reward distributions ?
    - Known limitation: No direct way to check a property on a transition based on a transition label
    - Known limitation: [no for loops, no lists or compact way to write the following in the Bluetooth case study](http://www.prismmodelchecker.org/casestudies/bluetooth.php)

### Next goal(s):

* More on reward distributions ? [Reward based properties](http://www.prismmodelchecker.org/manual/PropertySpecification/Reward-basedProperties)
* Non determinism vs probabilistic ? [MDP non determinism](https://www.prismmodelchecker.org/lectures/biss07/04-mdps.pdf)
* State-space explosion and "solutions" [Advanced topics](https://www.prismmodelchecker.org/lectures/biss07/11-advanced%20topics.pdf) 
