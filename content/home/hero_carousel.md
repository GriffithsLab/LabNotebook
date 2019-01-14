+++
# Hero Carousel widget.
widget = "hero_carousel"
active = true
#active = false
date = 2017-10-15T00:00:00

# Order that this section will appear in.
weight = 1

# Slide interval.
# Use `false` to disable animation or enter a time in ms, e.g. `5000` (5s).
#interval = false
interval = 5000
#interval = true

# Minimum slide height.
# Specify a height to ensure a consistent height for each slide.
height = "500px"

# Slides.
# Duplicate an `[[item]]` block to add more slides.
[[item]]
  title = "Whole Brain Modelling Group"
  #content = "I am center aligned :smile:"
  content = "Krembil Centre for Neuroinformatics @ CAMH "
  align = "center"  # Choose `center`, `left`, or `right`.

  # Overlay a color or image (optional).
  #   Deactivate an option by commenting out the line, prefixing it with `#`.
  overlay_color = "#666"  # An HTML color value.
  overlay_img = "ViewFromTorontoWestern.jpg"
  #overlay_img = "headers/bubbles-wide.jpg"  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.
 
  # Call to action button (optional).
  #   Activate the button by specifying a URL and button label below.
  #   Deactivate by commenting out parameters, prefixing lines with `#`.
  #cta_label = "Get Academic"
  #cta_url = "https://sourcethemes.com/academic/"
  #cta_icon_pack = "fas"
  #cta_icon = "graduation-cap"

[[item]]
  
  #title = "Left"
  #content = "I am left aligned :smile:"
  #align = "left"

  title = "Whole Brain Modelling Group"
  #content = "I am center aligned :smile:"
  content = "Krembil Centre for Neuroinformatics"
  align = "center"  # Choose `center`, `left`, or `right`.

  # Overlay a color or image (optional).
  overlay_color = "#555"  # An HTML color value.
  #overlay_img = ""  # Image path relative to your `static/img/` folder.
  overlay_img = "sim9a1_tsmovie.gif"
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

[[item]]
  title = "Right"
  content = "I am right aligned :smile:"
  align = "right"

  overlay_color = "#333"  # An HTML color value.
  overlay_img = ""  # Image path relative to your `static/img/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.
  
  content = "div <iframe src='https://www.camh.ca/en/science-and-research/institutes-and-centres/krembil-centre-for-neuroinformatics/research-pillars-and-values'></iframe>"

+++
