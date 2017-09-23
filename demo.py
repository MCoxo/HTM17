import nexmo
import random
import time
import sys

def randompasscode():
	return random.randint(1000,9999)

client = nexmo.Client(key='9657eee7', secret='045a91e184212e69')

users = ['447711853336','a','b','c']

chosen1 = 'a'
chosen2 = 'a'

while chosen1==chosen2:
	chosen=random.sample(users,  2)
	chosen1=users[random.randint(0,3)]
	chosen2=users[random.randint(0,3)]
	
print(chosen1 + ' ' + chosen2 + '\n')

decision = str(input('Is this ok? (y) '))

if decision=='y':
	
	code1 = str(randompasscode())
	code2 = str(randompasscode())
	
	response = client.send_message({
	  'from': 'msg1',
	  'to': chosen1,
	  'text': code1
	})

	response = response['messages'][0]

	if response['status'] == '0':
		print('Sent message ' + response['message-id'])
		print('first message sent \n')
		print('Remaining balance is ' + response['remaining-balance'] + '\n')
	else:
		print('Error: ' + response['error-text'] + '. Message sending failed\n')
		sys.exit(0)
		
	response = client.send_message({
	  'from': 'msg2',
	  'to': chosen2,
	  'text': code2
	})

	response = response['messages'][0]

	if response['status'] == '0':
		print('Sent message ' + response['message-id'])
		print('second message sent \n')
		print('Remaining balance is ' + response['remaining-balance'] + '\n')
	else:
		print('Error: ' + response['error-text'] + '. Message sending failed\n')
		sys.exit(0)
	
else:
	print('invalid input\n')
	