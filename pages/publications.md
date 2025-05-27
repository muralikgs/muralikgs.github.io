---
layout: page
title: Publications
permalink: /publications/
years: ["2025", "2024", "2023", "2021", "2018"]
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
    In {% if publication.booktitle %}<i>{{ publication.booktitle }}</i>{% elsif publication.journal %}<i>{{ publication.journal }}</i>{% endif %} ({{ publication.year }})<br>
</span>
{% endif %}
{% endfor %}

{% endfor %}
