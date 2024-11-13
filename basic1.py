import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Streamlit app title
st.title("SIR Model Simulation")

# User inputs for the initial conditions and parameters
location = st.text_input("Enter the name of the Region:", "Region X")
N = st.number_input("Enter the total population:", min_value=1, value=1000000)
I0 = st.number_input("Enter the initial number of infected individuals:", min_value=0, value=1)
R0 = st.number_input("Enter the initial number of recovered individuals:", min_value=0, value=0)
beta = st.slider("Enter the infection rate (beta):", 0.0, 1.0, 0.3)
gamma = st.slider("Enter the recovery rate (gamma):", 0.0, 1.0, 0.1)

# Initialize model values
S = N - I0 - R0
I = I0
R = R0

susceptible = [S]
infected = [I]
recovered = [R]

num_days = 300

# Calculate the model over time
for _ in range(num_days):
    S_new = S - beta * S * I / N
    I_new = I + beta * S * I / N - gamma * I
    R_new = R + gamma * I

    S = S_new
    I = I_new
    R = R_new

    susceptible.append(S)
    infected.append(I)
    recovered.append(R)

# Create the plot
fig, ax = plt.subplots()
ax.plot(susceptible, label="Susceptible")
ax.plot(infected, label="Infected")
ax.plot(recovered, label="Recovered")
ax.set_xlabel("Time (days)")
ax.set_ylabel("Number of individuals")
ax.set_title(f"SIR Model Simulation: {location}")
ax.legend()

# Display the plot
st.pyplot(fig)

# Optionally, show data in a table
st.subheader("Simulation Data (Final Day)")
data = pd.DataFrame({
    "Susceptible": [susceptible[-1]],
    "Infected": [infected[-1]],
    "Recovered": [recovered[-1]]
})
st.write(data)

