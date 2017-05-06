# pi_api

The goal of this program is to write a restful api in flask that allows me to query my pi from anywhere and return something interesting, like a photo of the backyard or the temperature in the house.

Right now, it's pretty lame; when the server is running (and you're on the LAN), you can type `http://192.168.0.8:5000/temp` into the browser to get the temperature of the pi's cpu.

## to do:
- [ ] set up camera
- [ ] take a photo when queried with a certain GET request
- [ ] show the photo to the user (see [here](http://stackoverflow.com/questions/8637153/how-to-return-images-in-flask-response))
