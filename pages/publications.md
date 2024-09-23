---
layout: page
title: Publications
permalink: /publications/
years: ["2024", "2023", "2021", "2018"]
linktoheader: true
---

# {{page.title}}

{% for year in page.years %}

<h3>{{ year }}</h3>
<hr>

{% for publication in site.data.publications %}
{% if publication.year == year %}
<span>
    <strong> {{ publication.title }}</strong><br>
    {{ publication.author }},<br> 
    In <i>{{ publication.booktitle }}</i>  ({{ publication.year }})<br> 
</span>
{% endif %}
{% endfor %}

{% endfor %}
