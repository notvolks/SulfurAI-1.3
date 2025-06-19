################ Welcome to SulfurAI dashboard!
### Functions here should be modified with proper intent.
### This python script was written in the Holly format. To find out how it works go into VersionDATA/HollyFormat/ReadMe.txt
### This python script is designed to host all SulfurAI API functions for python and run via the __main__ tag.

### LAYOUT:
# ---------------GOING DOWN!
#####-TOS reminder
#####-Imports call_file_path (important dependency)
#####-Installing all pip files
#####-Importing all files
#####-Running all creative files + dependancies
#####-Running the server/ webapp

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from VersionDATA.ai_renderer import error
import time
print_verti_list = error.print_verti_list

# Print Terms of Service on direct run
if __name__ == "__main__":
    TOS = [
        "--------------------------------------------------------------------------------------------------",
        "By using this application you agree to the Terms of Service listed in the project files.",
        "If you do not consent, stop using our services.",
        "If you cannot find it, install a new version OR look in the root folder for 'Terms of Service.txt'.",
        "--------------------------------------------------------------------------------------------------",
    ]
    print_verti_list(TOS)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import subprocess
import importlib

#####################------------------------------------------------INBUILT FUNCTIONS------------------------------------------------

def _get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

# Call file paths
call = _get_call_file_path()

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

# Safe import with install retry
def _safe_import(module_name, package_name=None):
    pkg = package_name or module_name
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"{pkg} not found. Installing...")
        _install(pkg)
        time.sleep(2)
        try:
            return importlib.import_module(module_name)
        except ImportError:
            print(f"Failed to import {pkg} even after installation.")
            return None

# Ensure required packages
modules = ["streamlit", "dash", "pandas", "plotly","pywebview"]
for mod in modules:
    _safe_import(mod)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from pathlib import Path
import webbrowser
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

def load_training_data_txt(filepath):
    import pandas as pd
    data = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) == 3:
                    sent_str, location, accuracy = parts
                    sent_clean = sent_str.strip("[]").strip("'").strip('"')
                    try:
                        accuracy_val = float(accuracy)
                    except ValueError:
                        accuracy_val = None
                    data.append({
                        "sentence": sent_clean,
                        "location": location,
                        "accuracy": accuracy_val
                    })
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Failed to load .txt data: {e}")
        return None

