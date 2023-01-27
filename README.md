# Dev Duck

It's a duck. It connects to AWS. It lights up on command for 10 seconds. 

You can make a reuest to a URL from anywhere that will trigger the duck to light up

The lambda publishes to a topic. The duck subscribes to that topic.  

These are incomplete instructions.

## Hardware

Check out the circuit diagram and other images in the hardware directory. 

## Software

### AWS Lambda

Create a Lambda function that runs Python. Use `lambda_function.py`

Set up API Gateway as a REST API for the trigger.

Set the role policy to allow the lambda function to publish to AWS IoT. See `duck-lambda-role-policy.txt`

Deploy the function.

### ESP32 Application
It's based on the esp-aws-iot example.

Clone this repo https://github.com/macl-spindance/esp-aws-iot-duck

Checkout the `devduck` branch.

Change directories to `examples/mqtt/tls_mutual_auth`

In the AWS IoT console, create a thing and generate a certificate. 

Download and place the following files in the certs folder.

```
├── certs
│   ├── client.crt
│   ├── client.key
│   └── root_cert_auth.pem
```

Set Up esp-idf tools

```source ~/[PATH TO ESP-IDF]/esp-idf/export.sh```

Connect the ESP32 module and find the serial port

```ls /dev/cu.usb*```

Set the target

```idf.py set-target esp32```


Configure the example. **Set the lambda URL**

```idf.py menuconfig```

Build 

```idf.py build```

Flash
```idf.py -p PORT [-b BAUD] flash```

Monitor the serial port

```idf.py -p PORT monitor```


## Testing

You can test with `api-test.py`

Change the request URL either using an environment variable or hard coded in the file. 

You can also use the AWS IoT MQTT Test Client. 

See the screenshot in `esp-aws-iot-duck/examples/mqtt/tls_mutual_auth/duck-mqtt-test-client.png`

## Limitations / Future Enhancements

* Ideally, the API would be protected with an API key, however, currently there is no authentication. 
* Currently it is hard coded for one duck. In the future it could be set up to interact with a fleet of ducks. 
* Currently the duck just lights up for 10 seconds. In the future it could do other things like quack.
* The lambda responds to any REST API request. Ideally, it should handle different requests differently. 
* The lambda doesn't require a specific payload and the duck doesn't handle different commands. In the future, the command could be made to be configurable by the payload such as the duration of how long it lights up or make it blink instead of just light up.

