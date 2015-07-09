#!/usr/bin/python

"""
 ================================================
 ABElectronics IO Pi 32-Channel Port Expander
 Version 1.0 Created 30/04/2014
 Version 1.1 bug fixes
 Version 1.2 changes to format source code to PEP8 rules 12/11/2014

Requires python 2 smbus to be installed with: sudo apt-get install python-smbus
================================================


Each MCP23017 chip is split into two 8-bit ports.  port 0 controls
pins 1 to 8 while port 1 controls pins 9 to 16.
When writing to or reading from a port the least significant bit represents
the lowest numbered pin on the selected port.
"""


class IoPi(object):
    # Define registers values from datasheet
    IODIRA = 0x00  # IO direction A - 1= input 0 = output
    IODIRB = 0x01  # IO direction B - 1= input 0 = output
    # Input polarity A - If a bit is set, the corresponding GPIO register bit
    # will reflect the inverted value on the pin.
    IPOLA = 0x02
    # Input polarity B - If a bit is set, the corresponding GPIO register bit
    # will reflect the inverted value on the pin.
    IPOLB = 0x03
    # The GPINTEN register controls the interrupt-onchange feature for each
    # pin on port A.
    GPINTENA = 0x04
    # The GPINTEN register controls the interrupt-onchange feature for each
    # pin on port B.
    GPINTENB = 0x05
    # Default value for port A - These bits set the compare value for pins
    # configured for interrupt-on-change. If the associated pin level is the
    # opposite from the register bit, an interrupt occurs.
    DEFVALA = 0x06
    # Default value for port B - These bits set the compare value for pins
    # configured for interrupt-on-change. If the associated pin level is the
    # opposite from the register bit, an interrupt occurs.
    DEFVALB = 0x07
    # Interrupt control register for port A.  If 1 interrupt is fired when the
    # pin matches the default value, if 0 the interrupt is fired on state
    # change
    INTCONA = 0x08
    # Interrupt control register for port B.  If 1 interrupt is fired when the
    # pin matches the default value, if 0 the interrupt is fired on state
    # change
    INTCONB = 0x09
    IOCON = 0x0A  # see datasheet for configuration register
    GPPUA = 0x0C  # pull-up resistors for port A
    GPPUB = 0x0D  # pull-up resistors for port B
    # The INTF register reflects the interrupt condition on the port A pins of
    # any pin that is enabled for interrupts. A set bit indicates that the
    # associated pin caused the interrupt.
    INTFA = 0x0E
    # The INTF register reflects the interrupt condition on the port B pins of
    # any pin that is enabled for interrupts. A set bit indicates that the
    # associated pin caused the interrupt.
    INTFB = 0x0F
    # The INTCAP register captures the GPIO port A value at the time the
    # interrupt occurred.
    INTCAPA = 0x10
    # The INTCAP register captures the GPIO port B value at the time the
    # interrupt occurred.
    INTCAPB = 0x11
    GPIOA = 0x12  # data port A
    GPIOB = 0x13  # data port B
    OLATA = 0x14  # output latches A
    OLATB = 0x15  # output latches B

    # variables
    address = 0x20  # I2C address
    port_a_dir = 0x00  # port a direction
    port_b_dir = 0x00  # port b direction
    portaval = 0x00  # port a value
    portbval = 0x00  # port b value
    porta_pullup = 0x00  # port a pull-up resistors
    portb_pullup = 0x00  # port a pull-up resistors
    porta_polarity = 0x00  # input polarity for port a
    portb_polarity = 0x00  # input polarity for port b
    intA = 0x00  # interrupt control for port a
    intB = 0x00  # interrupt control for port a
    # initial configuration - see IOCON page in the MCP23017 datasheet for
    # more information.
    config = 0x22
    global _bus

    def __init__(self, bus, address=0x20):
        """
        init object with smbus object, i2c address, default is 0x20, 0x21 for
        IOPi board,
        Load default configuration, all pins are inputs with pull-ups disabled
        """
        return

    # local methods

    def __updatebyte(self, byte, bit, value):
        """
        internal method for setting the value of a single bit within a byte
        """
        if value == 0:
            return byte & ~(1 << bit)
        elif value == 1:
            return byte | (1 << bit)

    def __checkbit(self, byte, bit):
        """
         internal method for reading the value of a single bit within a byte
        """
        if byte & (1 << bit):
            return 1
        else:
            return 0

    # public methods

    def set_pin_direction(self, pin, direction):
        return

    def set_port_direction(self, port, direction):
        return

    def set_pin_pullup(self, pinval, value):
        return

    def set_port_pullups(self, port, value):
        return

    def write_pin(self, pin, value):
        return

    def write_port(self, port, value):
        return

    def read_pin(self, pinval):
        return 1

    def read_port(self, port):
	if ( port == 0 ) :
        	return 0b00100100
	else :
		return 0b11010010

    def invert_port(self, port, polarity):
        return

    def invert_pin(self, pin, polarity):
        return

    def mirror_interrupts(self, value):
        return

    def set_interrupt_polarity(self, value):
        return

    def set_interrupt_type(self, port, value):
        return

    def set_interrupt_defaults(self, port, value):
        return

    def set_interrupt_on_port(self, port, value):
        return

    def set_interrupt_on_pin(self, pin, value):
        return

    def read_interrupt_status(self, port):
        return 1

    def read_interrupt_capture(self, port):
        return 1

    def reset_interrupts(self):
        return
