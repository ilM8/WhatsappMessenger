# WhatsappMessenger
The functions provided with WhatsAppMessenger are there to help you write automated Whatsapp messages via WhatsAppWeb. I'm using the Selenium library to interact with WhatsAppWeb. 

## Requirements
If you want to this to work you will have to install the selenium library using `pip install selenium` on Windows or `python -m pip install selenium` on MacOS and Linux.

The program is written to support the following browsers:
  + Chrome
  + Firefox
  + Safari
 
But as long as a browser is supported by selenium it is supported by this program. Fell free to open an issue for browsers you'd like to be added to the program. For the program to run you will need to write some information that selenium needs into the config.cfg file. First the program needs the path to the webdriver of your browser. Look at the selenium documentation for further information. Also you need the program to tell what browser you're using. We gonna do that by adding one of the following to the config file:
 + chrome
 + firefox
 + safari
 
We seperate the path and the browser we are using by a asterix. Our config.cfg file should look something like this if you're using chome:
```
Path/to/webdriver.exe*chrome
```
***
## How to use it
At the moment we can only send messages with this program but I want and will and more functionality to this. Again feel free to open an issue and request a new function for the program. If you are using the script make sure to import it like this `import messenger`. This will ensure that the whole script will run on import and the driver opens the WhatsAppWeb website. Once the website is loaded you will have to scan the QR-Code on the screen with your phone **through WhatsApp**. After the normal WhatsAppWeb site will open.

### Sending messages
`send_message(chat, message)`
  + *chat*: Here you pass a string that equals the name of the chat you want to send a message in
  + *message*: Here you pass a string that contains the message that is going to be sent
  
  






