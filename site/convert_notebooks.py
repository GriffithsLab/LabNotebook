import os,glob

nbc_str_tpl = 'jupyter nbconvert %s --to markdown --NbConvertApp.output_files_dir=.'

base_dir = os.getcwd()
post_dirs = glob.glob('content/entry/*')
post_dirs_fp = [base_dir + '/' + p for p in post_dirs]

top_lines = \
"""

+++
title = ""
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
#headless = true  # This file represents a page section.
headless = false
active = true  # Activate this widget? true/false
weight = 15  # Order that this section will appear.

[design]
# Choose how many columns the section has. Valid values: 1 or 2.
columns = "1"
[design.background]
  image = "grid_powerpoint_blueline.png"
  text_color_light = false
[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]
[advanced]
  # Custom CSS.
  css_style = ""

+++


"""

index_txt = \
"""

+++
title = "Making Word Clouds"  # Add a page title.
summary = "Hello!"  # Add a page description.
date = 2019-01-01T00:00:00  # Add today's date.
type = "widget_page"  # Page type is a Widget Page
+++

"""

for p in post_dirs_fp:

    os.chdir(p)
    ipynb_file = glob.glob('*.ipynb')[0] # assume there is only one nb
    nbc_str = nbc_str_tpl % ipynb_file 
    os.system(nbc_str)
   
    
    md_file = ipynb_file.replace('.ipynb', '.md')
    md_str = top_lines + open(md_file, 'r').read()
    open(md_file, 'w+').write(md_str)

    index_file = 'index.md'
    open(index_file, 'w+').write(index_txt)
    
    
os.chdir(base_dir)

#os.system('cat %s.md %s.md | tee -a index.md')


