# 	Fundamentals-of-Deep-Learning
Here is where I document my learning of Deep Learning.

---

## The Neuron

The idea of a neuron being used in a machine learning model was pioneered by Warren S. McCulloch and Walter H. Pitts. Similarly to a biological neuron, an artificial neuron contains:

- An **input** vector `X`. 

Each of which are multiplied by:

-  A **weight** vector `W`.

A dot product is then applied to the weight and input vectors to produce the **logit**. Example;
$$
X = [1, 2, 3] \\
W = [0.1, 0.2, 0.3] \\
logit = [1,2,3] \cdot [0.1, 0.2, 0.3] \\
logit = 1 \times 0.1 + 2 \times 0.2 + 3 \times 0.3 \\
\therefore logit = 1.4
$$
In most cases a **logit** also includes a **bias**, `b`. Producing a final equation:
$$
y = f(x\cdot w + b)
$$

---

## Linear Perceptron

A linear perceptron can be easily represented by a singular neuron. 

<img src=".\images\Perceptron.jpg" style="zoom:50%;" />

- For example a neuron given:

  - The following information the day before an exam can be used to determine if a student will pass an exam: **hours studied and time slept.**

  

However, this is severely limited. This leads us to **Feed-Forward Neural Networks**

# Feed-Forward Neural Networks

