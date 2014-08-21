date: 2014-01-01
author: Erwin Sterrenburg
title: This is a sample post
slug: sample-post-for-pelican-powered-blog
tags: blog, sample
sidebarimage: http://www.cheffen.nl/rode%20aardbei.png
summary: This is a test post powered by [Pelican].

todo:

-   about page
-   eerste blogpost
-   deploy workflow (fabric?)?
-   gebruikte foto?
-   favicon
-	description ([http://www.voidynullness.net/blog/2013/05/25/html-meta-description-in-pelican-blog-posts/])

	1.	hdf
	2.	fjd
	>2
		jdfkj

>	[This] is a test post powered by [Pelican].
>	`slug` refers to the final filename of the post. For example this post is "sample-post-for-peldddican-powered-blog.md" so Pelican will generate a file named "sample-post-for-pelican-powered-blog.html" which is what will appear in the address bar of your browser. Note that this can be different that the title of the post. The point of this attribute is to have a consistent name for the page that will *never* change even if the title/content changes.

>	`tags` are comma seperated list of metadata describing your posts. They're optional but if you add them to your posts the Pelican will automatically generate pages listing your posts by tag. For example you could have all your 'foobar' organized together.

`summary` refers to the text summary that will appear on the front page of your blog.

And here is how you add a image:

<img width="200" height="200" src="http://pilosa.eu/images/smiley.png" alt="Smiley" title="What you feel like when blogging with Pelican" />

![Alt Text](|filename|/images/smiley.png)

[Pelican]: http://getpelican.com/
[This]: http://jdlfjfl.com
Inline

LaTex between \$..\$, for example, $x^2$, will be rendered inline with respect to the current html block.
Displayed Math

LaTex between \$$..\$$, for example, $$x^2$$, will be rendered centered in a new paragraph.

$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$

$$\left [ - \frac{\hbar^2}{2 m} \frac{\partial^2}{\partial x^2} + V \right ] \Psi
= i \hbar \frac{\partial}{\partial t} \Psi$$

$
\\begin{array}{ccc}x&S(n,x)&x^n
\\log\\left(\\frac{x}{x-1}\\right)\\\\
-5&-1780484.04&-1780483.95\\\\
-3&-16987.42&-16987.34\\\\
2&709.598&709.783\\\\
4&301656.39&301656.52\\\\
6&1.102428722 \\times 10^7&1.102428734 \\times
10^7
\\end{array}
$


*[ATP]: adenosine triphosphate
*[PDCB]: paradichlorobenzene

The molecule ATP provides energy to molecular motors. PDCB is a
common ingredient in mothballs.
