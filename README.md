# Intro to Python

Dieses Projekt enthält eine Reihe von Jupyter-Notebooks für den Einstieg in Python (`*.ipynb`)

Dieses Projekt enthält eine Konfiguration für einen DevContainer zur Nutzung in einem GitHub CodeSpace bzw. für die lokale Entwicklung in Docker + VS Code.


## Verwendete Werkzeuge

1. **[pyenv]()** (Management der Python-Version, .python-version): 
2. **[poetry]()** (Management von Abhängigkeiten: `pyproject.toml`, `poetry.lock`. Verzeichnis `.venv`)
3. **[Development Containers](https://containers.dev/)** (Konsistente Entwicklungsumgebungen in der Cloud via [CodeSpaces](https://github.com/features/codespaces) oder lokal mit [Docker](https://www.docker.com/products/docker-desktop/)) `.devcontainer`, [`.devcontainer/devcontainer.json`](./.devcontainer/devcontainer.json), [`.devcontainer/Dockerfile`](./.devcontainer/Dockerfile) 
4. **[VS Code](https://code.visualstudio.com/)** mit der Remote Development Extension installiert. 

## Abhängigkeiten

siehe `.python-version`, `pyproject.toml`, `poetry.lock`

## Verwendung

### Voraussetzungen


1. [VS Code](https://code.visualstudio.com/) mit der [Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) installiert + [Docker](https://www.docker.com/products/docker-desktop/)-Installation oder [CodeSpaces](https://github.com/features/codespaces)

Im Dev Container bereits installiert:

2. [Python 3.12](https://www.python.org/) 
3. [Poetry](https://python-poetry.org/docs/)