def render_glowing_section(title, dataframes, graph_names):
    import pandas as pd
    import plotly.express as px
    import streamlit.components.v1 as components

    inner_charts_html = []
    chart_ids = []

    for idx, df in enumerate(dataframes):
        if df is None or df.empty:
            continue

        # Adapt columns based on data available
        if 'intent' in df.columns:
            col = 'intent'
        elif 'location' in df.columns:
            col = 'location'
        else:
            col = df.columns[0]  # fallback

        intent_counts = df[col].value_counts(normalize=True) * 100

        pie_fig = px.pie(names=intent_counts.index, values=intent_counts.values,
                         title=graph_names[idx]["pie"], template="plotly_dark")
        bar_fig = px.bar(x=intent_counts.index, y=intent_counts.values,
                         title=graph_names[idx]["bar"],
                         labels={"x": col.capitalize(), "y": "%"},
                         template="plotly_dark")
        line_fig = px.line(x=intent_counts.index, y=intent_counts.values,
                           title=graph_names[idx]["line"],
                           labels={"x": col.capitalize(), "y": "%"},
                           template="plotly_dark")

        for fig in (pie_fig, bar_fig, line_fig):
            fig.update_layout(width=200, height=200, margin=dict(l=5, r=5, t=25, b=5))

        if col == "location":
            width, height = 400, 400
        else:
            width, height = 300, 300



        pie_html = pie_fig.to_html(include_plotlyjs="cdn", full_html=False)
        bar_html = bar_fig.to_html(include_plotlyjs=False, full_html=False)
        line_html = line_fig.to_html(include_plotlyjs=False, full_html=False)
        bg = '#111111'
        chart_id = f"{title.lower().replace(' ', '')}-{idx}"
        chart_ids.append(chart_id)

        chart_html = f"""
         <div class="glowing-chart" id="chart-{chart_id}" style="background-color:{bg};">
           <div class="chart-ring"></div>
           <div class="slider-wrapper">
               <div class="slider-ring"></div>
               <input id="slider-{chart_id}" type="range" min="0" max="2" value="0" style="width:100%; margin-bottom:5px;">
          </div>
           <div id="pie-{chart_id}">{pie_html}</div>
           <div id="bar-{chart_id}" style="display:none">{bar_html}</div>
           <div id="line-{chart_id}" style="display:none">{line_html}</div>
         </div>
         """
        inner_charts_html.append(chart_html)

    # JS to handle chart type switching
    chart_scripts = ""
    for cid in chart_ids:
        chart_scripts += f"""
        document.getElementById('slider-{cid}').addEventListener('input', e => {{
            document.getElementById('pie-{cid}').style.display = e.target.value === '0' ? 'block' : 'none';
            document.getElementById('bar-{cid}').style.display = e.target.value === '1' ? 'block' : 'none';
            document.getElementById('line-{cid}').style.display = e.target.value === '2' ? 'block' : 'none';
        }});
        """

    full_html = f"""
    <style>
      .glowing-section {{
          position: relative;
          border: 3px solid #FFA500;
          border-radius: 20px;
          background-color: #222222;
          padding: 20px;
          margin: 20px auto 40px auto;
          box-shadow: 0 8px 30px rgba(255,165,0,0.5);
          color: white;
          max-width: 950px;
          display: flex;
          gap: 20px;
          flex-wrap: wrap;
          justify-content: center;
          transition: transform 0.2s ease;
          cursor: pointer;
      }}
      .glowing-section-title {{
          font-family: 'Roboto', sans-serif;
          font-size: 2rem;
          font-weight: 700;
          color: #FFA500;
          text-align: center;
          text-shadow: 0 0 8px rgba(255,165,0,0.9);
          margin-bottom: 15px;
          width: 100%;
      }}
      #ring {{
          pointer-events: none;
          position: absolute;
          top: -8px; left: -8px; right: -8px; bottom: -8px;
          border-radius: 24px;
          border: 5px solid transparent;
          border-image: conic-gradient(from var(--angle, 0deg), rgba(255,255,255,0.8) 0deg 20deg, rgba(255,255,255,0) 20deg 360deg) 1;
          z-index: 1;
          transition: box-shadow 0.2s ease;
      }}
      .glowing-chart {{
          position: relative;
          border-radius: 12px;
          width: 220px;
          padding: 10px;
          box-shadow: 0 4px 12px rgba(255,165,0,0.3);
          flex-shrink: 0;
          transition: transform 0.2s ease;
          cursor: pointer;
          overflow: visible;
      }}
      .glowing-chart .chart-ring {{
          pointer-events: none;
          position: absolute;
          top: -5px; left: -5px; right: -5px; bottom: -5px;
          border-radius: 18px;
          border: 3px solid transparent;
          border-image: conic-gradient(from var(--angle, 0deg), rgba(255,255,255,0.8) 0deg 20deg, rgba(255,255,255,0) 20deg 360deg) 1;
          z-index: 2;
          transition: box-shadow 0.2s ease;
      }}
      .slider-wrapper {{
          position: relative;
          width: 100%;
          padding: 4px;
          border-radius: 12px;
          margin-bottom: 10px;
          box-shadow: 0 2px 8px rgba(255,165,0,0.25);
          transition: transform 0.2s ease;
          overflow: visible;
          cursor: pointer;
      }}
      .slider-ring {{
          pointer-events: none;
          position: absolute;
          top: -4px; left: -4px; right: -4px; bottom: -4px;
          border-radius: 14px;
          border: 2px solid transparent;
          border-image: conic-gradient(from var(--angle, 0deg), rgba(255,255,255,0.8) 0deg 20deg, rgba(255,255,255,0) 20deg 360deg) 1;
          z-index: 1;
          transition: box-shadow 0.2s ease;
      }}
    </style>

    <div class="glowing-section" id="section-container">
      <div id="ring"></div>
      <div class="glowing-section-title">{title}</div>
      {"".join(inner_charts_html)}
    </div>

    <script>
      // Section glow
      const section = document.getElementById('section-container');
      const ring = document.getElementById('ring');
      function center() {{
          const b = section.getBoundingClientRect();
          return {{ x: b.width / 2, y: b.height / 2, r: Math.min(b.width, b.height) / 2 }};
      }}
      section.addEventListener('mousemove', e => {{
          const rect = section.getBoundingClientRect();
          const mx = e.clientX - rect.left, my = e.clientY - rect.top;
          const m = center();
          const ang = (Math.atan2(my - m.y, mx - m.x) * 180 / Math.PI + 360) % 360;
          ring.style.setProperty('--angle', ang + 'deg');
          section.style.transform = `translate(${{(mx - m.x) / m.r * 8}}px, ${{(my - m.y) / m.r * 8}}px)`;
      }});
      section.addEventListener('mouseenter', () => {{
          ring.style.boxShadow = '0 0 25px 12px rgba(255,165,0,0.6)';
      }});
      section.addEventListener('mouseleave', () => {{
          ring.style.boxShadow = 'none';
          section.style.transform = 'translate(0,0)';
      }});

      // Chart glow
      document.querySelectorAll('.glowing-chart').forEach(chart => {{
          const ring = chart.querySelector('.chart-ring');
          chart.addEventListener('mousemove', e => {{
              const rect = chart.getBoundingClientRect();
              const mx = e.clientX - rect.left, my = e.clientY - rect.top;
              const cx = rect.width / 2, cy = rect.height / 2;
              const ang = (Math.atan2(my - cy, mx - cx) * 180 / Math.PI + 360) % 360;
              ring.style.setProperty('--angle', ang + 'deg');
              chart.style.transform = `translate(${{(mx - cx) / cx * 4}}px, ${{(my - cy) / cy * 4}}px)`;
          }});
          chart.addEventListener('mouseenter', () => {{
              ring.style.boxShadow = '0 0 20px 8px rgba(255,165,0,0.7)';
          }});
          chart.addEventListener('mouseleave', () => {{
              ring.style.boxShadow = 'none';
              chart.style.transform = 'translate(0,0)';
          }});
      }});

      // Slider glow
      document.querySelectorAll('.slider-wrapper').forEach(wrapper => {{
          const ring = wrapper.querySelector('.slider-ring');
          wrapper.addEventListener('mousemove', e => {{
              const rect = wrapper.getBoundingClientRect();
              const mx = e.clientX - rect.left, my = e.clientY - rect.top;
              const cx = rect.width / 2, cy = rect.height / 2;
              const ang = (Math.atan2(my - cy, mx - cx) * 180 / Math.PI + 360) % 360;
              ring.style.setProperty('--angle', ang + 'deg');
              wrapper.style.transform = `translate(${{(mx - cx) / cx * 4}}px, ${{(my - cy) / cy * 4}}px)`;
          }});
          wrapper.addEventListener('mouseenter', () => {{
              ring.style.boxShadow = '0 0 16px 6px rgba(255,165,0,0.6)';
          }});
          wrapper.addEventListener('mouseleave', () => {{
              ring.style.boxShadow = 'none';
              wrapper.style.transform = 'translate(0,0)';
          }});
      }});

      // Chart switching logic
      {chart_scripts}
    </script>
    """

    components.html(full_html, height=600 + 220 * ((len(dataframes) - 1) // 4))


def run_dashboard():
    st.set_page_config(page_title="SulfurAI Dashboard", layout="wide")
    st.markdown("""
        <style>
        /* 🌞 Golden Gradient Title */
        .custom-title {
            font-size: 64px;
            font-weight: 900;
            background: linear-gradient(90deg, #FFA500, #FFD700, #FFA500);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;

            /* ✨ Glowy Outline (gradient untouched) */
            text-shadow:
                0 0 5px rgba(255, 215, 0, 0.7),
                0 0 10px rgba(255, 215, 0, 0.6),
                0 0 20px rgba(255, 165, 0, 0.5),
                0 0 30px rgba(255, 165, 0, 0.4);
            /* optional sharper edge glow */
            -webkit-text-stroke: 1px rgba(255, 215, 0, 0.6);

            animation: glowMove 5s ease-in-out infinite;
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
        }

        /* 🔁 Sunset Shine Animation */
        @keyframes glowMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>

        <!-- ☀️ Title -->
        <div class="custom-title">SulfurAI Dashboard</div>

        <!-- 🌟 Glow Orb -->
        <div id="glow-orb"></div>

        <!-- 🧠 Mouse Tracker -->
        <script>
        document.addEventListener("mousemove", function(e) {
            const orb = document.getElementById("glow-orb");
            orb.style.left = e.pageX + "px";
            orb.style.top = e.pageY + "px";
        });
        </script>
    """, unsafe_allow_html=True)

    # Load first dataset: intents from CSV
    intent_csv_path = "VersionDATA/ai_renderer_2/training_data_sentences/data.csv"
    try:
        intent_df = pd.read_csv(intent_csv_path)
    except Exception as e:
        st.error(f"Failed to load intent CSV data: {e}")
        intent_df = None

    # Load second dataset: try txt first, fallback to CSV
    #location_txt_path = r"VersionDATA\ai_renderer\sentence_location_build\training_data_sentences\data.txt"
    #location_csv_path = r"VersionDATA/ai_renderer/sentence_location_build/training_data_sentences/data.txt"

    #location_df = load_training_data_txt(location_txt_path)
    #if location_df is None:
        #try:
           # location_df = pd.read_csv(location_csv_path)
       # except Exception as e:
            #st.error(f"Failed to load location CSV data: {e}")
            #location_df = None

    sections = {
        "User Insight": {
            "dataframes": [intent_df],
            "graph_names": [
                {
                    "pie": "User Intents Pie",
                    "bar": "User Intents Bar",
                    "line": "User Intents Line"
                },

            ],
        }
    }

    selected = list(sections.keys())[0]

    dataframes = sections[selected]["dataframes"]
    graph_names = sections[selected]["graph_names"]

    render_glowing_section(title=selected, dataframes=dataframes, graph_names=graph_names)
def launch_self():
    port = 8501
    script = Path(__file__).resolve()

    try:
        import psutil
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                psutil.Process(conn.pid).terminate()
    except Exception:
        pass

    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', str(script), f'--server.port={port}'])

    for _ in range(15):
        try:
            import socket
            socket.create_connection(('localhost', port), 1).close()
            break
        except:
            time.sleep(1)

    try:
        import webview
        webview.create_window("SulfurAI Dashboard", f"http://localhost:{port}")
        webview.start()
    except:
        import webbrowser
        webbrowser.open(f"http://localhost:{port}")


# --- Main entry ---
try:
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    if get_script_run_ctx():
        run_dashboard()
    else:
        launch_self()
except:
    launch_self()
