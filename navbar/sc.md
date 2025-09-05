---
layout: default
title: Scientific Computing
permalink: /navbar/sc/
pagination:
  enabled: true
  collection: posts
  category: sc
  per_page: 20
  title: ':title - page :num'
---

<h2>Scientific Computing Archive</h2>

{% assign current_year = "" %}

<ul>
{% for post in paginator.posts %}
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

<!-- 分页导航 -->
<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path }}" class="prev">Previous page</a>
  {% endif %}

  <span>page {{ paginator.page }}, total {{ paginator.total_pages }}</span>

  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path }}" class="next">Next page</a>
  {% endif %}
</div>
