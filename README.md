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


| Address | Register                                | Purpose     | Tested |
|---------|-----------------------------------------|-------------|--------|
| 0x00    | HMI_REG_VERSION_NUM                     | common      | nok
| 0x01    | HMI_REG_VERSION_SRING                   | common      | nok
| 0x02    | [HMI_REG_IRQ](#test)                             | common      | ok
| 0x03    | HMI_REG_IER                             | common      | ok
| 0x04    | HMI_REG_CPUID                           | common      | nok
| 0x05    | HMI_REG_NFC_LEN                         | common      | ok
| 0x06    | HMI_REG_NFC_UID                         | common      | nok
| 0x07    | HMI_REG_CHARGE_STATE_MAIN               | indication  | ok
| 0x08    | HMI_REG_CHARGE_STATE_DYN                | indication  | ok
| 0x09    | HMI_REG_CHARGE_STATE_ERROR              | indication  | nok
| 0x0A    | HMI_REG_CHARGE_STATE_FLAGS              | indication  | ok
| 0x0B    | HMI_REG_TEMPERATURE                     | common      | ok
| 0x0C    | HMI_REG_PWM                             | common      | ok
| 0x22    | HMI_REG_HEARTBEAT                       | common      | ok
| 0x23    | HMI_REG_DEBUG_NFC_UID_LEN               | debug       | nok
| 0x24    | HMI_REG_DEBUG_NFC_UID                   | debug       | ok
| 0x35    | HMI_REG_CAPACITIVE_TOUCH_BUTTON_DELAY   | common      | ok
| 0x36    | HMI_REG_CAPACITIVE_FORCED_CHARGE_DELAY  | common      | ok
| 0x37    | HMI_REG_STATUS_HMI_RFID_ENABLED         | common      | ok
| 0x38    | HMI_REG_HEARTBEAT_LOST_FREQUENCY        | common      | ok


## test

### Read register
```
debian@BeaglePlay:~$ i2cget -y 3 0x50 0x02 wp
0x0021
```
0x0000 means no IRQ happen

| Bit | Mask | Description             |
| --- | ---- | ----------------------- |
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
