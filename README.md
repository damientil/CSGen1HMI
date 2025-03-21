# CSGen1HMI

## Connect to Wifi Beagle hotspot
* Wifi host : BeaglePlay-xxx
* Password : BeaglePlay or Beagle board

## Connect thru SSH

```
l-dtil@CRE2-L05426:~$ ssh debian@192.168.8.1
```

* Password : temppwd

## Discover I2C

```
debian@BeaglePlay:~$ i2cdetect -l
i2c-3	i2c       	OMAP I2C adapter                	I2C adapter
i2c-1	i2c       	OMAP I2C adapter                	I2C adapter
i2c-2	i2c       	OMAP I2C adapter                	I2C adapter
i2c-0	i2c       	OMAP I2C adapter                	I2C adapter
i2c-5	i2c       	OMAP I2C adapter                	I2C adapter
```

I2C-5 is the QWIIC connection


# Commands

## Read register - general

```
debian@BeaglePlay:~$ i2cget -y 3 0x50 REG_ID wp
```
Replace REG_ID with the register id from the table below.

## Registers list

https://github.com/damientil/CSGen1HMI/edit/main/README.md#hmi_reg_irq-register


| REG_ID | Register                                | Purpose     | Description | Tested |
|:------:|-----------------------------------------|:-----------:|-------------|:------:|
| 0x00   | HMI_REG_VERSION_NUM                     | common      |  | nok :red_circle:
| 0x01   | HMI_REG_VERSION_SRING                   | common      |  | nok :red_circle:
| 0x02   | [HMI_REG_IRQ](#hmi_reg_irq-register)    | common      | Notify master which interrupt occured | ok
| 0x03   | HMI_REG_IER                             | common      | Interupt enable register | ok
| 0x04   | HMI_REG_CPUID                           | common      |  | nok :red_circle:
| 0x05   | HMI_REG_NFC_LEN                         | common      |  | ok
| 0x06   | HMI_REG_NFC_UID                         | common      |  | nok :red_circle:
| 0x07   | HMI_REG_CHARGE_STATE_MAIN               | indication  |  | ok
| 0x08   | HMI_REG_CHARGE_STATE_DYN                | indication  |  | ok
| 0x09   | HMI_REG_CHARGE_STATE_ERROR              | indication  |  | nok :red_circle:
| 0x0A   | HMI_REG_CHARGE_STATE_FLAGS              | indication  |  | ok
| 0x0B   | HMI_REG_TEMPERATURE                     | common      | Board temperature in °C | ok
| 0x0C   | HMI_REG_PWM                             | common      | Led brightness | ok
| 0x22   | HMI_REG_HEARTBEAT                       | common      |  | ok
| 0x23   | HMI_REG_DEBUG_NFC_UID_LEN               | debug       |  | nok :red_circle:
| 0x24   | HMI_REG_DEBUG_NFC_UID                   | debug       |  | ok
| 0x35   | HMI_REG_CAPACITIVE_TOUCH_BUTTON_DELAY   | common      |  | ok
| 0x36   | HMI_REG_CAPACITIVE_FORCED_CHARGE_DELAY  | common      |  | ok
| 0x37   | HMI_REG_STATUS_HMI_RFID_ENABLED         | common      |  | ok
| 0x38   | HMI_REG_HEARTBEAT_LOST_FREQUENCY        | common      |  | ok


## HMI_REG_IRQ register

### Read register
```
debian@BeaglePlay:~$ i2cget -y 3 0x50 0x02 wp
0x0021
```
### Returned value

0x0000 means no IRQ happen

| Bit | Mask | Description             |
| :-: | :--: | ----------------------- |
| 0   | 0x01 | RFID interrupt occured  |
| 0   | 0x10 | Force charge interrupt occured  |
| 5   | 0x20 | Touch interrupt occured |


### Clear register
To clear IRQ register, write 0xFF.
Read back register. 0x0000 value is expected

```
debian@BeaglePlay:~$ i2cset -y 3 0x50 0x02 0xFFFF wp
debian@BeaglePlay:~$ i2cget -y 3 0x50 0x02 wp
0x0000

```
Selective clear can also be performed using bitmask instead of 0xFFFF value.

## PWM
| Duty cycle | Hexa value |
|:---:|:---:|
| 1   | 0x000A   |
| 2   | 0x0014  |
| 5   | 0x0032  |
| 10  | 0x0064  |
| 20  | 0x00C8  |
| 30  | 0x012C |
| 40  | 0x0190 |
| 50  | 0x01F4 |
| 60  | 0x0258 |
| 70  | 0x02BC |
| 80  | 0x0320 |
| 90  | 0x0384 |
| 100 | 0x03E8 |
