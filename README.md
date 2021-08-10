# 	Fundamentals-of-Deep-Learning
Here is where I document my learning of Deep Learning.

- [Training theory](./Training.md)
- [Multilayer Perceptron](./MLP)
  - [Binary - Ionosphere Dataset](./MLP/MLP_Binary.ipynb)
  - [Multiclass - Iris Dataset](.MLP/MLP_Multiclass_Classification.ipynb)
  - [Regression - Boston Housing Dataset](./MLP/MLP_Regression.ipynb)

---

## The Neuron

The idea of a neuron being used in a machine learning model was pioneered by Warren S. McCulloch and Walter H. Pitts. Similarly to a biological neuron, an artificial neuron contains:

- An **input** vector `X`. 

Each of which are multiplied by:

-  A **weight** vector `W`.

A dot product is then applied to the weight and input vectors to produce the **logit**. Example;

<img src=".\images\Logit.png" />

In most cases a **logit** also includes a **bias**, `b`. Producing a final equation:

<img src=".\images\Logit2.png"/>

---

## Linear Perceptron

A linear perceptron can be easily represented by a singular neuron. 

<img src=".\images\Perceptron.jpg" style="zoom:50%;" />

- For example a neuron given:

  - The following information the day before an exam can be used to determine if a student will pass an exam: **hours studied and time slept.**

  

However, this is severely limited. This leads us to **Feed-Forward Neural Networks**

# Feed-Forward Neural Networks

Feed-Forward Neural Networks are networks consisting of layers of nodes. The network consists of three types of layers, an Input Layer, Hidden Layer(s), and an Output Layer. 

The Hidden layers are **Dense**, meaning that all nodes in the Hidden Layer have inputs from all nodes in the previous layer and outputs to all nodes in the next layer.

<img src=".\images\Feed_forward_neural_net.png" alt="Feed_forward_neural_net" style="zoom:70%;" />

A few important notes:

1. Having **fewer neurons per layer** in the hidden layers are usually recommended. This is as it forces the network to **learn compressed representations** of original input.

2. Having all neurons connect to all in the next layer is **not required**. It is an important skill to determine which neurons to connect.

## Limitations of Linear Neurons

Neuron types are defined by the activation function type, `f`, that they apply to the **logit ** `z`.

**Linear Neurons are very limited as a feed-forward network consisting of only linear neurons can be expressed as a network with no hidden layers.**

- This is problematic as hidden layers are what enables us to learn important features from the data / problem.
  - This makes it hard to learn about complex relationships.

There are 3 basic neurons that can be used.

### Sigmoid Neurons

The sigmoid function is below and produces an s shape:

<img src=".\images\sigmoid-f.png" />

The function transforms the input from, **x** in [-1, 1] to **S(x)** in [0, 1].

<img src=".\images\sigmoid-g.png" style="zoom:25%;" />

- When the logit is small, the output of a sigmoid neuron is close to 0.
- When the logit is large, the output of a sigmoid neuron is close to 1. 

### Tanh Neurons

The tanh function is similar in shape to the Sigmoid Function, except it ranges from -1 to 1.

The Tanh function is expressed as: ***f(z) = tanh(z)*.**

### ReLU Neurons

The *Restricted Linear Unit (ReLU)* neuron is unlike the other two. It produces a hockey stick shaped graph.

The ReLU function is expressed as: ***f(z) = max(0, z)*.**

<img src=".\images\ReLU-g.png" style="zoom:33%;" />

---

## SoftMax Output Layers

If we want our output vectors to be a probability distribution over a set of mutually exclusive labels:

- MNIST data set, handwritten digit between 0 to 9.
  - Each label is mutually exclusive.

Therefore, the **SoftMax Layer** is unlike other layers, as the output is determined by the outputs of other neurons on the same layer. This is as **we require the sum of all outputs to equal 1.**

The formula can be seen below:

<img src=".\images\SoftMax-f.png"/>

**This generates a strong prediction being an output in a vector being close to 1.** If multiple outputs in the vector have **similarly high strengths then the prediction is weak**.
