# Home Assistant IKEA Stock Checker

## Features

- Gets stock on item from selected IKEA store in specific country.
- Makes a sensor that updates every 5 minutes.


## Configuration

| Name    | Type        | Default       |   Description     |
|---------|-------------|---------------|-------------------|
| `product_id`    | string | **Required** | Product ID, see below how to get this. |
| `store`         | number | **Required** | Store ID, see below how to get this. |
| `url_locale`    | string | **Required** | no/no for Norway, se/sv for Sweden ect. |
| `friendly_name` | string | **Required** | Friendly name for you sensor, example: name of item. |




### Product ID
Visit www.ikea.no to get the product ID.


### Store ID
Visit www.ikea.no to get the product ID.





Example:

```yaml
sensor:
  - platform: ikea_sensor
    product_id: 10260281
    store: '095'
    url_locale: no/no
    friendly_name: Skap 100x35
```


