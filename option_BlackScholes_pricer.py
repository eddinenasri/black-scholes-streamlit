import streamlit as st
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

# ===============================
# Black-Scholes Functions
# ===============================
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# ===============================
# Streamlit Config
# ===============================
st.set_page_config(page_title="Black-Scholes Option Pricer", layout="wide")
st.title("📊 Black-Scholes Option Pricing")

# ===============================
# Sidebar Inputs
# ===============================
st.sidebar.header("Option Parameters")

S0 = st.sidebar.number_input("Current Asset Price S₀", 100.0)
K  = st.sidebar.number_input("Strike Price K", 100.0)
T  = st.sidebar.number_input("Time to Maturity T (Years)", 1.0)
sigma_input = st.sidebar.number_input("Volatility σ", 0.2)
r  = st.sidebar.number_input("Risk-Free Rate r", 0.05)

st.sidebar.markdown("---")
st.sidebar.header("Heatmap Parameters")

min_s = st.sidebar.number_input("Min Spot Price", 50.0)
max_s = st.sidebar.number_input("Max Spot Price", 150.0)
min_vol = st.sidebar.slider("Min Volatility", 0.01, 1.0, 0.05)
max_vol = st.sidebar.slider("Max Volatility", 0.01, 1.0, 0.8)

# ===============================
# Current Option Prices
# ===============================
call_val = black_scholes_call(S0, K, T, r, sigma_input)
put_val  = black_scholes_put(S0, K, T, r, sigma_input)

col1, col2 = st.columns(2)
col1.metric("Call Option Price", f"${call_val:.2f}")
col2.metric("Put Option Price", f"${put_val:.2f}")

st.markdown("---")

# ===============================
# Heatmap Data
# ===============================
S_range = np.linspace(min_s, max_s, 60)
vol_range = np.linspace(min_vol, max_vol, 60)
vol_grid, S_grid = np.meshgrid(vol_range, S_range, indexing="ij")

call_matrix = black_scholes_call(S_grid, K, T, r, vol_grid)
put_matrix  = black_scholes_put(S_grid, K, T, r, vol_grid)

# ===============================
# Call Heatmap
# ===============================
fig_call = go.Figure(go.Heatmap(
    z=call_matrix,
    x=S_range,
    y=vol_range,
    colorscale="Viridis",
    colorbar=dict(title="Call Price"),
    hovertemplate="S=%{x:.2f}<br>σ=%{y:.2f}<br>Price=%{z:.2f}<extra></extra>"
))
fig_call.add_vline(x=S0, line_dash="dash", line_color="red")

fig_call.update_layout(
    title="Call Option Price Heatmap",
    xaxis_title="Spot Price S",
    yaxis_title="Volatility σ",
    height=650
)

# ===============================
# Put Heatmap
# ===============================
fig_put = go.Figure(go.Heatmap(
    z=put_matrix,
    x=S_range,
    y=vol_range,
    colorscale="Plasma",
    colorbar=dict(title="Put Price"),
    hovertemplate="S=%{x:.2f}<br>σ=%{y:.2f}<br>Price=%{z:.2f}<extra></extra>"
))
fig_put.add_vline(x=S0, line_dash="dash", line_color="red")

fig_put.update_layout(
    title="Put Option Price Heatmap",
    xaxis_title="Spot Price S",
    yaxis_title="Volatility σ",
    height=650
)

# ===============================
# Display
# ===============================
st.subheader("Options Price – Interactive Heatmaps")

tab1, tab2 = st.tabs(["Call Heatmap", "Put Heatmap"])

with tab1:
    st.plotly_chart(fig_call, use_container_width=True, key="call")

with tab2:
    st.plotly_chart(fig_put, use_container_width=True, key="put")
