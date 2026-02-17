import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NEXTMIND Dashboard",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/run"

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "expanded_graph" not in st.session_state:
    st.session_state.expanded_graph = None

# ---------------- PLOT HELPERS ----------------
def plot_curiosity(df, expanded=False):
    if expanded:
        fig, ax = plt.subplots(figsize=(8, 5), dpi=120)
    else:
        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)

    ax.plot(df["curiosity_score"], marker="o")
    ax.set_title("Curiosity Over Time", fontsize=10)
    ax.set_xlabel("Run", fontsize=8)
    ax.set_ylabel("Score", fontsize=8)
    ax.tick_params(labelsize=8)
    return fig


def plot_decisions(df, expanded=False):
    if expanded:
        fig, ax = plt.subplots(figsize=(8, 5), dpi=120)
    else:
        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)

    df["analysis_decision"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Accept vs Reject", fontsize=10)
    ax.set_ylabel("Count", fontsize=8)
    ax.tick_params(labelsize=8)
    return fig


# ---------------- UI HEADER ----------------
st.title("🧠 NEXTMIND — Artificial Scientist Dashboard")

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("Input Parameters")

uncertainty = st.sidebar.slider(
    "Uncertainty", 0.0, 1.0, 0.8, 0.05
)

embedding_x = st.sidebar.slider("Embedding X", 0.0, 1.0, 0.9)
embedding_y = st.sidebar.slider("Embedding Y", 0.0, 1.0, 0.1)

run_btn = st.sidebar.button("Run NEXTMIND")

# ---------------- API CALL ----------------
if run_btn:
    payload = {
        "uncertainty": uncertainty,
        "novelty": 0.0,   # backward compatibility
        "embedding": [embedding_x, embedding_y]
    }

    res = requests.post(API_URL, json=payload)

    if res.status_code == 200:
        st.session_state.history.append(res.json())
    else:
        st.error("API Error")

# ---------------- OUTPUT METRICS ----------------
if st.session_state.history:
    latest = st.session_state.history[-1]

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Curiosity Score", round(latest["curiosity_score"], 3))
    m2.metric("Hypothesis", latest["hypothesis"])
    m3.metric("Analysis Decision", latest["analysis_decision"])
    m4.metric("Meta Decision", latest["meta_decision"])

    df = pd.DataFrame(st.session_state.history)

    st.markdown("---")
    st.subheader("📊 Analytics Overview")

    # ---------------- GRID VIEW ----------------
    c1, c2, c3 = st.columns([1, 1, 1])

    with c1:
        st.pyplot(plot_curiosity(df), use_container_width=False)
        if st.button("🔍 Expand Curiosity"):
            st.session_state.expanded_graph = "curiosity"

    with c2:
        st.pyplot(plot_decisions(df), use_container_width=False)
        if st.button("🔍 Expand Decisions"):
            st.session_state.expanded_graph = "decisions"

    with c3:
        st.info("ℹ️ Click expand to view graphs in detail")

# ---------------- EXPANDED VIEW ----------------
if st.session_state.expanded_graph:
    st.markdown("---")
    st.subheader("🔎 Expanded View")

    if st.button("❌ Close Expanded View"):
        st.session_state.expanded_graph = None

    df = pd.DataFrame(st.session_state.history)

    if st.session_state.expanded_graph == "curiosity":
        st.pyplot(plot_curiosity(df, expanded=True), use_container_width=True)

    elif st.session_state.expanded_graph == "decisions":
        st.pyplot(plot_decisions(df, expanded=True), use_container_width=True)
