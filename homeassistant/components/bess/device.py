from __future__ import annotations

import asyncio
import json

from homeassistant.core import HomeAssistant


class BmsDevice:
    def __init__(self, config_entry, hass: HomeAssistant, host: str) -> None:
        """Init dummy hub."""
        self._host = host
        self._hass = hass
        self._name = host
        self._id = host.lower()
        self.online = True
        self._sensors = dict()

    def register_sensors(self, key, value) -> None:
        self._sensors.update({key: value})

    @property
    def bms_device_id(self) -> str:
        """ID for dummy hub."""
        return self._id

    async def test_connection(self) -> bool:
        """Test connectivity to the Dummy hub is OK."""
        await asyncio.sleep(1)
        return True

    def parse_incoming_bess_data(self, payload) -> None:
        status_message_dict = json.loads(payload)
        self._sensors["ActivePower"].set_new_state(status_message_dict["ActivePower"])
        self._sensors["ReactivePower"].set_new_state(
            status_message_dict["ReactivePower"]
        )
        self._sensors["ApparentPower"].set_new_state(
            status_message_dict["ApparentPower"]
        )
        self._sensors["PackEnergyIn"].set_new_state(status_message_dict["PackEnergyIn"])
        self._sensors["PackEnergyOut"].set_new_state(
            status_message_dict["PackEnergyOut"]
        )
        self._sensors["ReleasableCapacity"].set_new_state(
            status_message_dict["ReleasableCapacity"]
        )
        self._sensors["ChargeCapacity"].set_new_state(
            status_message_dict["ChargeCapacity"]
        )
        self._sensors["DischargeCapacity"].set_new_state(
            status_message_dict["DischargeCapacity"]
        )
        self._sensors["PackSoC"].set_new_state(status_message_dict["PackSoC"])

        self._sensors["PackSoC"].set_new_state(status_message_dict["PackSoC"])
        self._sensors["SoxSoc"].set_new_state(status_message_dict["SoxSoc"])
        self._sensors["SoxSoH"].set_new_state(status_message_dict["SoxSoH"])
        self._sensors["SoxDod"].set_new_state(status_message_dict["SoxDod"])
        self._sensors["MaxCellV"].set_new_state(status_message_dict["MaxCellV"])
        self._sensors["MinCellV"].set_new_state(status_message_dict["MinCellV"])
        self._sensors["AcVoltageAB"].set_new_state(status_message_dict["AcVoltageAB"])
        self._sensors["AcVoltageAC"].set_new_state(status_message_dict["AcVoltageAC"])
        self._sensors["AcVoltageCA"].set_new_state(status_message_dict["AcVoltageCA"])
        self._sensors["CellVoltageVector"].update_voltage_vector(
            status_message_dict["CellVoltageVector"]
        )

        self._sensors["InverterPackCurrent"].set_new_state(
            status_message_dict["InverterPackCurrent"]
        )
        self._sensors["PackCurrent"].set_new_state(status_message_dict["PackCurrent"])
        self._sensors["InverterPackCurrent"].set_new_state(
            status_message_dict["InverterPackCurrent"]
        )

        self._sensors["MaxCellTemp"].set_new_state(status_message_dict["MaxCellTemp"])
        self._sensors["MinCellTemp"].set_new_state(status_message_dict["MinCellTemp"])
        self._sensors["AmbTemp"].set_new_state(status_message_dict["AmbTemp"])
        self._sensors["BatteryCycles"].set_new_state(
            status_message_dict["BatteryCycles"]
        )
        self._sensors["NumberModulesInBalancing"].set_new_state(
            status_message_dict["NumberModulesInBalancing"]
        )
        self._sensors["NumberCellsInBalancing"].set_new_state(
            status_message_dict["NumberCellsInBalancing"]
        )
        self._sensors["InvStatus"].set_new_state(status_message_dict["InvStatus"])
        self._sensors["PmStatus"].set_new_state(status_message_dict["PmStatus"])

        self._sensors["ContactorState"].set_new_state(
            status_message_dict["ContactorState"]
        )
        self._sensors["EnergyState"].set_new_state(status_message_dict["EnergyState"])

        self._sensors["PosContState"].set_new_contactor_state(
            next(iter(status_message_dict["contactors"]))
        )
        self._sensors["NegContState"].set_new_contactor_state(
            next(iter(status_message_dict["contactors"]))
        )
        self._sensors["PreContState"].set_new_contactor_state(
            next(iter(status_message_dict["contactors"]))
        )
        self._sensors["NumberCellsInBalancing"].update_balancing_vector(
            status_message_dict["BalancingVector"]
        )
        self._sensors["NumberCellsInBalancing"].set_new_state(
            status_message_dict["NumberCellsInBalancing"]
        )
        # self._sensors["errors"].update_error_vector(status_message_dict["errors"])

        # self._sensors["ModuleSoC"].set_new_state(status_message_dict["ModuleSo
        # C"])
