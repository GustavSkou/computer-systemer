samplesPrSec = 44100
sec = 120
bitsPrSample = 32
bitsInRec = sec * samplesPrSec * bitsPrSample

print(f"{bitsInRec}")

kilobytes = bitsInRec/1000
megabytes = kilobytes/1000
gigabytes = megabytes/1000
terabytes = gigabytes/1000

print(f" bytes = {kilobytes} kilobytes = {megabytes} megabytes = {gigabytes} gigabytes = {terabytes} terabytes")