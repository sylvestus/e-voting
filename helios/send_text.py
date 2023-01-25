# import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "48ad9f842c56522fb2e77c719b548a28eba8568530934255642a030ea6700c9d"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
# response = sms.send("Hello Message!", ["+254748595855"])
# print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

def send_mess(x,y):
    return sms.send(x, [y], callback=on_finish)
