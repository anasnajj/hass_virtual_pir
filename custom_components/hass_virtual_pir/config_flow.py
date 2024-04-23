import voluptuous as vol
from homeassistant import config_entries

class VirtualPIRFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        # Implementation for adding/configuring devices via GUI
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str
            })
        )
