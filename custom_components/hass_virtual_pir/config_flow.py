import voluptuous as vol
from homeassistant import config_entries
from subprocess import run, PIPE

DOMAIN = "hass_virtual_pir"

class VirtualPIRFlowHandler(config_entries.ConfigFlow):

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Validate the entered IP address
            ip_address = user_input.get("ip_address")
            if not ip_address:
                errors["base"] = "Please enter an IP address."
            elif not await self.hass.async_add_executor_job(self._ping_ip, ip_address):
                errors["base"] = "Failed to ping the specified IP address. Please enter a valid IP."
            else:
                return self.async_create_entry(title="Virtual PIR Configuration", data=user_input)

        # Show form to enter IP address
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ip_address"): str
            }),
            errors=errors
        )

    def _ping_ip(self, ip_address):
        """Ping the specified IP address."""
        result = run(["ping", "-c", "1", "-W", "1", ip_address], stdout=PIPE, stderr=PIPE)
        return result.returncode == 0
