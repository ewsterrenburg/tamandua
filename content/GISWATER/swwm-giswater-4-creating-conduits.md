date: 2014-09-04
author: Erwin Sterrenburg
title: SWMM GISWATER 4: Creating Conduits
slug: swmm-giswater-4-creating-conduits
tags: GISWATER, SWMM
summary: A short welcome message

#GISWATER tutorial 4: creating conduits:

What is the minimum information you need?

- location (i.e. geometry, begin and end-node automatically (if not possible, not arc?)
- arcID (db constraint: simply refuses to save)

'B2424298424436', 1.86, 2.24, 'T', 'BETON', 1, null, 0, 0, 0, 'NO', null, null, 'sector_01'

- names of the inlet and outlet nodes
- offset depth or elevation of the conduit above the inlet and outlet node inverts
- conduit length
- Manning's roughness
- cross-sectional geometry
- entrance/exit losses
- presence of a flap gate to prevent reverse flow
- inlet geometry code number if conduit acts as a culvert

direction from high to low!!! will this be a problem during calculations?
