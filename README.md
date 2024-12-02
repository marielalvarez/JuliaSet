This repository contains a script for generating and animating Julia sets. 

- The Julia set is defined as:
  
  $$J_c = {z_0 \in \mathbb{C} \; | \; \text{the sequence } \{z_n\}_{n=0}^\infty \text{ is bounded}}$$

- To identify points outside the Julia set, we check if $|z_n| > 2$:

  $$\text{If } \exists n \text{ such that } |z_n| > 2, \text{ then } z_0 \notin J_c$$

This script allows you to customize the complex parameter $c$ and visualize how the Julia set evolves over time.

Save the script as julia_animation.py. and run the script from the command line:
```
python julia_animation.py -0.8 0.156
```
<div align="center">
  <img src="animatedJulia.gif" alt="Animated Julia Set" width="500"/>
</div>
