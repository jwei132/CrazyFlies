# Setting up Crazy Flie PA

## Installing CrazyRadio Drivers

[Getting started](https://www.bitcraze.io/products/crazyradio-2-0/#tab-id-usage)

This link directs to a page with instructions on how to install the relevant drivers for the CrazyRadioPA.

Once the drivers are set, you can move on to the next step.

### Windows

If you are using windows and using WSL, you need to attach the CrazyRadio to the WSL lightweight VM. Follow the instructions [here](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)

The main idea is to attach the USB devices to the WSL ports so the WSL can access the devices. 

## Installing the python client

I would first recomend installing [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-fil) first.

## Checking Config of a CrazyFlie

https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client/#firmware-configuration

For checking what the URI of the CrazyFlie is.

Connect the flie with usb to the computer. In a virtual python environment, install cflib and cfclient

```python
pip install cflib cfclient
```

To determine the configuration of the Flie, start the crazyflie GUI with cfclient in the virtual environment. Press the scan button to scan the available USB ports, then press connect to connect to the flie.

Once connected, navigate to connection/configure 2.x and you should see the crazyflie's radio configuration.

The format for the URI is

```python
radio://<radio_dongle_id>/<channel>/<datarate>/<address>
```

## Set up for Linux

https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/installation/usb_permissions/
