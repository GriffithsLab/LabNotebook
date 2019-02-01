+++
# Project title.
title = "Computational and theoretical models of brain dynamics"

# Date this page was created.
#date = 2016-04-27T00:00:00
#date = ""

# JG_ADD; c.f. hugo.io conversation
showFooter = false


# Project summary to display on homepage.
#summary = "An example of using the in-built project page."

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["modelling", "theory"]

# Optional external URL for project (replaces project detail page).
#external_link = ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides = "example-slides"
# slides = ""

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
#url_custom = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com/georgecushen"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder. 
[image]
#  # Caption (optional)
  caption = "transition from a clean alpha-frequency limit cycle to a multi-frequency regime with nested gamma oscillations in a thalamocortical mean field model of EEG activity" 
  
#  # Focal point (optional)
#  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "TopLeft"


+++

A main overarching theme of most of the work I do is meso/macroscopic computational models of neural dynamics. I use mathematical models describing neural population activity on the scale of millimetres to centimetres, together with network structure from macaque histology or diffusion MRI fibre tracking, to simulate (approximately) whole-brain activity measurements of the kind measured by fMRI and M/EEG. These techniques are gradually allowing us to obtain more mechanistic insights into observed patterns in neuroimaging data relating to the resting state, oscillations, and the impact of neurological and neurodegenerative disease.

 

Much of my work in this area is based around usage and development of the modelling and neuroinformatics software platform the The Virtual Brain (TVB), the brainchild of my boss Randy McIntosh and colleague Vik Jirsa. As a member of the TVB team I provide technical support on the Forum, and also teach at our regular official (and unofficial) TVB workshops.



<img style="align: right; margin: 15px 15px 15px 15px;" src="/img/tvb_logo.png" width="300" />





In a second complementary line of work, I have been working together with Prof. Peter Robinson at the University of Sydney, on macroscopic neural field models for large-scale brain dynamics. These are generally formulated in terms of second-order partial differential (wave) equations that are substantially simpler to work with analytically than the stochastic delay-differential equation numerically integrated in TVB simulations. In particular, we have studied the role of the spherical topology and physical embedding of the cerebral cortex on anatomical structure and dynamics. This, together with the steady-state eigenmode solutions to the Robinson neural field equations, predicts the presence of spherical harmonic-like patterns in fast-timescale activity measurements. Consistent with this, we have recently shown that this spherical harmonic-like spatial eigenmode structure is observed in cortical surface Laplacians, anatomical connectivity (tractography) networks, (MEG) functional connectivity networks, and numerical simulations (Griffiths et al. 2017; Griffiths et al. submitted; Robinson et al. 2016). These results provide new insight into the role of the network topology and geometric embedding of the cerebral hemispheres in shaping brain dynamics, as well as the theoretical and practical utility of macroscopic neural field models with spherical boundary conditions.


<img style="align: right; margin: 15px 15px 15px 15px;" src="/img/mode_topographies.png" width="700" />


<img style="align: right; margin: 15px 15px 15px 15px;" src="/img/tc_model_diagram.png" width="700" />

<img style="align: right; margin: 15px 15px 15px 15px;" src="/img/tc_model_arnold_tongues.png" width="700" />





