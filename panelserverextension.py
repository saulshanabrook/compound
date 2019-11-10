

from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the clifford.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "Untitled.ipynb", "--allow-websocket-origin=*"])
