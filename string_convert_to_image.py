#First We Import Base64.
#Then We Open Our binary File Where We Dumped Our String.
# Then Open The File rb Mode Which Is Read In Binary Mode.
#Store The Data That was Read From File Into A Variable. Then Close The File
#Then Just Give Any Image File Name (ex:”myimage.png”) And Open It In wb Mode Write In  Binary
#Decode The Binary With b64.decode() Then Close The File With .close()

import base64


file = open('encode.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('reconstructed_image.jpg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()
