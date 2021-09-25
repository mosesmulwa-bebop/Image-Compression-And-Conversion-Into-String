import base64

##Here First We Import “Base64“ Method To Encode The Given Image
##Next, We Opened Our Image File In rb Mode Which Is Read In Binary Mode.
##The We Read Our Image With image2.read() Which Reads The Image And Encode it Using b64encode()
##This Method That Is Used To Encode Data Into Base64
##Finally, we Print Our Encoded String
with open("myimage.jpg", "rb") as image2string:
    converted_string = base64.b64encode(image2string.read())
print(converted_string)

with open('encode.bin', "wb") as file:
    file.write(converted_string)
