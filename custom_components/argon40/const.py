"""Constants for Argon40."""
# Base component constants
NAME = "Argon40"
DOMAIN = "argon40"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTR_NAME = "speed"
SERVICE_SET_FAN_SPEED = "set_fan_speed"

ISSUE_URL = "https://github.com/Misiu/argon40/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""