# ...compound...


```bash
conda env create -f environment.yml
conda activate compound

(* jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib jupyterlab_bokeh *)
jupyter labextension install @pyviz/jupyterlab_pyviz
# Install latest altair to get geo features
# https://github.com/altair-viz/altair/pull/1664
pip install git+https://github.com/altair-viz/altair.git#b98ab5b6ec9b2fac3d0b2cc13cd31c0f0970fc5a

jupyter lab
```