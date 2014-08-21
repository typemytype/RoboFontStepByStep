## Build glyphs

# get the current font
font = CurrentFont()

# create a glyph
font.newGlyph("Aacute")
glyph = font["Aacute"]

# add a component
glyph.appendComponent("A")

# add an other component and shift it up
glyph.appendComponent("acute", (0, 150))

# set the metrics for the new glyph
glyph.width = font["A"].width



