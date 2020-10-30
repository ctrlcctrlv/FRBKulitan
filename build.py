#!/usr/bin/env python3

import fontforge
import psMat

font = fontforge.open("FRBKulitan.sfd")

scale_matrix = psMat.scale(0.8, 1)

for i in list(range(0x14C00, 0x14C0B+1)) + [0x14C0E, 0x14C10]:
    g = font[font.findEncodingSlot(i)]
    ng = font.createChar(-1, g.glyphname+"80")
    ng.background = g.background
    ng.background = ng.background.transform(scale_matrix)
    ng.foreground = ng.background
    ng.stroke("circular", 65)
    ng.width = int(g.width*0.8)

font.mergeFeature("features.fea")

font.save("FRBKulitan-temp.sfd")
font.generate("FRBKulitan.otf")
font.close()
