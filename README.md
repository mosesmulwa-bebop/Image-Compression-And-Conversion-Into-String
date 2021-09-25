# Image-Compression-And-Conversion-Into-String
This compresses an image and converts the resulting image into a string. 
This is useful for sending images over Long Range Radio. 

## Pipeline


Image capture -> Image Compression -> Image Decompression -> Conversion into String -> Send String Via Lora -> Convert string to image -> Send image to database -> Display image

### Image capture

This is from the cameras.

### Image Compression and Decompression

Done using python to reduce size of the image

### Conversion into String

Convert image into form that can be sent via Lora
It may useful to divide string into smaller strings for easier sending

### Send String via Lora

This just sends string via lora.

### Conversion into image

Sent string is re-converted into an image

### Image is sent into the database


