################ Welcome to SulfurAI dashboard!
### Functions here should be modified with proper intent.
### This python script was written in the Holly format. To find out how it works go into VersionDATA/HollyFormat/ReadMe.txt
### This python script is designed to host all SulfurAI API functions for python and run via the __main__ tag.

### LAYOUT:
# ---------------GOING DOWN!
#####-TOS reminder
#####-Imports call_file_path (important dependency)
#####-Ensures required packages are installed
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
        "⚠️ This application is external to SulfurAI and is maintained by different sources. Therefore project works may be different.",
        "--------------------------------------------------------------------------------------------------",
        "By using this application you agree to the Terms of Service listed in the project files.",
        "If you do not consent, stop using our services.",
        "If you cannot find it, install a new version OR look in the root folder for 'Terms of Service.txt'.",
        "--------------------------------------------------------------------------------------------------",
        "",
        "                                       🔃 Loading... 🔃                                                    ",
        "                           App powered by the SulfurAI Sulfax UI engine.                                                             ",
        "",
        "--------------------------------------------------------------------------------------------------",
        "⚠️ App freezing? Restart the app and wait. Cacheing may take a while.",
        "--------------------------------------------------------------------------------------------------",

    ]
    print_verti_list(TOS)


# DELETING THE TOS NOTICE SCRIPT RESULTS IN INSTANT TERMINATION OF SULFUR WARRANTY AND CANCELS YOUR CONTRACT. IT IS *IN VIOLATION* OF THE TOS.
# YOU MAY BE INDEFINITELY BANNED FROM SULFUR SERVICES IF YOU REMOVE THIS TOS NOTICE SCRIPT WITHOUT PRIOR WRITTEN CONSENT BY VOLKSHUB GROUP.

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





# Ensure required packages
modules = ["streamlit", "dash", "pandas", "plotly","pywebview"]
for mod in modules:
    try:  __import__(mod)
    except ImportError:
        file_path_cache_localHost_pip_debug = call.cache_LocalpipCacheDebug()
        with open(file_path_cache_localHost_pip_debug, "r", encoding="utf-8", errors="ignore") as file:  cache_stored_pip_debug = file.readlines()
        if mod not in [line.strip() for line in cache_stored_pip_debug]: print(f"The dependancies for SulfurAI Dashboard are not installed. Please install them using the installer in INSTALLER/INSTALL SULFURAI-DASHBOARD/Run Installer.bat")




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from streamlit.runtime.scriptrunner import get_script_run_ctx
from pathlib import Path
import webbrowser
import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

all_sections_html = ""


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




#---------------------------paths---------------------------


css_path = os.path.join("SulfurDashboardAssets\styling", "style.css")
with open(css_path, "r") as f:
    css = f.read()

js_path = os.path.join("SulfurDashboardAssets\styling", "script.js")
with open(js_path, "r") as f:
    js = f.read()





