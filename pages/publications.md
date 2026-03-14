---
layout: page
title: Publications
permalink: /publications/
years: ["2026", "2025", "2023", "2021", "2018"]
linktoheader: true
---

# {{page.title}}

{% for year in page.years %}

<h3 style="text-align: right; color: #acabab;">{{ year }}</h3>
<hr style="border: 0; border-top: 1px solid #E3E3E3; margin: 4px 0;">

{% for publication in site.data.publications %}
{% if publication.year == year %}
<div class="publication-entry">
    <strong>{{ publication.title }}</strong><br>
    {% assign my_name = "Muralikrishnna G. Sethuraman" %}
    {% if publication.author contains my_name %}
    {{ publication.author | replace: my_name, '<span class="author-me">Muralikrishnna G. Sethuraman</span>' }}<br>
    {% else %}
    {{ publication.author }}<br>
    {% endif %}
    In {% if publication.booktitle %}<i>{{ publication.booktitle }}</i>{% elsif publication.journal %}<i>{{ publication.journal }}</i>{% endif %} ({{ publication.year }})<br>
    {% if publication.pdf %}<a href="{{ publication.pdf }}" class="pub-link">paper</a>{% endif %} {% if publication.supp %}<a href="{{ publication.supp }}" class="pub-link">supp</a>{% endif %} {% if publication.slides %}<a href="{{ publication.slides }}" class="pub-link">slides</a>{% endif %} {% if publication.poster %}<a href="{{ publication.poster }}" class="pub-link">poster</a>{% endif %} {% if publication.code %}<a href="{{ publication.code }}" class="pub-link">code</a>{% endif %} {% if publication.video %}<a href="{{ publication.video }}" class="pub-link">video</a>{% endif %}<br>
</div>
{% endif %}
{% endfor %}

{% endfor %}
