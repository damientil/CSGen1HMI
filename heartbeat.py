import time
from datetime import datetime
import smbus

# Init I2C bus
I2C_BUS = 2                # Use I2C2 (MIKROBUS) 
DEVICE_ADDRESS = 0x50      # Adresse I2C de la carte fille
HEARTBEAT_REGISTER = 0x00  # Registre du heartbeat
HEARTBEAT_SIGNAL = 0x01    # Signal heartbeat

# Affichage des informations de configuration
print("=" * 40)
print("Configuration du script Heartbeat")
print(" - Bus : /dev/i2c-{I2C_BUS}")
print(" - Adress : 0x{DEVICE_ADDRESS:02X}")
print(" - Register : 0x{HEARTBEAT_REGISTER:02X}")
print(" - Heartbeat value : 0x{HEARTBEAT_SIGNAL:02X}")
print("=" * 40)
print("\n\n")

# Initialisation du bus I2C
bus = smbus.SMBus(I2C_BUS)
print("I2C init\n")

print("Start sending heartbeat...\n")

while True:
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S:%f")

    try:
        # Envoi du heartbeat via I2C
        bus.write_byte_data(DEVICE_ADDRESS, HEARTBEAT_REGISTER, HEARTBEAT_SIGNAL)
    except Exception as e:
        print(f"?~Z| ?~O Erreur I2C : {e}") 

    time.sleep(0.5)