def render_glowing_section(title, dataframes, graph_names, section_id="section-container", custom_style=""):
    import pandas as pd
    import plotly.express as px

    inner_charts_html = []
    chart_ids = []

    for idx, df in enumerate(dataframes):
        if df is None or df.empty:
            continue
        try:
            pos = graph_names[idx]["positions"][idx]
            left = pos.get("left", "0px")
            top = pos.get("top", "0px")
        except:
           left, top = "0px", "0px"

        is_device_data = graph_names[idx].get("type") == "device"

        if is_device_data:
            def map_device_type(row):
                val = str(row.iloc[-1]).strip()
                if val == "2":
                    return "mobile"
                elif val == "1":
                    return "desktop"
                else:
                    return None

            df['device_type'] = df.apply(map_device_type, axis=1)
            df = df[df['device_type'].notna()]
            col = 'device_type'
        else:
            if 'intent' in df.columns:
                col = 'intent'
            elif 'location' in df.columns:
                col = 'location'
            else:
                col = df.columns[0]

        intent_counts = df[col].value_counts(normalize=True) * 100

        pie_fig = px.pie(names=intent_counts.index, values=intent_counts.values,
                         title=graph_names[idx]["pie"], template="plotly_dark")
        bar_fig = px.bar(x=intent_counts.index, y=intent_counts.values,
                         title=graph_names[idx]["bar"], labels={"x": col.capitalize(), "y": "%"},
                         template="plotly_dark")
        line_fig = px.line(x=intent_counts.index, y=intent_counts.values,
                           title=graph_names[idx]["line"], labels={"x": col.capitalize(), "y": "%"},
                           template="plotly_dark")

        for fig in (pie_fig, bar_fig, line_fig):
            fig.update_layout(width=200, height=200, margin=dict(l=5, r=5, t=25, b=5))

        chart_id = f"{title.lower().replace(' ', '')}-{idx}"
        chart_ids.append(chart_id)

        pie_html = pie_fig.to_html(include_plotlyjs=False, full_html=False)
        bar_html = bar_fig.to_html(include_plotlyjs=False, full_html=False)
        line_html = line_fig.to_html(include_plotlyjs=False, full_html=False)

        slider_default_value = 1 if is_device_data else 0

        try:
            pos = graph_names[idx]["positions"][idx]
            left = pos.get("left", "0px")
            top = pos.get("top", "0px")
        except (KeyError, IndexError):
            left, top = "0px", "0px"

        chart_html = f"""
         <div class="glowing-chart"
              id="chart-{chart_id}"
              style="position:absolute;
                     left:{left};
                     top:{top};
                     background-color:#111;">
           <div class="chart-ring"></div>
           <div class="slider-wrapper">
               <div class="slider-ring"></div>
               <input id="slider-{chart_id}"
                      type="range"
                      min="0" max="2"
                      value="{slider_default_value}"
                      style="width:100%; margin-bottom:5px;">
          </div>
           <div id="pie-{chart_id}"
                style="display:{'none' if slider_default_value == 1 else 'block'}">
             {pie_html}
           </div>
           <div id="bar-{chart_id}"
                style="display:{'block' if slider_default_value == 1 else 'none'}">
             {bar_html}
           </div>
           <div id="line-{chart_id}" style="display:none">
             {line_html}
           </div>
         </div>
        """
        inner_charts_html.append(chart_html)

    chart_scripts = """
        <script>
        document.addEventListener('DOMContentLoaded', function() {
        """

    for cid in chart_ids:
        chart_scripts += f"""
            document.getElementById('slider-{cid}').addEventListener('input', function(e) {{
                const value = e.target.value;
                document.getElementById('pie-{cid}').style.display = value === '0' ? 'block' : 'none';
                document.getElementById('bar-{cid}').style.display = value === '1' ? 'block' : 'none';
                document.getElementById('line-{cid}').style.display = value === '2' ? 'block' : 'none';
            }});
            """

    chart_scripts += """
        });
        </script>
        """

    section_html = f"""
                <div class="glowing-section" id="{section_id}" style="{custom_style}">
                    <div class="section-ring" id="ring-{section_id}"></div>
                    <div class="glowing-section-title">{title}</div>
                    <div class="charts-container">
                        {"".join(inner_charts_html)}
                    </div>
                    {chart_scripts}
                </div>
                """

    return section_html



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
    user_devices = r"DATA\ai_renderer\training_data\data_train_sk\data.txt"
    try:
        intent_df = pd.read_csv(intent_csv_path)
    except Exception as e:
        st.error(f"Failed to load intent CSV data: {e}")
        print(f"Failed to load intent CSV data: {e}")
        intent_df = None

    from io import StringIO

    try:
        expected_commas = 2
        clean_lines = []

        with open(user_devices, "r", encoding="utf-8") as f:
            header = f.readline().strip()
            clean_lines.append(header)
            for line in f:
                if line.count(",") == expected_commas:
                    clean_lines.append(line.strip())
                else:
                    # Skip lines with unexpected number of commas
                    pass

        clean_data = "\n".join(clean_lines)
        devices = pd.read_csv(StringIO(clean_data), sep=",")
    except Exception as e:
        st.error(f"Failed to load user CSV data: {e}")
        print(f"Failed to load user CSV data: {e}")
        devices = None

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
                    "line": "User Intents Line",
                    "type": "insight",

                    "positions": [
                        {"left": "40%", "top": "150px"}, #right + bottom
                        {"left": "0%", "top": "0px"}, #left + top
                ]
                },
            ],
            "position": {
                "left": "5%",    # CSS percentage or pixel value
                "top": "20px",   # CSS pixel value
                "width": "45%"   # CSS percentage or pixel value
            }
        },

        "User Average Devices": {
            "dataframes": [devices],
            "graph_names": [
                {
                    "bar": "User Devices Bar",
                    "pie": "User Devices Pie",
                    "line": "User Devices Line",
                    "type": "device",

                    "positions": [
                    {"left": "40%", "top": "150px"}, #right + bottom
                    {"left": "0%", "top": "0px"}, #left + top
                ]
                },
            ],
            "position": {
                "left": "52%",
                "top": "20px",
                "width": "45%"
            }
        },
    }

    all_sections_html = ""
    for section_title, section_config in sections.items():
        dataframes = section_config["dataframes"]
        graph_names = section_config["graph_names"]
        position = section_config["position"]

        custom_style = f"""
            position: absolute;
            top: {position['top']};
            left: {position['left']};
            width: {position['width']};
        """

        section_id = section_title.lower().replace(" ", "-") + "-section"

        section_html = render_glowing_section(
            title=section_title,
            dataframes=dataframes,
            graph_names=graph_names,
            section_id=section_id,
            custom_style=custom_style
        )

        all_sections_html += section_html

    final_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            {css}
        </style>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <div id="section-container" class="glowing-dashboard-container">
            {all_sections_html}
        </div>
        <script>{js}</script>
    </body>
    </html>
    """



    import threading
    from http.server import HTTPServer, SimpleHTTPRequestHandler

    file_path = call.EXTERNALAPP_dashboard_renderer()  # This returns path to your HTML file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)



    # Step 2: Start a simple HTTP server in the directory of the HTML file
    directory = os.path.dirname(file_path)
    os.chdir(directory)

    # Serve on localhost:8000 or any free port
    PORT = 8000

    def start_server():
        httpd = HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)
        httpd.serve_forever()

    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Step 3: Build URL to the dashboard HTML file
    dashboard_url = f"http://localhost:{PORT}/{os.path.basename(file_path)}"

    # Step 4: Embed with iframe pointing to HTTP URL (works better than local file path)
    components.iframe(dashboard_url, height=1000, scrolling=True)


def launch_self():

    port = 8502
    script = Path(__file__).resolve()

    # Kill any existing process on that port
    try:
        import psutil
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr.port == port and conn.status == psutil.CONN_LISTEN:
                psutil.Process(conn.pid).terminate()
    except Exception:
        pass

    # Set up and launch Streamlit
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    subprocess.Popen([
        sys.executable, '-m', 'streamlit', 'run', str(script), f'--server.port={port}'
    ])

    # Wait for Streamlit to start
    for _ in range(30):
        try:
            import socket
            socket.create_connection(('localhost', port), 1).close()
            break
        except:
            time.sleep(0.2)

    # Try to open in PyWebView, fallback to browser
    try:
        import webview
        webview.create_window("SulfurAI Dashboard", f"http://localhost:{port}")
        webview.start()
    except:
        import webbrowser
        webbrowser.open(f"http://localhost:{port}")


# --- Main entrypoint ---
if __name__ == "__main__":
    try:
        ctx = get_script_run_ctx()
        if ctx:
            # ✅ Inside Streamlit — only run dashboard once
            if "dashboard_ran" not in st.session_state:
                st.session_state.dashboard_ran = True
                run_dashboard()
        else:
            # 🚀 Not inside Streamlit — relaunch self
            launch_self()
    except:
        # 🛡️ Fallback if anything goes wrong
        launch_self()
