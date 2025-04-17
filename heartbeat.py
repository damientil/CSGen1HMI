import smbus

# I2C configuration
I2C_BUS = 3  # MIKROBUS connector on BeaglePlay (updated to 3)
DEVICE_ADD = 0x50  # HMI I2C address (updated to DEVICE_ADD)

# HMI Registers (based on provided documentation)
HMI_REG_VERSION_NUM = 0x00
HMI_REG_VERSION_SRING = 0x01
HMI_REG_IRQ = 0x02
HMI_REG_IER = 0x03
HMI_REG_CPUID = 0x04
HMI_REG_NFC_LEN = 0x05
HMI_REG_NFC_UID = 0x06
HMI_REG_CHARGE_STATE_MAIN = 0x07
HMI_REG_CHARGE_STATE_DYN = 0x08
HMI_REG_CHARGE_STATE_FLAGS = 0x0A
HMI_REG_TEMPERATURE = 0x0B
HMI_REG_PWM = 0x0C
HMI_REG_HEARTBEAT = 0x22
HMI_REG_DEBUG_NFC_UID_LEN = 0x23
HMI_REG_DEBUG_NFC_UID = 0x24
HMI_REG_TEMP_THRESHOLD = 0x33
HMI_REG_CAPACITIVE_TOUCH_BUTTON_DELAY = 0x35
HMI_REG_CAPACITIVE_FORCED_CHARGE_DELAY = 0x36
HMI_REG_STATUS_HMI_RFID_ENABLED = 0x37
HMI_REG_HEARTBEAT_LOST_FREQUENCY = 0x38

# Affichage des informations de configuration
print("=" * 40)
print("Configuration du script Heartbeat")
print(f" - Bus : /dev/i2c-{I2C_BUS}")
print(f" - Adress : 0x{DEVICE_ADD:02X}")
print("=" * 40)
print("\n\n")

# Initialisation du bus I2C
bus = smbus.SMBus(I2C_BUS)
print("I2C init\n")

print("Sending 1st heartbeat\n")
bus.write_byte(DEVICE_ADD, HMI_REG_HEARTBEAT)

version = bus.read_i2c_block_data(DEVICE_ADD, HMI_REG_VERSION_NUM, 4)
print("Read sw version: ", version)

print("Set low brightness")
bus.write_word_data(DEVICE_ADD, HMI_REG_PWM, 0x000C)

print("Set Available status (0x10)")
bus.write_byte_data(DEVICE_ADD, HMI_REG_CHARGE_STATE_MAIN, 0x10) 

print("Start periodic heartbeat ...")

while True:
    try:
        # Envoi du heartbeat via I2C
        bus.write_byte(DEVICE_ADD, HMI_REG_HEARTBEAT)
    except Exception as e:
        print(f"?~Z| ?~O Erreur I2C : {e}") 

    time.sleep(0.5)
