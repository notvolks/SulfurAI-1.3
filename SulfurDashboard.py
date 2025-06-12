################ Welcome to SulfurAI  dashboard!
### Functions here should be modified with proper intent.
### This python script was written in the Holly format. To find out how it works go into VersionDATA/HollyFormat/ReadMe.txt
### This python script is designed to host all SulfurAI API functions for python and run via the __main__ tag.

### LAYOUT:
# ---------------GOING DOWN!
#####-Imports call_file_path (important dependancy)
#####-Installing all pip files
#####-Importing all files
#####-Running dash (the host)


#####################------------------------------------------------INBUILT FUNCTIONS------------------------------------------------
def _get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

# Call file paths
call = _get_call_file_path()

import sys
import subprocess
import importlib
import threading
import os


# Upgrade pip tools
def _upgrade_pip_tools():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        print("Warning: Failed to upgrade pip tools.")

# Install Python packages
def _install(packages):
    if isinstance(packages, str):
        packages = [packages]

    _upgrade_pip_tools()
    for pkg in packages:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print(f"Failed to install {pkg}.")

# Import safely with auto-install
def _safe_import(module_name, package_name=None):
    pkg = package_name or module_name
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"{pkg} not found. Installing...")
        _install(pkg)
        return importlib.import_module(module_name)

# Install required Python packages
modules = ["streamlit", "dash","pandas"]
for mod in modules:
    _safe_import(mod)

import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components


# --- Data & Chart Setup ---
df = pd.read_csv("VersionDATA/ai_renderer_2/training_data_sentences/data.csv")
intent_counts = df["intent"].value_counts(normalize=True) * 100
fig = px.pie(
    names=intent_counts.index,
    values=intent_counts.values,
    title="Intent Distribution",
    template="plotly_dark"
)
bg = fig.layout.paper_bgcolor
chart_html = fig.to_html(include_plotlyjs="cdn", full_html=False)

# --- Build the wrapper HTML & JS with black outline background ---
wrapper_html = """
<style>
  .custom-wrapper { margin:0; padding:0; }

  /* outline + moving shine slice */
  #shine-ring {
    position:absolute; top:0; left:0; right:0; bottom:0;
    background-color: #111111 !important;      /* <-- pure black outline */
    border-radius:12px;
    box-shadow: none;                       /* glow off by default */
    border:5px solid transparent;
    border-image: conic-gradient(
      from var(--angle,0deg) at center,
      rgba(255,255,255,0.8) 0deg 20deg,
      rgba(255,255,255,0) 20deg 360deg
    ) 1;
    z-index:1;
    transition: box-shadow 0.2s ease;
  }

  /* keep the chart inside using its original Plotly bg */
  #chart-layer {
    position:relative; z-index:2; padding:20px;
    background-color: %(bg)s !important;
    border-radius:12px;
    transition: transform 0.1s ease-out;
  }
</style>

<div id="chart-container" class="custom-wrapper" style="
    position:relative; width:100%%; max-width:600px; height:600px;
    margin:30px auto; font-size:0;
">
  <div id="shine-ring"></div>
  <div id="chart-layer">
    %(chart_html)s
  </div>
</div>

<script>
  const container  = document.getElementById('chart-container');
  const ring       = document.getElementById('shine-ring');
  const chartLayer = document.getElementById('chart-layer');

  function getCenterAndRadius() {
    const r = container.getBoundingClientRect();
    const cx = r.width/2, cy = r.height/2;
    return { cx, cy, r: Math.min(cx, cy) - 12 };
  }

  container.addEventListener('mousemove', e => {
    const rect = container.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const c = getCenterAndRadius();
    const cx = c.cx, cy = c.cy, r = c.r;

    // rotate the highlight slice
    const ang = (Math.atan2(my - cy, mx - cx) * 180/Math.PI + 360) %% 360;
    ring.style.setProperty('--angle', ang + 'deg');

    // parallax
    const dx = (mx - cx)/r, dy = (my - cy)/r;
    chartLayer.style.transform = `translate(${dx*8}px, ${dy*8}px)`;
  });

  container.addEventListener('mouseenter', () => {
    // enable glow on hover
    ring.style.boxShadow = '0 0 25px 12px rgba(255,165,0,0.6)';
  });
  container.addEventListener('mouseleave', () => {
    // disable glow & reset
    ring.style.boxShadow = 'none';
    chartLayer.style.transform = 'translate(0,0)';
  });

  // Function to update the chart type
  function updateChartType(chartType) {
    fig.update_layout(template=chartType);
    chart_html = fig.to_html(include_plotlyjs="cdn", full_html=False);
    document.getElementById('chart-layer').innerHTML = chart_html;
  }
</script>
""" % {'bg': bg, 'chart_html': chart_html}

# Display the HTML content
components.html(wrapper_html, height=620, scrolling=True)