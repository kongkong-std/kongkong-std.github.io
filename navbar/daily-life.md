---
layout: page
title: Daily Life
permalink: navbar/daily-life/
---

<h2>Daily Life Archive</h2>

{% assign posts = site.categories.daily-life | sort: "date" | reverse %}
{% assign current_year = "" %}

<ul>
{% for post in posts %}
  {% assign post_year = post.date | date: "%Y" %}
  {% if post_year != current_year %}
    {% unless forloop.first %}</ul>{% endunless %}
    <h3>{{ post_year }}</h3>
    <ul>
    {% assign current_year = post_year %}
  {% endif %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="text-muted">({{ post.date | date: "%m-%d" }})</span>
  </li>
{% endfor %}
</ul>
