# grideye-testing

## Test Your Own
0. (optional) Have a play around with the [iOS App!](https://itunes.apple.com/de/app/grid-eye-visualize-temperature/id1110815348) This is truly plug-and-play. Just download from the Apple store, connect via bluetooth and go nuts.

1. Get your Pi [running](https://www.lifehacker.com.au/2016/06/the-always-up-to-date-guide-to-setting-up-your-raspberry-pi/) your preferred OS. I used Raspbian here.
2. Download the [Python Module](https://eu.industrial.panasonic.com/sites/default/pidseu/files/grideye-eval_kit_0-3_0.zip) onto your Pi.
3. Plug in the GridEYE evalkit via the USB port.  
  _If you aren’t using the evaluation kit, no worries! The GridEYE uses the [I2C protocol](https://learn.sparkfun.com/tutorials/i2c), and so can the [Raspberry Pi](https://pinout.xyz/). Follow this [awesome tutorial](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/raspberry-pi-thermal-camera) by [Dean Miller](https://learn.adafruit.com/users/real_dean) over at Adafruit, and you’ll be up and running in no time._
  4. Store your Data. You can simply use our python code to store it as a csv on your Pi.  
  If you plan on running the GridEYE for more than a few days, the Pi won't have enough storage. We recommend storing your data with [AWS](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdk-setup.html)  
    _If you want to run the Pi headless, make sure you setup your data logging software to run on boot. We used a crontab for this test, but there's many ways to do it._
