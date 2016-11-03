# Script Name       : main.py
# Author            : Shy Ruparel
# Created           : September 8 2015

# Pulls in data from "data.csv" which is 2 columns wide
# Uses a base image as the background
# Uses the data - school name, and venue address -
# and prints onto the base image
# and saves every image as a .PNG

from PIL import Image, ImageDraw,ImageFont
import csv

# Main image from base.jpg
im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .80

# Text writing onto image
with open('data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        im = Image.open('base.jpg').convert('RGBA')

        venueSize = MaxSize
        addressSize = MaxSize/2

        # Grab name and address
        venueName = row[0].decode('utf-8')
        addressDetails = row[1].decode('utf-8')

        # Set font and size
        venue = ImageFont.truetype('fonts/OpenSansBold.ttf', venueSize)
        address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)

        draw = ImageDraw.Draw(im)

        # Find size of text
        wVenue, hVenue = draw.textsize(venueName,font=venue)

        # Make size smaller until width is less than size of maxFontW
        while (wVenue > maxFontW):
            venueSize = venueSize - 10
            venue = ImageFont.truetype('fonts/OpenSansBold.ttf', venueSize)
            wVenue, hVenue = draw.textsize(venueName,font=venue)

        wAddress, hAddress = draw.textsize(addressDetails,font=address)

        while (wAddress > maxFontW):
            addressSize = addressSize - 10
            address = ImageFont.truetype('fonts/OpenSansRegular.ttf', addressSize)
            wAddress, hAddress = draw.textsize(addressDetails,font=address)

        # Put text onto the image
        draw.text(((W-wVenue)/2,(H-hVenue)/2 ), venueName,font=venue, fill="black")
        draw.text(((W-wAddress)/2,((H-hAddress)/2)+hVenue), addressDetails,font=address, fill="black")

        # Save out the image
        filename = 'output/' + venueName.strip() + '.png'
        filename = filename.replace (" ", "_")
        print filename
        im.save(filename,'PNG')