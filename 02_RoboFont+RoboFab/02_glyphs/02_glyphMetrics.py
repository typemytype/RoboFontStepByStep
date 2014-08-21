## Glyph metrics

glyph = CurrentGlyph()

glyph.leftMargin = 10      # set the left margin to 10
glyph.rightMargin = 10     # set the right margin to 10
print glyph.width

glyph.width = 600          # set the width of the glyph to 600
print glyph.width


# set metrics in all glyphs
font = CurrentFont()

# loop over all glyphs in the font
for glyph in font:
    glyph.leftMargin = 10
    glyph.rightMargin = 10