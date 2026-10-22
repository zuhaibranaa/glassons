# glassons

A Scrapy crawler for **glassons.com** — the clothing catalogue. It pages through the clothing
category and extracts each product, with a dedicated helper for the product type taxonomy.

## Stack

- Python, Scrapy
- Item pipelines and middlewares under `glassons/`

## Layout

```
scrapy.cfg
glassons/
  items.py
  middlewares.py
  pipelines.py
  settings.py
  spiders/
    glassons.py        the catalogue spider
    product_type_id.py helper that resolves product-type identifiers
```

## Running it

```bash
pip install scrapy
scrapy crawl glassons
```

## Note

`product_type_id.py` maps the site's category labels onto stable identifiers so downstream
records stay consistent when the catalogue is re-crawled.
