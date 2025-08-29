# INF100 Labs Runner

A lightweight way to run INF100 lab scripts interactively using Streamlit.

## Prerequisites
- Python 3.10+ — [python.org downloads](https://www.python.org/downloads/)
- PowerShell 7 (recommended on Windows) — [Install PowerShell 7](https://learn.microsoft.com/powershell/scripting/install/installing-powershell)

## Dev Container (VS Code / Cursor)
- Requires Docker (or Podman), and the Dev Containers feature in your editor.
- Open this folder and choose “Reopen in Container”.
- The container build will automatically:
  - create `.venv` and install from `requirements.txt` (see `.devcontainer/devcontainer.json`).
  - auto-activate the virtual environment in new terminals.

Run the app inside the container:
```bash
streamlit run app.py
```

Managing packages inside the container:
```bash
# install new deps
pip install <package>

# capture all installed versions
python -m pip freeze > requirements.txt
```

## Open in GitHub Codespaces
Launch in the cloud (Codespaces) or locally (Dev Containers):

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://codespaces.new/cbru93/INF100)
[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/cbru93/INF100)

Both use `.devcontainer/devcontainer.json` to provision Python and install `requirements.txt` automatically.

## Setup
```bash
# From repo root
python -m venv .venv
. .venv/Scripts/Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
```

## Run the app
```bash
streamlit run app.py
```
Then open the URL shown in the terminal (usually http://localhost:8501) to select and run scripts from `lab1`, `lab2`, ...

## Adding scripts
- Put your Python files in the appropriate `labX` folder (e.g., `lab2/joker.py`).
- If a script needs data files (e.g., `joker.json`), place them in the same folder as the script.

## Publishing to GitHub
1. Create a new GitHub repository (private or public).
2. Initialize and push:
```bash
git init
git add .
git commit -m "Initial INF100 labs runner"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Optional: Deploy Streamlit Cloud
- Create a repo on GitHub with this project.
- Go to https://streamlit.io/cloud and deploy the repo.
- Set the entry point to `app.py`.
- Add any required secrets in `.streamlit/secrets.toml` (excluded by `.gitignore`).

## Notes
- The app attempts to run scripts in-process; avoid using `input()` prompts. Prefer functions and printing output.
- For scripts that exit via `sys.exit`, the app catches `SystemExit` to keep the UI responsive.
