# Python imports
import logging
import requests
import json
import voluptuous as vol
from datetime import timedelta

# More imports for home assistant
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (ATTR_ATTRIBUTION, CONF_FRIENDLY_NAME)
from homeassistant.components.sensor import (PLATFORM_SCHEMA, ENTITY_ID_FORMAT)
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle, slugify

# Variables
ATTRIBUTION = 'Data provided by ikea.com'
USER_AGENT = "Home Assistant IKEA sensor"
CONF_PRODUCT = 'product_id'
CONF_URL_LOCALE = "url_locale"
CONF_STORE = 'store'
# Headers :O
ACCEPT = "application/vnd.ikea.iows+json:version=1.0"
CONSUMER = "MAMMUT"
CONTRACT = "37249"

# Data validation
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_PRODUCT): cv.string,   
    vol.Required(CONF_STORE): cv.string,
    vol.Required(CONF_URL_LOCALE): cv.string,
    vol.Optional(CONF_FRIENDLY_NAME): cv.string
})

# Update timer
TIME_BETWEEN_UPDATES = timedelta(minutes=5)

_LOGGER = logging.getLogger(__name__)

# Setup - Creates enteties
def setup_platform(hass, config, add_entities, discovery_info=None):
    product_id = config.get(CONF_PRODUCT)
    store_id = config.get(CONF_STORE)
    url_locale = config.get(CONF_URL_LOCALE)
    name = 'IKEA - {} {}'.format(store_id, product_id)
    friendly_name = config.get(CONF_FRIENDLY_NAME, name)
    _LOGGER.debug("Setting up the sensor for store %s", store_id)
    sensors = []
    sensors.append(IKEASensor(name, friendly_name, product_id, store_id, url_locale))
    add_entities(sensors)

class IKEASensor(Entity):
    def __init__(self, name, friendly_name, product_id, store_id, url_locale):
        self.entity_id = ENTITY_ID_FORMAT.format(slugify(name))
        self._friendly_name = friendly_name
        self._url = "https://www.ikea.com/retail/iows/{}/stores/{}/availability/ART/{}". \
                   format(url_locale, store_id, product_id)
        self._test2 = None
        self._product_id = product_id
        self._store_id = store_id

    # Sets friendly name
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._friendly_name

    # Sets icon
    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:shopping'

    # Sets state of device, aka stock number
    @property
    def state(self):
        """Return the state of the device."""
        if self._test2:
            return self._test2
        return '-'
    
    # Unit of measurements, i have it as stk in Norwegian
    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return "units"

    # Updates stock every TIME_BETWEEN_UPDATES as above.
    @Throttle(TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data and updates the states."""
        _LOGGER.debug("Update data for %s using %s", self.entity_id, self._url)
        headers = {'Accept': 'application/vnd.ikea.iows+json:version=1.0', 'Contract': '37249', 'Consumer': 'MAMMUT'}
        try:
            req = requests.get(self._url, headers=headers)

        except:
            _LOGGER.error("Failed fetching IKEA availability for product '%s'", 
                self._product_id)
            return

        found = False
        if req.status_code == 200:
            # Seriously dont know how to parse json data, so fuckit
            data = json.loads(req.text)

            test = (data['StockAvailability'])
            test1 = (test['RetailItemAvailability'])
            test2 = (test1['AvailableStock'])
            data1 = json.dumps(test2)
            res = data1.translate({ ord(c): None for c in "{$:}" })
            res1 = res.translate({ ord(c): None for c in '"" ' })
            self._test2 = res1

        else:
                _LOGGER.error("Failed fetching IKEA availability for product '%s', server returned HTTP %d", 
                    self._product_id, req.status_code)
