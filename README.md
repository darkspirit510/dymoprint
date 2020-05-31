[![Build Status](https://travis-ci.org/computerlyrik/dymoprint.svg?branch=master)](https://travis-ci.org/computerlyrik/dymoprint)

dymoprint
=========

Linux Software to print with LabelManager PnP from Dymo


cloned for development from https://sbronner.com/dymoprint.html

## Features

* Works on python 3.3 to 3.8
* Supports text printing
* Supports qr code printing
* Supports barcode printing
* Supports image printing
* Supports combined barcode / qrcode and text printing

## Installation & Configuration
### Dependent packages

```
pip install -r requirements.txt
```
or in userspace
```
pip install --user -r requirements.txt
```

#### For ubuntu based distributions:
(should also work for debian, but not tested yet)
use **udev** and **modeswitch** configurations to work with the LabelManager PNP.
**modeswitch** changes the mode (and USB Id) from mass storage device to printer device.

    sudo cp 91-dymo-labelmanager-pnp.rules /etc/udev/rules.d/
    sudo cp dymo-labelmanager-pnp.conf /etc/usb_modeswitch.d/    
    
and restart services with:
  
    sudo systemctl restart udev.service

([more info](http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=947))

#### For arch based distributions:
(should also work for manjaro, but not tested yet)
use **udev** and **modeswitch** configurations to work with the LabelManager PNP.
**modeswitch** changes the mode (and USB Id) from mass storage device to printer device.

Install **usb_modeswitch** at first:

    sudo pacman -S usb_modeswitch

if the **/etc/usb_modeswitch.d/** folder was not created at installation do:

    sudo mkdir /etc/usb_modeswitch.d/

now copy the udev and usb_modswitch configs:

    sudo cp 91-dymo-labelmanager-pnp.rules /etc/udev/rules.d/
    sudo cp dymo-labelmanager-pnp.conf /etc/usb_modeswitch.d/    
    
and restart services with:
  
    sudo udevadm control --reload

you might need to change the permissions of the hid device (dymoprint will tell if it is the case):

    sudo chown your_user:users /dev/hidraw0 

([more info](http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?t=947))


### Font management

Fonts are managed via **dymoprint.ini**

You may choose any TTF Font you like

You may edit the file to point to your favorite font.

For my Arch-Linux System, fonts are located at e.g.

	/usr/share/fonts/TTF/DejaVuSerif.ttf

It is also possible to Download a font from
http://font.ubuntu.com/ and use it.

## Modes
### Print text
```./dymoprint MyText```

Multilines will be generated on whitespace

```./dymoprint MyLine MySecondLine # Will print two Lines```

If you want whitespaces just enclose in " "

```./dymoprint "prints a single line"```

### Print QRCodes and Barcodes
```./dymoprint --help```

### Print Codes and Text
just add a text after your qr or barcode text

```./dymoprint -qr "QR Content" "Cleartext printed"```

### Picture printing
Any picture with JPEG standard may be printed. Beware it will be downsized to tape.

```./dymoprint -p mypic.jpg ""```

Take care of the trailing "" - you may enter text here which gets printed in front of the image

## Development 
Besides the travis-ci one should run the following command on a feature implemention or change to ensure the same outcome on a real device:
```
./dymoprint Tst && \
./dymoprint -qr Tst && \
./dymoprint -c code128 Tst && \
./dymoprint -qr qrencoded "qr_txt" && \
./dymoprint -c code128 Test "bc_txt"
```

## Docker

This repository also contains a Dockerfile to print labels in a simple web frontend. With this method you can use
your Dymo LabelWriter without installation of drivers or python on the host. The downside of this that the 
container has to run in privileged mode. This container has only been tested on a Raspberry Pi.

```
docker build --tag dymoprint .
docker run --privileged --rm -p 8000:8000 -v /dev/bus/usb:/dev/bus/usb -d dymoprint
```

http://raspberrypi:8000

### ToDo
- (?)support multiple ProductIDs (1001, 1002) -> use usb-modeswitch?
- put everything in classes that would need to be used by a GUI
- ~~for more options use command line parser framework~~
- ~~allow selection of font with command line options~~
- allow font size specification with command line option (points, pixels?)
- ~~provide an option to show a preview of what the label will look like~~
- ~~read and write a .dymoprint file containing user preferences~~
- ~~print barcodes~~
- ~~print graphics~~
- ~~plot frame around label~~
- vertical print
