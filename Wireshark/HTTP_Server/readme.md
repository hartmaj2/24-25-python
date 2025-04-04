# Info

- this folder contains two servers that can be run with python
- both servers use the `form.html` file as a form to which the user submits data
- the server `server_http.py` provides only http connection and this can be then demonstrated by listening with Wireshark on the loopback channel
- the server `server_https.py` provides https connection, when we inspect the packets with Wireshark, we cannot find plaintext data because everything is ciphered

- to be able to run https server, I need a certificate and key which can be generated using following:
`openssl req -new -x509 -keyout key.pem -out cert.pem -days 365 -nodes`