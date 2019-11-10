# ...compound...


```bash
conda env create -f environment.yml
conda activate compound

jupyter labextension install @pyviz/jupyterlab_pyviz

jupyter lab
```

## Deploy

```bash
heroku container:login
 
heroku create
heroku container:push web
heroku container:release web
```