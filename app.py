import subprocess
import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).parent

st.set_page_config(page_title="INF100 Labs Runner", page_icon="🎓", layout="centered")
st.title("INF100 Labs Runner 🎓")

st.write("Velg et skript fra lab-mappene og kjør det interaktivt.")

# Discover available lab directories (lab1, lab2, ...)
lab_dirs = sorted([p for p in PROJECT_ROOT.iterdir() if p.is_dir() and p.name.startswith("lab")])

selected_lab = st.selectbox(
    "Velg lab",
    options=[p.name for p in lab_dirs] or ["(ingen lab funnet)"],
)

if selected_lab and selected_lab != "(ingen lab funnet)":
    current_lab_dir = PROJECT_ROOT / selected_lab
    # Discover Python scripts in the selected lab
    scripts = [p for p in current_lab_dir.glob("*.py") if p.name != "__init__.py"]
    script_names = [p.name for p in scripts]

    selected_script = st.selectbox("Velg skript", options=script_names or ["(ingen skript funnet)"])

    if selected_script and selected_script != "(ingen skript funnet)":
        script_path = current_lab_dir / selected_script
        st.subheader(f"Kjører: {selected_lab}/{selected_script}")

        # Helper to execute a python file in a subprocess and capture stdout/stderr
        def run_script_and_capture(path: Path) -> str:
            result = subprocess.run(
                [sys.executable, path.name],
                cwd=str(path.parent),
                capture_output=True,
                text=True,
                shell=False,
                check=False,
            )
            stdout_text = result.stdout
            if result.stderr:
                stdout_text += ("\n" if stdout_text else "") + result.stderr
            return stdout_text

        # Special handling for known scripts with file inputs (e.g., joker.py uses joker.json)
        if selected_script == "joker.py":
            json_path = current_lab_dir / "joker.json"
            if json_path.exists():
                with open(json_path, "r", encoding="utf-8") as f:
                    content = f.read()
                st.caption("Innhold i joker.json:")
                st.code(content, language="json")
                if st.button("Kjør Joker"):
                    with st.spinner("Kjører joker.py ..."):
                        output = run_script_and_capture(script_path)
                    st.text_area("Utdata", value=output, height=180)
            else:
                st.warning("Filen joker.json ble ikke funnet i samme mappe.")
        else:
            # Generic runner: execute the selected script as a module in-process
            if st.button("Kjør skript"):
                with st.spinner(f"Kjører {selected_script} ..."):
                    output = run_script_and_capture(script_path)
                st.text_area("Utdata", value=output, height=180)

st.caption("Tips: Legg nye skript i lab-mappene (lab1, lab2, ...) så dukker de opp her.")
