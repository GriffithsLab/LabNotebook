+++
# Project title.
title = "Modelling brain stimulation"

# Date this page was created.
#date = 2016-04-27T00:00:00

# Project summary to display on homepage.
# summary = "An example of using the in-built project page."

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["modelling", "stimulation", "tms"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references 
#   `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides = "example-slides"

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{icon_pack = "fab", icon="twitter", name="Follow", url = "https://twitter.com/georgecushen"}]

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder. 
[image]
  preview_only = true
  # Caption (optional)
  # caption = "Photo by rawpixel on Unsplash"
  
  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"


+++

Brain stimulation is both a fundamental tool for studying basic principles of neuronal function, and an increasingly used therapeutic technique in clinical neurology and neuropsychiatry. Our work on computational models of neurostimulation spans both of these domains, with particular focus on oscillatory network dynamics and transcranial magnetic stimulation (TMS) therapy for major depressive disorder. 

<img src="/img/tc_model_arnold_tongues.png" align="right" margin="15px 15px 15px 15px" width="300" />

Our recent work on this has explored brain stimulation in the thalamocortical system. Driving this system with periodic electric stimulation produces Arnold Tongues and resonance effects that depend on both the noise and the time delay structure of the underlying neural system, as well as its current state - which (like the EEG) shows endogeneous fluctuations between regimes of synchronous alpha activity and periods of relatively more asynchronous high-frequency activity.


Key questions for future work: 

1. *Plasticity*: How to oscillatory changes due to TMS obtain from the treatment, continuing to have long-term efficacious effects weeks or months down the line. 
2. *Propagation*: How does stimulation at one site propagate to distal brain regions? How can we make use of anatomical and functional brain connectivity information, combined with neurophysiological models, to map out the network effects of focal noninvasive stimulation?










