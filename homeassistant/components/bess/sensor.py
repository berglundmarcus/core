"""Platform for sensor integration."""

from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
)

from . import DOMAIN

# entity_id_primarystatus_ActivePower = "tb_bess.Active_Power"
# entity_id_primarystatus_ReactivePower = "tb_bess.Reactive_Power"
# entity_id_primarystatus_PackSoc = "tb_bess.Pack_SoC"
# entity_id_primarystatus_EnergyState = "tb_bess.Energy_State"
# entity_id_primarystatus_ContactorState = "tb_bess.Contactor_State"
# entity_id_primarystatus_PackEnergyIn = "tb_bess.Pack_Energy_In"
# entity_id_primarystatus_PackEnergyOut = "tb_bess.Pack_Energy_Out"
# entity_id_primarystatus_SoxSoH = "tb_bess.Sox_SoH"
# entity_id_primarystatus_SoxSoc = "tb_bess.Sox_Soc"
# entity_id_primarystatus_SoxDod = "tb_bess.Sox_Dod"
# entity_id_primarystatus_contactors = "tb_bess.Contactors_State"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add sensors for passed config_entry in HA."""
    device = hass.data[DOMAIN][config_entry.entry_id]

    new_sensors = []
    new_sensors.append(
        PowerSensor(
            device, "Power Active", f"{device.bms_device_id}_activepower", "ActivePower"
        )
    )
    new_sensors.append(
        PowerSensor(
            device,
            "Power Reactive",
            f"{device.bms_device_id}_reactivepower",
            "ReactivePower",
        )
    )
    new_sensors.append(
        PowerSensor(
            device,
            "Power Apparent",
            f"{device.bms_device_id}_apparantpower",
            "ApparentPower",
        )
    )
    new_sensors.append(
        EnergySensor(
            device,
            "Energy In Total",
            f"{device.bms_device_id}_packenergyin",
            "PackEnergyIn",
        )
    )
    new_sensors.append(
        EnergySensor(
            device,
            "Energy Out Total",
            f"{device.bms_device_id}_packenergyout",
            "PackEnergyOut",
        )
    )
    new_sensors.append(
        EnergySensor(
            device,
            "Capacity Charge",
            f"{device.bms_device_id}_chargecapacity",
            "ChargeCapacity",
        )
    )
    new_sensors.append(
        EnergySensor(
            device,
            "Capacity Discharge",
            f"{device.bms_device_id}_dischargecapacity",
            "DischargeCapacity",
        )
    )
    new_sensors.append(
        EnergySensor(
            device,
            "Capacity Releaseable",
            f"{device.bms_device_id}_releasablecapacity",
            "ReleasableCapacity",
        )
    )
    new_sensors.append(
        SoxSensor(
            device,
            "SoC Pack",
            f"{device.bms_device_id}_packsoc",
            "PackSoC",
        )
    )
    new_sensors.append(
        SoxSensor(
            device,
            "Sox SoC - ECC",
            f"{device.bms_device_id}_soxsoc",
            "SoxSoc",
        )
    )
    new_sensors.append(
        SoxSensor(
            device,
            "Sox SoH - ECC",
            f"{device.bms_device_id}_soxsoh",
            "SoxSoH",
        )
    )
    new_sensors.append(
        SoxSensor(
            device,
            "Sox Dod - ECC",
            f"{device.bms_device_id}_soxdod",
            "SoxDod",
        )
    )
    # new_sensors.append(
    #     SoxSensor(
    #         device,
    #         "Module SoC",
    #         f"{device.bms_device_id}_modulesoc",
    #         "ModuleSoC",
    #     )
    # )
    new_sensors.append(
        PotentialSensor(
            device,
            "Cell Voltage Max",
            f"{device.bms_device_id}_maxcellv",
            "MaxCellV",
        )
    )
    new_sensors.append(
        PotentialSensor(
            device,
            "Cell Voltage Min",
            f"{device.bms_device_id}_mincellv",
            "MinCellV",
        )
    )
    new_sensors.append(
        PotentialSensor(
            device,
            "Voltage AC (AB)",
            f"{device.bms_device_id}_acvoltageab",
            "AcVoltageAB",
        )
    )
    new_sensors.append(
        PotentialSensor(
            device,
            "Voltage AC (AC)",
            f"{device.bms_device_id}_acvoltageac",
            "AcVoltageAC",
        )
    )
    new_sensors.append(
        PotentialSensor(
            device,
            "Voltage AC (CA)",
            f"{device.bms_device_id}_acvoltageca",
            "AcVoltageCA",
        )
    )
    new_sensors.append(
        MultiPotentialSensor(
            device,
            "Cell Voltages",
            f"{device.bms_device_id}_cellvoltages",
            "CellVoltageVector",
        )
    )
    new_sensors.append(
        CurrentSensor(
            device,
            "Inverter Current",
            f"{device.bms_device_id}_invertercurrent",
            "InverterPackCurrent",
        )
    )
    new_sensors.append(
        CurrentSensor(
            device,
            "Current Sensor",
            f"{device.bms_device_id}_packcurrent",
            "PackCurrent",
        )
    )

    new_sensors.append(
        TempSensor(
            device,
            "Cell Temp Max",
            f"{device.bms_device_id}_maxcelltemp",
            "MaxCellTemp",
        )
    )

    new_sensors.append(
        TempSensor(
            device,
            "Cell Temp Min",
            f"{device.bms_device_id}_mincelltemp",
            "MinCellTemp",
        )
    )

    new_sensors.append(
        TempSensor(
            device,
            "Inverter Temp",
            f"{device.bms_device_id}_invertertemp",
            "AmbTemp",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "Number of Cycles",
            f"{device.bms_device_id}_numberofcycles",
            "BatteryCycles",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "Number of Balancing Modules",
            f"{device.bms_device_id}_NumberModulesInBalancing",
            "NumberModulesInBalancing",
        )
    )

    new_sensors.append(
        MultiVectorBinarySensor(
            device,
            "Number of Balancing Cells",
            f"{device.bms_device_id}NumberCellsInBalancing",
            "NumberCellsInBalancing",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "Inverter Status",
            f"{device.bms_device_id}InvStatus",
            "InvStatus",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "Inverter Status PM",
            f"{device.bms_device_id}PmStatus",
            "PmStatus",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "BESS State Contactor",
            f"{device.bms_device_id}ContactorState",
            "ContactorState",
        )
    )

    new_sensors.append(
        NumericSensor(
            device,
            "BESS State Energy",
            f"{device.bms_device_id}EnergyState",
            "EnergyState",
        )
    )

    new_sensors.append(
        EnumContactorSensor(
            device,
            "Contactor Positive Open",
            f"{device.bms_device_id}PosContState",
            "PosContState",
        )
    )

    new_sensors.append(
        EnumContactorSensor(
            device,
            "Contactor Negative Open",
            f"{device.bms_device_id}NegContState",
            "NegContState",
        )
    )

    new_sensors.append(
        EnumContactorSensor(
            device,
            "Contactor Precharge Open",
            f"{device.bms_device_id}PreContState",
            "PreContState",
        )
    )

    # new_sensors.append(
    #     MultiVectorErrors(
    #         device,
    #         "Errors",
    #         f"{device.bms_device_id}Errors",
    #         "errors",
    #     )
    # )

    for sensor in new_sensors:
        device.register_sensors(sensor.get_mqtt_key(), sensor)

    async_add_entities(new_sensors)


