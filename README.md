# Solving peg solitaire by reinforcement learning 

In this repo we have built a reinforcement learning system according
to the Actor-Critic model, and applied it to Peg Solitaire.
The overall architecture is shown in the figure below.
The agent (the reinforcement learner) consists of an 
actor and a critic, where the actor holds the action policy and adjusts
this policy by receiving messages (the Temporal Difference error) from the critic.
The agent is built as a stand-alone general purpose model which can be applied to
any kind of game environment.
Here it is used to solve Peg Solitaire. As shown in the figure, 
the game is represented by a Simulated World that holds the rules of 
the game and knows the transitions between states by actions. 

![actor-critic](/images/actor-critic_rl-system.jpg)
#### The basic components of an Actor-Critic reincforcement learning system for playing Peg Solitaire. The red dotted arrows represents communication related to learning.



Progression of learning | Averaged progression | Last game 
------------ | ------------- | -------------
![pegs left](/images/example_run/pegs_left.png) | ![avg pegs](/images/example_run/average_pegs_left.png) | ![game](/images/example_run/game.gif) 





<br/>

#### Eliot & Markus