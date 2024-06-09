"""The TB Tech BESS integration."""

from __future__ import annotations

from homeassistant.components import mqtt
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import device
from .const import DOMAIN

# TODO List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up TB Tech BESS from a config entry."""

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = device.BmsDevice(
        entry, hass, entry.data["host"]
    )
    _bms_device = hass.data[DOMAIN][entry.entry_id]

    # Listen to a message on MQTT.
    @callback
    def message_received(args: ReceiveMessage) -> None:
        """A new MQTT message has been received."""
        topic = getattr(args, "topic")
        payload = getattr(args, "payload")
        qos = getattr(args, "qos")
        _bms_device.parse_incoming_bess_data(payload)

    # TODO 1. Create API instance
    # TODO 2. Validate the API connection (and authentication)
    # TODO 3. Store an API object for your platforms to access
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    topic = "energy/storage/tbtechbess/primarystatus"
    await hass.components.mqtt.async_subscribe(topic, message_received)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
