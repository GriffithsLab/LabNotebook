# LabNotebook

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/GriffithsLab/LabNotebook/master)





## Notebook format

Pages are build from jupyter notebooks in the `notebooks` folder. 

Not all notebooks in that folder have associated pages on the site, 
for example if they are RISE slideshows not intended to be read as a linear 
webpage, or if they have nbconvert-incompatible contents. 

Those notebooks that don't have associated pages can still be viewed via binder,
or locally. 

The decision as to whether a page is built from a notebook or not is based on the notebook metadata. 

Specifically, the line in `convert_notebooks.py`:


```python
  if 'grifflab_labnotebook' in nb_md:
        gl_nb_md = nb_md['grifflab_labnotebook']
        post_title = gl_nb_md['post_title'] 
```

...so notebooks without a 'grifflab_labnotebook' key/value entry in the notebook metadata dict will 
not produce web pages, and the title of the page is derived from the 'post_title' key/value in the 
'grifflab_labnotebook' sub-dictionary. 






## Local dev  


The LabNotebook website is configured via netlify's CI functionality to automatically re-generate upon every commit. 

Currently it runs just a single linux bash command, which calls a simple python function (`convert_notebooks.py`) and the hugo binary. 

The command is defined in `netlify.toml. 

To reproduce the CI behaviour locally for testing purposes, I use something like the following commands:


```bash

# Make sure hugo binary is on path so 'hugo' bash command runs
export PATH=$PATH:~/Software/hugo  

# Make sure python is on the path; needs to have the correct libraries
# (i.e. reasonably up to date nbformat+nbconvert)
source ~/Software/miniconda3/bin/activate  jupyter_py3  

# Run the one-liner in netlify.toml
rm -rf site/public && cd site && python convert_notebooks.py && hugo  

# Spin up a local hugo server to see how it's looking. 
# This needs to be run from the 'site' folder
# (which is where you end up after the previous command)
hugo server -t hugo-academic --disableFastRender  

```



