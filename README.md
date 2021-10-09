# Home Assistant Stock Checker
Home Assistant sensor that checks Ikea stock on one or multiple items.


| Name    | Type        | **Required**  |   Description     |
|---------|-------------|---------------|-------------------|
| `product_id`    | 
| `store`         |
| `url_locale`    |
| `friendly_name` |








Example:

```yaml
sensor:
  - platform: ikea_sensor
    product_id: 10260281
    store: '095'
    url_locale: no/no
    friendly_name: Skap 100x35
```