class SensorBase(SensorEntity):
    firmware_version = "0.0.1"
    model = "BESS v1.2"
    manufacturer = "TB Teknik AB"
    should_poll = False

    def __init__(self, device, name, mqtt_key) -> None:
        """Initialize the sensor."""
        self._device = device
        self._attr_name = name
        self._mqtt_key = mqtt_key
        self._attr_suggested_display_precision = 2

    @property
    def device_info(self) -> DeviceInfo:
        """Information about this entity/device."""
        return {
            "identifiers": {(DOMAIN, self._device.bms_device_id)},
            # If desired, the name for the device could be different to the entity
            "name": "TB Teknik BESS",
            "sw_version": self.firmware_version,
            "model": self.model,
            "manufacturer": self.manufacturer,
        }

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._value

    @property
    def available(self) -> bool:
        """Return True if roller and hub is available."""
        return True

    def set_new_state(self, new_state) -> None:
        self._value = new_state
        self.async_write_ha_state()

    def get_mqtt_key(self):
        return self._mqtt_key


class PowerSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfPower.KILO_WATT
        self._attr_device_class = SensorDeviceClass.POWER
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class EnumContactorSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._options = list()
        self._value = "True"
        self._attr_device_class = SensorDeviceClass.ENUM
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id

    def set_new_contactor_state(self, str):
        self._value = str

    @property
    def options(self) -> list:
        self._options.append("True")
        self._options.append("False")
        return self._options


class NumericSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_suggested_display_precision = 0

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class EnergySensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
        self._attr_device_class = SensorDeviceClass.ENERGY
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class SoxSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = PERCENTAGE
        self._attr_device_class = SensorDeviceClass.BATTERY
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class TempSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class PotentialSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfElectricPotential.VOLT
        self._attr_device_class = SensorDeviceClass.VOLTAGE
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class CurrentSensor(SensorBase):
    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfElectricCurrent.AMPERE
        self._attr_device_class = SensorDeviceClass.CURRENT
        self._attr_state_class = SensorStateClass.MEASUREMENT

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25


class MultiPotentialSensor(SensorBase):
    should_poll = True

    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_native_unit_of_measurement = UnitOfElectricPotential.VOLT
        self._attr_device_class = SensorDeviceClass.VOLTAGE
        self._attr_state_class = SensorStateClass.TOTAL
        self._attr_extra_state_attributes = True
        print(self._attr_name)

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25
        self._voltage_vector = set()

    def update_voltage_vector(self, voltage_vector) -> None:
        self._voltage_vector = voltage_vector

    @property
    def extra_state_attributes(self) -> dict:
        voltage_vector_dict = dict()
        counter = 0
        for voltage in self._voltage_vector:
            counter = counter + 1
            voltage_vector_dict.update({"Cell " + str(counter): voltage})

        return voltage_vector_dict


class MultiVectorBinarySensor(SensorBase):
    should_poll = True

    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_extra_state_attributes = True

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25
        self._balancing_vector = set()

    def update_balancing_vector(self, balancing_vector) -> None:
        self._balancing_vector = balancing_vector

    @property
    def extra_state_attributes(self) -> dict:
        balancing_vector_dict = dict()
        counter = 0
        for balancing in self._balancing_vector:
            counter = counter + 1
            balancing_vector_dict.update({"Cell " + str(counter): balancing})

        return balancing_vector_dict


class MultiVectorErrors(SensorBase):
    should_poll = True

    def __init__(self, device, name, unique_id, mqtt_key) -> None:
        super().__init__(device, name, mqtt_key)
        self._attr_name = name
        self._attr_extra_state_attributes = True

        # As per the sensor, this must be a unique value within this domain. This is done
        # by using the device ID, and appending "_battery"
        self._attr_unique_id = unique_id
        self._value = 25
        self._error_vector = set()

    def update_error_vector(self, error_vector) -> None:
        self._error_vector = error_vector

    @property
    def extra_state_attributes(self) -> dict:
        error_vector_dict = dict()

        error_vector_dict.update({"LT6811 Mux Error": next(iter(self._error_vector))})
        error_vector_dict.update({"LT6811 Therm Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Over Current Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Over Temp Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Over Volt Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Under Temp Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Under Volt Error": next(iter(self._error_vector))})
        error_vector_dict.update({"Contactor Error": next(iter(self._error_vector))})
        return error_vector_dict
