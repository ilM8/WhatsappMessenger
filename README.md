# WhatsappMessenger
The functions provided with WhatsAppMessenger are there to help you write automated Whatsapp messages via WhatsAppWeb. I'm using the Selenium library to interact with WhatsAppWeb. 

## Requirements
If you want to this to work you will have to install the selenium library using `pip install selenium` on Windows or `python -m pip install selenium` on MacOS and Linux.

The program is written to support the following browsers:
  + Chrome
  + Firefox
  + Safari
 
But as long as a browser is supported by selenium it is supported by this program. Fell free to open an issue for browsers you'd like to be added to the program. For the program to run you will need to tell it what browser you want to use. For that you will have to run the program via the command-line. The command should look something like this: `py messenger.py browser`(Windows), `python messenger.py browser`or `python3 messenger.py`(MacOS and Linux) and replace 'browser' with one of the following:
 + chrome
 + firefox
 + safari
 
For the program to run you will also have to set up a file that's called .env in the same directory as the program. The contents of the file should look like this:
```
{PATH:"Path/to/webdriver.exe"}
```
For selenium to run you will have to download the right webdriver for the browser you're using. Then you will have to write the path to the webdriver executable into the .env file. For further details have a look at the selenium documentation.
***






