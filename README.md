# Home Assistant IKEA Stock Checker

## Features

- Gets stock on item from selected IKEA store in specific country.
- Makes a sensor that updates every 5 minutes.


## Configuration

| Name    | Type        | Default       |   Description     |
|---------|-------------|---------------|-------------------|
| `product_id`    | string | **Required** | Product ID, see [below](#product-id) how to get this. |
| `store`         | number | **Required** | Store ID, see [below](#store-id) how to get this. |
| `url_locale`    | string | **Required** | no/no for Norway, se/sv for Sweden ect. |
| `friendly_name` | string | **Required** | Friendly name for you sensor, example: name of item. |

Example configuration.yaml:

```yaml
sensor:
  - platform: ikea_sensor
    product_id: 10260281
    store: '095'
    url_locale: no/no
    friendly_name: Skap 100x35
```







### Product ID
Visit https://www.ikea.com/gb/en/ and search for your product. At the end of the URL there is a 8-digit code. This is the Product ID.

Example: 

```https://www.ikea.com/no/no/p/pax-garderobeskapstamme-brunsvart-10260281/```

Where ```10260281``` is my product ID.




### Store ID
Visit https://github.com/Ephigenia/ikea-availability-checker, install it and run ```npx ikea-availability-checker stores no``` where ```no``` is your country code!
This will return something like this:


    ┌─────────────┬─────────┬────────┬────────────────┐
    │ countryCode │ country │ buCode │ name           │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 007    │ Sørlandet      │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 091    │ Slependen      │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 095    │ Furuset        │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 126    │ Forus          │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 371    │ Leangen        │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 390    │ Ringsaker      │
    ├─────────────┼─────────┼────────┼────────────────┤
    │ no          │ Norway  │ 441    | Åsane          |
    └─────────────┴─────────┴────────┴────────────────┘
    
buCode is your Store ID.



