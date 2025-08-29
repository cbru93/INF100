import subprocess
import sys
from pathlib import Path
from datetime import datetime
import os
import tempfile
import shutil

import streamlit as st
import re
import ast

PROJECT_ROOT = Path(__file__).parent

st.set_page_config(page_title="INF100 Labs Runner",
                   page_icon="🎓", layout="centered")
st.title("INF100 Labs Runner 🎓")

st.write("Velg et skript fra lab-mappene og kjør det interaktivt.")

# Discover available lab directories (lab1, lab2, ...)
lab_dirs = sorted([p for p in PROJECT_ROOT.iterdir()
                  if p.is_dir() and p.name.startswith("lab")])

selected_lab = st.selectbox(
    "Velg lab",
    options=[p.name for p in lab_dirs] or ["(ingen lab funnet)"],
)

if selected_lab and selected_lab != "(ingen lab funnet)":
    current_lab_dir = PROJECT_ROOT / selected_lab
    # Discover Python scripts in the selected lab
    scripts = [p for p in current_lab_dir.glob(
        "*.py") if p.name != "__init__.py"]
    script_names = [p.name for p in scripts]

    selected_script = st.selectbox("Velg skript", options=script_names or [
                                   "(ingen skript funnet)"])

    if selected_script and selected_script != "(ingen skript funnet)":
        script_path = current_lab_dir / selected_script
        st.subheader(f"Kjører: {selected_lab}/{selected_script}")

        # Helper to execute a python file in a subprocess and capture stdout/stderr
        def run_script_and_capture(path: Path, stdin_text: str = "") -> str:
            result = subprocess.run(
                [sys.executable, path.name],
                cwd=str(path.parent),
                capture_output=True,
                text=True,
                input=stdin_text,
                shell=False,
                check=False,
            )
            stdout_text = result.stdout
            if result.stderr:
                stdout_text += ("\n" if stdout_text else "") + result.stderr
            return _filter_known_warnings(stdout_text)

        def run_script_with_graphics_capture(path: Path, stdin_text: str = "") -> tuple[str, bytes | None]:
            """Run script under a virtual display and capture graphics as bytes.

            Returns (output_text, image_bytes_or_None).
            """
            lab_dir = path.parent

            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            base_name = path.stem
            tmp_dir = tempfile.mkdtemp(prefix="inf100-canvas-")
            out_path = Path(tmp_dir) / f"{base_name}-canvas-{timestamp}.gif"

            # Environment for uib_inf100_graphics to save frames
            env = os.environ.copy()
            env["ENVPRIORITY"] = "1"
            env["FILETOSAVE"] = str(out_path)
            # Optional: make frames shorter to speed up GIF playback
            env["STDDURATION"] = "0.1"

            # Run with xvfb-run to provide a virtual X display for Tk
            cmd = [
                "xvfb-run",
                "-a",
                sys.executable,
                path.name,
            ]
            result = subprocess.run(
                cmd,
                cwd=str(lab_dir),
                env=env,
                capture_output=True,
                text=True,
                input=stdin_text,
                shell=False,
                check=False,
            )
            stdout_text = result.stdout
            if result.stderr:
                stdout_text += ("\n" if stdout_text else "") + result.stderr

            if out_path.exists():
                try:
                    data = out_path.read_bytes()
                finally:
                    shutil.rmtree(tmp_dir, ignore_errors=True)
                return _filter_known_warnings(stdout_text), data
            shutil.rmtree(tmp_dir, ignore_errors=True)
            return _filter_known_warnings(stdout_text), None

        def _filter_known_warnings(text: str) -> str:
            # Remove noisy pyscreenshot warning emitted by uib_inf100_graphics
            try:
                pattern = (
                    r"\*{50,}\n\*\* Cannot import pyscreenshot[\s\S]*?runtime error\.\n\*{50,}\n\n")
                text = re.sub(pattern, "", text)
            except Exception:
                pass
            return text

        # Dynamic input field generation from input() prompts
        def _extract_input_prompts(path: Path) -> list[str]:
            try:
                source = path.read_text(encoding="utf-8")
                tree = ast.parse(source)
                prompts: list[str] = []
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "input":
                        if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                            prompts.append(str(node.args[0].value))
                return prompts
            except Exception:
                return []

        prompts = _extract_input_prompts(script_path)
        if prompts:
            st.caption("Input (fra scriptets input()-kall)")
            input_values: list[str] = []
            for idx, prompt in enumerate(prompts):
                label = prompt if len(prompt) <= 80 else prompt[:77] + "…"
                input_values.append(st.text_input(
                    label, key=f"stdin_{selected_lab}_{selected_script}_{idx}"))
            stdin_text = "\n".join(input_values)
            st.caption(
                "Tips: Hvis et input()-kall forventer flere verdier i én linje, skill dem med mellomrom (f.eks. '2 3').")
        else:
            # Fallback: generic stdin textbox
            stdin_text = st.text_area("Standard input (valgfritt)", height=80,
                                      placeholder="Skriv eventuell input her, slik den ville blitt tastet i terminalen…")

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
                        output = run_script_and_capture(
                            script_path, stdin_text)
                    st.text_area("Utdata", value=output, height=180)
            else:
                st.warning("Filen joker.json ble ikke funnet i samme mappe.")
        else:
            # Single button: run with graphics capture and display image if any
            if st.button("Kjør skript"):
                with st.spinner(f"Kjører {selected_script} ..."):
                    output, image_bytes = run_script_with_graphics_capture(
                        script_path, stdin_text)
                st.text_area("Utdata", value=output, height=180)
                if image_bytes is not None:
                    st.caption("Viser generert grafikk (ikke lagret på disk)")
                    st.image(image_bytes)

st.caption(
    "Tips: Legg nye skript i lab-mappene (lab1, lab2, ...) så dukker de opp her.")
