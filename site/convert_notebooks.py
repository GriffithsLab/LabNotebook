import os,glob,nbformat

nbc_md_str_tpl = 'jupyter nbconvert %s --to markdown --NbConvertApp.output_files_dir=.'

nbc_sl_str_tpl = 'jupyter nbconvert %s --to slides --NbConvertApp.output_files_dir=.'




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

post_index_txt = \
"""

+++
title = "%s"  # Add a page title.
summary = "Hello!"  # Add a page description.
date = 2019-01-01T00:00:00  # Add today's date.
type = "widget_page"  # Page type is a Widget Page
math = true
diagram = true
markup = "mmark"
+++

"""


talk_index_txt = \
"""
---
title: "%s" # Add talk title 
event: Academic Theme Conference
event_url: https://example.org

location: Source Themes HQ
address:
  street: 450 Serra Mall
  city: Stanford
  region: CA
  postcode: '94305'
  country: United States

summary: An example talk using Academic's Markdown slides feature.
abstract: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellusac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2030-06-01T13:00:00Z"
date_end: "2030-06-01T15:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2017-01-01T00:00:00Z"

authors: []
tags: []

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/georgecushen
url_code: ""
url_pdf: ""
url_slides: "slides/%s"
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: example
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- internal-project

# Enable math on this page?
math: true
---

"""





os.chdir(nb_dir)
nbs = glob.glob('*.ipynb')

entries_dir = base_dir + '/content/entry' 

talks_dir = base_dir + '/content/talk'
slides_dir = base_dir + '/content/slides'


print('\n\nnotebooks: %s\n\n\n' %nbs)


for nb_it,nb in enumerate(nbs):

    nb_full = nb_dir + '/' + nb    
    nb_name = nb.replace('.ipynb', '')
    
    F = open(nb_full, 'r')
    thisnb = nbformat.read(F,nbformat.NO_CONVERT)
    nb_md = thisnb['metadata']
    
    if 'grifflab_labnotebook' in nb_md:
        gl_nb_md = nb_md['grifflab_labnotebook']
        if 'post_title' in gl_nb_md:
            post_title = gl_nb_md['post_title']    
        
            new_dir = entries_dir + '/%s' % nb_name
            print('\n\ngoing to new dir: %s' %new_dir)
            if not os.path.isdir(new_dir): os.makedirs(new_dir)
            os.chdir(new_dir)
            print('\n\ncopying file %s to .' %nb_full)
            os.system('cp %s .'  %nb_full)
            print('\n\nrunning nbconvert for %s' %nb)
            nbc_str = nbc_md_str_tpl % nb 
            os.system(nbc_str)
    
            md_file = nb_name + '.md'
            md_str = top_lines + open(md_file, 'r').read()
            open(md_file, 'w+').write(md_str)

            index_file = 'index.md'
            open(index_file, 'w+').write(post_index_txt %post_title)    
  
            os.system('rm %s' %nb)


        elif 'talk_title' in gl_nb_md:
            talk_title = gl_nb_md['talk_title']
        
            new_talk_dir = talks_dir + '/%s' % nb_name
            print('\n\ngoing to new talk dir: %s' %new_talk_dir)
            if not os.path.isdir(new_talk_dir): os.makedirs(new_talk_dir)
            os.chdir(new_talk_dir)
            #print('\n\ncopying file %s to .' %nb_full)
            #os.system('cp %s .'  %nb_full)
            #print('\n\nrunning nbconvert for %s' %nb)
            #nbct_str = nbct_str_tpl % nb
            #os.system(nbct_str)
    
            #html_file = nb_name + '.slides.html'
            #html_str = top_lines + open(html_file, 'r').read()
            #open(html_file, 'w+').write(html_str)

            index_file = 'index.md'
            open(index_file, 'w+').write(talk_index_txt %(talk_title,nb_name))
  
            #os.system('rm %s' %nb)
 

            new_slides_dir = slides_dir + '/%s' % nb_name
            print('\n\ngoing to new slides dir: %s' %new_slides_dir)
            if not os.path.isdir(new_slides_dir): os.makedirs(new_slides_dir)
            os.chdir(new_slides_dir)
            print('\n\ncopying file %s to .' %nb_full)
            os.system('cp %s .'  %nb_full)
            print('\n\nrunning nbconvert for %s' %nb)
            nbc_str = nbc_sl_str_tpl % nb
            os.system(nbc_str)
             
            os.system('mv %s.slides.html index.html' %nb_name)
            #html_file = nb_name + '.slides.html'
            #html_file = 'index.html'
            #html_str = top_lines + open(html_file, 'r').read()
            #open(html_file, 'w+').write(html_str)

            #index_file = 'index.md'
            #open(index_file, 'w+').write(index_txt %post_title)

            os.system('rm %s' %nb)


 
    else:
        print('\n\n%s - skipping; grifflab labnotebook info not in metadata' %nb)

os.chdir(base_dir)

#os.system('cat %s.md %s.md | tee -a index.md')


