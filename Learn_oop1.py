def call():
    print("calling one person")
    return 'call done'
class phone:
    price=18888
    color='blue'
    brand='samsung'
    features=['camera','speaker','hammer']
    def call(self):
        print('calling one persion')
    def send_sms(self,phone,sms):
        text=f'send to {phone} and message: {sms}'
        return text    
my_phone=phone()
print(my_phone)    
print(my_phone.price)
print(my_phone.color)
print(my_phone.brand)
print(my_phone.features)
my_phone.call()
print(call())
my_phone.send_sms(1213348,'I forgot miss you')