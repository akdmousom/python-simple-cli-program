'''
* First of all you have to import os otherwise you can't able to import env variable
* Now you have to import load_dotenv from dotenv otherwise you can't access the .env file
* 3rd step you have to execute the load_dontenv() method this method help us to get access our env file
'''
import os

from dotenv import load_dotenv

load_dotenv()

'''
Now open your .env file and declear a variable with any value like secret = 1122334455. After declear the
variable you have to get some value from user using input method.

Now we have to import the secret key and contain the secret value in a variable
'''
envSecret = int(os.getenv('secret'))

userName = str(input("Enter Your Name: "))

clientSecret = int(input("Enter The Secret Key: "))



