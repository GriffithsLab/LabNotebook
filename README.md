# LabNotebook

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/GriffithsLab/LabNotebook/master)


[View on nbviewer](https://nbviewer.jupyter.org/github/GriffithsLab/LabNotebook/tree/master/notebooks/)





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
#export PATH=$PATH:~/Software/hugo  
export PATH=$PATH:~/Software/hugo_extended_0.59.0


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


## Latex usage

A few apparently necessary tweaks for using latex within markdown in hugo. 


### Page frontmatter

Need to insert the following lines in the page source

```
math = true
markup = "mmark"
```

In this repo the frontmatter for each page is being generated auatomatically (in a small, separate `index.md` file) after running nbconvert on the notebooks. So that has now been added to `convert_notebooks.py.`



### Latex source

The hugo academic page provides various equation examples 

https://academic-demo.netlify.com/post/writing-technical-content/


It appears however that not all latex that renders in e.g. jupyter notebook / markdown works in the sites currently being generated. 


I'm not exactly sure at this point what the differences are from my typical latex use cases and the examples from the above page that do equivalent things and do work. 

That would be useful to know. 

In the meantime, following observations from hugo forums, I've found two tweaks are sufficient to get equations rendering pretty much exactly the same in jupyter notebooks (which pages in this repo are generated from) and the hugo webpages:


1. Use double dollar sign (`$$`) enclosures, including for arrays (e.g. `$$\begin{array}...` rather than `\begin{array}` )

2. Insert spaces before and after underscores used for subscripts (i.e. replace e.g. `a_{ij}` with `a _ {ij}`. This appears to make no change to the rendered equations. 


I also have read that multi-line equations need to replace double backslash escape '\\' with six backslahes '\\\\\\'. Haven't confirmed that that is necessary yet. 



Good example page for this: 'tvb_neural_fields_and_power_spectra' post. 



