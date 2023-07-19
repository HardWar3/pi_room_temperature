# www.github.com/adafruit/Adafruit_CircuitPython_DHT

import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        temperature_celsius = dhtDevice.temperature
        temperature_fahrenheit = temperature_celsius * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "\U0001F525 : {:.1f}°C / {:.1f}°F\n\U0001F4A7 : {}% ".format(
                temperature_celsius, temperature_fahrenheit, humidity
            )
        )
        break
    except RuntimeError as error:
        #print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
