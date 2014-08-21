## Contours

glyph = CurrentGlyph()

# a glyph works like a list
# get the first contour
print glyph[0]

# get the last contour
print glyph[-1]

# loop over the glyph contours
for contour in glyph:
    print contour

# get the first contour    
contour = glyph[0]

# get the contour direction
print contour.clockWise
# set the contour direction
contour.clockWise = False

# each contour is a list of segments
for segment in contour:
    print segment
    # each segment is a list of points
    for point in segment:
        print point

# access the points directly
for point in contour.points:
    print points

for bPoint in contour.bPoints:
    print bPoint

# reverse
contour.reverseContour()

# round all coordinates
contour.round()


