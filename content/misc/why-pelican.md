date: 2014-09-01
author: Erwin Sterrenburg
title: Why Pelican?
slug: why-pelican
tags: PYTHON, BLOG
summary: Short explanation on why this website is created using pelican.

The idea of a personal website and blog had been floating around in my 
head for a long long time. Most of this time, I expected the result
to be powered by [Django](https://www.djangoproject.com/ "Django") /
[Mezzanine](http://mezzanine.jupo.org/ "Mezzanine").
Some weeks ago, I finally got to work and set things into motion. The result 
however was not really satisfying. All functionality was there and 
the looks kept making me happy, yet the approach felt like overkill
for my simple needs.

Some internet research for alternatives opened up
a whole world of static site generators that seemed much 
more appropriate for a site like this. Among these, I've chosen
[Pelican](http://blog.getpelican.com/ "Pelican") for the following reasons:

- it is written in familiar language (python) and uses a familiar template system (jinja2);
- it's extensive collection of themes and plugins;
- the documentation is elaborate and many fellow bloggers have written helpful posts
 on how to use and customize Pelican;
- pelicans are awesome![^staticgenerators]

![awesome pelican](/images/pelican.jpg "Awesome pelican") 
<cite>By [DickDaniels](http://carolinabirds.org/ "DickDaniels") (Own work), [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0 "CC-BY-SA-3.0") or [GFDL](http://www.gnu.org/copyleft/fdl.html "GFDL"), via Wikimedia Commons</cite>

<br>
The only big con of this approach is the need to use a 3rd party service for comments.[^staticcomments]
The most widely used comment hosting service is Disqus, which I implemented here as well since it's
omnipresence suggest they must do something right. After all:
> Fifty million Frenchmen can't be wrong

None-the-less using a service that I have blocked by Ghostery during most of my
browsing time feels somewhat wrong, so this might change in the future.

##Why this theme?
The theme I created for Mezzanine consisted of a dark color scheme
with a dynamically generated fractal background.
After moving to Pelican, I looked at the available themes to see which 
of these would form the best starting point to re-create this look.
However, when I encountered the pure theme, this theme seemed to be 
almost good enough without further modification. 
The only drawback was a severe shortage of bananas, but that was easy
enough to solve. Bananas improve everything.

[^staticgenerators]: Well-chosen names seem to be common among static site generators: 
[Nikola Tesla](http://getnikola.com/) and [Octopuses](http://octopress.org/)
 are awesome as well!
[^staticcomments]: Alternatives do exist like using the
 [Pelican comment system](https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system)
 plugin or hosting your own comment service using
 [Isso](http://posativ.org/isso/), yet would take some of the simplicity of a static site generator approach away.
