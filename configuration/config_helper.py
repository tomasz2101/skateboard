ENVIRONMENT = "development"
I2C_MODULE = True
GPIO_MODULE = True

MOTOR = {
    "status": True,
    "pin": 4
}

LED_STRIP = {
    "status": False,
    "pin_blue": 20,
    "pin_red": 21,
    "pin_green": 22,
    "frequency_hz": 50,
    "max_pwm": 75,
}

LCD_DISPLAY = {
    "status": False,
    "address": 0x27
}

LIGHTS = {
    "status": False,
    "pin_front": 23,
    "pin_back": 24,
}

WII_REMOTE = {
    "status": True,
    "address": "00:24:1E:A8:47:5F"
}

BATTERY_METER = {
    "status": False,
    "reference_voltage": 4.38,
    "max_value": 255,
    "modules": {
        0: {
            "address": 0x44,
            "pins": {
                "s1": 0,
                "s2": 1,
                "s3": 2,
                "s4": 3,
            }
        },
        1: {
            "address": 0x45,
            "pins": {
                "s5": 0,
                "s6": 1,
            }
        },
    },
}