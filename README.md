# Home Assistant Stock Checker

## Features

- Gets stock on item from selected IKEA store in specific country.
- Makes a sensor that updates every 5 minutes.


| Name    | Type        | Default       |   Description     |
|---------|-------------|---------------|-------------------|
| `product_id`    | string | **Required** | test1 |
| `store`         | number | **Required** | test1 |
| `url_locale`    | string | **Required** | test1 |
| `friendly_name` | string | **Required** | test1 |



Example:

```yaml
sensor:
  - platform: ikea_sensor
    product_id: 10260281
    store: '095'
    url_locale: no/no
    friendly_name: Skap 100x35
```


