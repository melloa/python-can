"""
Interfaces contain low level implementations that interact with CAN hardware.
"""

# interface_name => (module, classname)
BACKENDS = {
    "kvaser": ("can.interfaces.kvaser", "KvaserBus"),
    "socketcan": ("can.interfaces.socketcan", "SocketcanBus"),
    "serial": ("can.interfaces.serial.serial_can", "SerialBus"),
    "pcan": ("can.interfaces.pcan", "PcanBus"),
    "usb2can": ("can.interfaces.usb2can", "Usb2canBus"),
    "ixxat": ("can.interfaces.ixxat", "IXXATBus"),
    "nican": ("can.interfaces.nican", "NicanBus"),
    "iscan": ("can.interfaces.iscan", "IscanBus"),
    "virtual": ("can.interfaces.virtual", "VirtualBus"),
    "udp_multicast": ("can.interfaces.udp_multicast", "UdpMulticastBus"),
    "neovi": ("can.interfaces.ics_neovi", "NeoViBus"),
    "vector": ("can.interfaces.vector", "VectorBus"),
    "slcan": ("can.interfaces.slcan", "slcanBus"),
    "robotell": ("can.interfaces.robotell", "robotellBus"),
    "canalystii": ("can.interfaces.canalystii", "CANalystIIBus"),
    "systec": ("can.interfaces.systec", "UcanBus"),
    "seeedstudio": ("can.interfaces.seeedstudio", "SeeedBus"),
    "cantact": ("can.interfaces.cantact", "CantactBus"),
    "gs_usb": ("can.interfaces.gs_usb", "GsUsbBus"),
    "nixnet": ("can.interfaces.nixnet", "NiXNETcanBus"),
    "neousys": ("can.interfaces.neousys", "NeousysBus"),
}

try:
    from importlib.metadata import entry_points

    entry = entry_points()
    if "can.interface" in entry:
        BACKENDS.update(
            {
                interface.name: tuple(interface.value.split(":"))
                for interface in entry["can.interface"]
            }
        )
except ImportError:
    from pkg_resources import iter_entry_points

    entry = iter_entry_points("can.interface")
    BACKENDS.update(
        {
            interface.name: (interface.module_name, interface.attrs[0])
            for interface in entry
        }
    )

VALID_INTERFACES = frozenset(list(BACKENDS.keys()))
