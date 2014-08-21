## Current Glyph

# if no glyph is selected or no font is open it will return None
glyph = CurrentGlyph()

# if no glyph is selected this will raise an error
print glyph.name
# rename glyph
glyph.name = "myGlyphName"

# get the unicode value
print glyph.unicode
# set a unicode value
# note that the unicode value is not a hex value,
# it is a integer
glyph.unicode = 65

# get the note
print glyph.note
# set a note
glyph.note = "Adjusted by Foo"

# loop over the glyph contours
for contour in glyph:
    print contour
    # code more --> 03_contours.py

# loop over the components
for component in glyph.components:
    print component
    # code more --> 04_components.py

# loop over the anchors
for anchor in glyph.anchors:
    print anchor
    # code more --> 05_anchors.py


