import os,glob,nbformat

nbc_str_tpl = 'jupyter nbconvert %s --to markdown --NbConvertApp.output_files_dir=.'



base_dir = os.getcwd()
post_dirs = glob.glob('content/entry/*')
post_dirs_fp = [base_dir + '/' + p for p in post_dirs]

nb_dir = base_dir + '/../notebooks'



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
title = "%s"  # Add a page title.
summary = "Hello!"  # Add a page description.
date = 2019-01-01T00:00:00  # Add today's date.
type = "widget_page"  # Page type is a Widget Page
+++

"""

os.chdir(nb_dir)
nbs = glob.glob('*.ipynb')

entries_dir = base_dir + '/content/entry' 

print('notebooks: %s' %nbs)


for nb_it,nb in enumerate(nbs):

    nb_full = nb_dir + '/' + nb    
    nb_name = nb.replace('.ipynb', '')
    
    F = open(nb_full, 'r')
    thisnb = nbformat.read(F,nbformat.NO_CONVERT)
    nb_md = thisnb['metadata']
    
    if 'grifflab_labnotebook' in nb_md:
        gl_nb_md = nb_md['grifflab_labnotebook']
        post_title = gl_nb_md['post_title']    
        
        new_dir = entries_dir + '/%s' % nb_name
        print('going to new dir: %s' %new_dir)
        if not os.path.isdir(new_dir): os.makedirs(new_dir)
        os.chdir(new_dir)
        print('copying file %s to .' %nb_full)
        os.system('cp %s .'  %nb_full)
        print('running nbconvert for %s' %nb)
        nbc_str = nbc_str_tpl % nb 
        os.system(nbc_str)
    
        md_file = nb_name + '.md'
        md_str = top_lines + open(md_file, 'r').read()
        open(md_file, 'w+').write(md_str)

        index_file = 'index.md'
        open(index_file, 'w+').write(index_txt %post_title)    
  
        os.system('rm %s' %nb)

    else:
        print('%s - skipping; grifflab labnotebook info not in metadata' %nb)

os.chdir(base_dir)

#os.system('cat %s.md %s.md | tee -a index.md')


