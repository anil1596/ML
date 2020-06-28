from gtts import gTTS
text = ['tuen on multi view', 'turn off universal remote setup', 'turn ambient mode off', 'set volume to 20', 'take me to zee5 app', 'open youtube', 'turn off the internet', 'search action movies on jioCinema', 'show me some comedy movies', 'view ambient mode', 'open hotstar', 'open settings', 'take me to gallery now', 'switch to internet browser', 'stop the tv settings please']

language = 'en-us'
count = 0
prstr = ''
i = 0
print('len text : ', len(text))
while i < len(text):
	print('inside while : ', text[i])
	speech = gTTS(text = text[i], lang = language, slow = False )
	name = str(count)+'.mp3'
	speech.save(name)
	i+=1
	count+=1
