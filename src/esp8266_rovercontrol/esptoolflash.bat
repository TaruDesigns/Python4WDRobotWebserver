esptool.py --port COM5 erase_flash
esptool.py --port COM5 --baud 1000000 write_flash --flash_size=4MB -fm dio 0 bin\esp8266_microdot.bin