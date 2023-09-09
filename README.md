<img src="static/img/logo.png">

# Dangerous Pickle

## Description

John Judgment Organization uses the software Dangerous Pickle to operate its eletrical doors.

However, the management is afraid that the software is not secure enough and hired you to audit it.

The IT departament gave you a container with the necessary files to run the software locally.

The applications read keycards however there is also a way to open the door by inputing the cards code that is in **base64**.

The team gave you to test the code of the guest card: `eyJweS9vYmplY3QiOiAiYXBwLlVzZXIiLCAicHkvc3RhdGUiOiB7InVzZXJuYW1lIjogImd1ZXN0In19`

They told you there are two diffrent types of cards: `worker` and `guest`.

**Can you gain worker access by using the guest card?**

The IT team suspects there is a vulnerable dependency in the software.

To help them prove their theory, they added a flag in the /tmp repository of the container called flag.txt.

**Can you access it?**

## Challenge

This is a pretty easy challenge and its based on a popular package that is vulnerable to deserialization attacks.

Explore exploit-db and you will find the answer. Or github.

## Setup

To run this challenge you need to have docker installed.

To build the image run:

```bash
docker build --tag dangerous-pickle . 
```

To run the image run:

```bash
docker run -p 5000:5000 dangerous-pickle
```

## Solution

In case you are stuck, this repo contains a python script that creates a malicious payload that can be used to exploit the vulnerability.

You can write different payloads to test different things.

You case you do not know how to write the payload, there is a good repo for generating payloads for this vulnerability: [Github](https://github.com/j0lt-github/python-deserialization-attack-payload-generator/tree/master)

## License

MIT License