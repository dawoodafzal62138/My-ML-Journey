# Dice Simulation 

## 📌 Project Overview
This project is a Python-based, interactive demonstration of the **Law of Large Numbers (LLN)**. Through automated simulations of dice rolls, this project visualizes how the experimental probability ($P_e$) of an event converges to its theoretical probability ($P_t$) as the number of trials ($n$) approaches infinity.

The project is split into two main Jupyter Notebooks:
* **Single Die Simulation:** Demonstrates convergence on a uniform distribution.
* **Multiple Dice Simulation:** Demonstrates convergence on a non-uniform (bell-shaped) distribution by summing the results of two dice.

---

## 🧮 Mathematical Background
This project bridges the gap between perfect mathematical expectations and real-world random variations using three core concepts:

### 1. Theoretical Probability ($P_t$)
The expected outcome in a perfect system, calculated before any experiments are run.
$$P_t = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

### 2. Experimental Probability ($P_e$)
The actual observed outcome after running trials.
$$P_e = \frac{f}{n}$$
*(where $f$ is the frequency of the desired outcome, and $n$ is the total number of trials)*

### 3. The Law of Large Numbers
The theorem stating that as the sample size grows, the experimental probability will equal the theoretical probability.
$$\lim_{n \to \infty} P_e = P_t$$

---

## 🔬 Simulations Included

### Phase 1: Single Die Simulation (`dice_simulation.ipynb`)
Simulates the rolling of a standard 6-sided die.
* **Distribution:** Uniform.
* **Expected Result:** Every outcome (1, 2, 3, 4, 5, 6) has an identical theoretical probability of exactly $\frac{1}{6} \approx 0.1667$. The charts demonstrate the frequencies flattening out equally as $n$ scales up to 100,000,000 rolls.

### Phase 2: Multiple Dice Simulation (`dice_simulation_multiple_dice.ipynb`)
Simulates rolling two 6-sided dice and summing their values (ranging from 2 to 12).
* **Distribution:** Non-uniform (bell-shaped).
* **Expected Result:** The probabilities are weighted based on the 36 possible combinations. For example:
  * **Sum = 2 or 12:** 1 combination $\rightarrow \frac{1}{36} \approx 0.0278$
  * **Sum = 7:** 6 combinations $\rightarrow \frac{6}{36} \approx 0.1667$ *(Most likely outcome)*
* The charts in this simulation visualize the experimental data molding into a Gaussian-like curve over millions of rolls.

---

## 🛠️ Technologies Used
* **Python 3.x:** Core programming language.
* **NumPy (`numpy`):** Used for fast, large-scale randomized number generation (`np.random.default_rng`) and array manipulation (`np.unique`).
* **Matplotlib (`matplotlib.pyplot`):** Used for graphing and visually tracking the convergence of probabilities.
* **Jupyter Notebook:** Interactive environment used to display code execution step-by-step alongside markdown explanations.

---

## 🚀 Installation

### Prerequisites
Make sure you have Python installed, along with Jupyter Notebook and the required libraries. You can install the dependencies using pip:

```bash
pip install numpy matplotlib jupyterlab
```

---
# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Dawood Afzal**