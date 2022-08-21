---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Electronic Information Engineering, The Chinese University of Hong Kong, Shenzhen, 2020
* Ph.D. in Data Science, The Chinese University of Hong Kong, Shenzhen, 2020 - Present

Skills
======
* Programming Languages: Python, MATLAB, C/C++, Julia, R
* Development Environments: PyTorch, TensorFlow, Pandas, Linux
* Languages: English, Fluent. Chinese, Mother Tongue

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  

