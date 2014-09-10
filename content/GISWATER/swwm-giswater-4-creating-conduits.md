date: 2014-09-04
author: Erwin Sterrenburg
title: SWMM GISWATER 4: Creating Conduits
slug: swmm-giswater-4-creating-conduits
tags: GISWATER, SWMM
status: draft
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


The (... elaborate) SWMM help provides us with the following information on junctions:
>   Conduits are pipes or channels that move water from one node to another in the conveyance system.
>   Their cross-sectional shapes can be selected from a variety of standard open and closed geometries.
>   Irregular natural cross-section shapes are also supported, as are user-defined closed shapes.

>   The principal input parameters for conduits are:

>   * names of the inlet and outlet nodes
>   * offset depth or elevation of the conduit above the inlet and outlet node inverts
>   * conduit length
>   * Manning's roughness
>   * cross-sectional geometry
>   * entrance/exit losses
>   * presence of a flap gate to prevent reverse flow
>   * inlet geometry code number if conduit acts as a culvert.
>
>   Conduits designated as culverts are checked continuously during dynamic wave flow routing
>   to see if they operate under Inlet Control as defined in the Federal Highway Administration's
>   publication Hydraulic Design of Highway Culverts (Publication No. FHWA-NHI-01-020, May 2005).
>
>   <cite>Dr. Anteater in "Ant Fugue" in Godel Escher Bach by Douglas R. Hofstadter</cite>

For now, we keep it as simple as possible and leave the two optional attributes for later. However, there are some other
attributes that may seem trivial, yet still require attention:

*   Geometry
*   ArcID /Name
 User-assigned conduit name.

##SWMM GUI



##GISWATER: QGIS as frontdoor


Some of the
* manning (from material)
* crossection (from cat_arc)
* name of inlet + outlet node (results from geometry)
* length (from geometry)



* arcid
* geometry
* cat_arc
* mat_arc

z1 / z2 (from data)
kentry / kexit / kaverage (later on)
qinit / qmax
flapgate + culvert
sector_id




Inlet Offset
 Depth or elevation of the conduit invert above the node invert at the inlet end of the conduit (feet or meters).

Outlet Offset
 Depth or elevation of the conduit invert above the node invert at the outlet end of the conduit (feet or meters).


Initial Flow
 Initial flow in the conduit at the start of the simulation (flow units).

Maximum Flow
 Maximum flow allowed in the conduit (flow units) - use 0 or leave blank if not applicable.



Max. Depth
 Maximum depth of the conduit's cross section (feet or meters).

kentry / kexit / kaverage

Entry Loss Coeff.
 Head loss coefficient associated with energy losses at the entrance of the conduit. For culverts, refer to Culvert Inlet Loss Coefficients table.

Exit Loss Coeff.
 Head loss coefficient associated with energy losses at the exit of the conduit. For culverts, use a value of 1.0.

Avg. Loss Coeff.
 Head loss coefficient associated with energy losses along the length of the conduit.

flap gate

Flap Gate
 YES if a flap gate exists that prevents backflow through the conduit, or NO if no flap gate exists.

culvert

Culvert Code
 Code number of inlet geometry if conduit is a culvert subject to possible inlet flow control -- leave blank otherwise. Refer to the table of Culvert Code Numbers.


Barrels?!
The Barrels field specifies how many identical parallel conduits exist between its end nodes.



New node: just place it :)
Deleting node: connected arcs also deleted!
Moving a node: connected arcs updated!
Change top_elev: direction of connected arcs is updated!

New arc: from begin to end
Change geometry of arc (does not end on node): impossible to place an arc that is not connected to both begin- and end node, so nothing happens
change of geometry (snap to node): begin / end node id + direction are updated
Delete arc: no effect on connected nodes

overnemen z1, z2????
