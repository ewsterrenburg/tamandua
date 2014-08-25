date: 2014-09-03
author: Erwin Sterrenburg
title: SWMM GISWATER 3: Creating Junctions
slug: swmm-giswater-3-creating-junctions
status: draft
tags: GISWATER, SWMM
summary: A short welcome message

The (... elaborate) SWMM help provides us with the following information on junctions:
>	Junctions are drainage system nodes where links join together.
>	Physically they can represent the confluence of natural surface channels,
>	manholes in a sewer system, or pipe connection fittings.
>	External inflows can enter the system at junctions.
>	Excess water at a junction can become partially pressurized while
>	connecting conduits are surcharged and can either be lost from the system
>	or be allowed to pond atop the junction and subsequently drain back into the junction.

>	The principal input parameters for a junction are:

>	* invert elevation.
>	* height to ground surface (Maximum depth at the junction (i.e., the distance from the invert to the ground surface) (feet or meters). If zero, then the distance from the invert to the top of the highest connecting link will be used. ).
>	- ponded surface area when flooded (optional).
>	- external inflow data (optional).
>   
>    <cite>Dr. Anteater in "Ant Fugue" in Godel Escher Bach by Douglas R. Hofstadter</cite>

For now, we keep it as simple as possible and leave the two optional attributes for later. However, there are some other
attributes that may seem trivial, yet still require attention:

*	Geometry
*	X-coordinate
*	Y-coordinate
*	NodeID

##SWMM GUI

The GUI of EPA SWMM prodides two ways to create a new node.
It is possible to draw a new node on the map (which ) 
The other way .
If you supp
(which in its turn is placed on the map based on the coordinates supplied).
A nodeID is automatically generated using an autoincremetor,
yet can be replaced manually with an alphanumeric value.
The constraint of unique nodeIDs is enforced by the software


##GISWATER: QGIS as frontdoor

The GISWATER equivalent of drawing a junction in EPA SWMM directly, would b
to add a feature to the junction layer of the created gis-project.

basemaps,
own data (snapping, copy/paste),
more powerful drawing tools. Standard already ..., for more CAD-like functionality,
tracing etc, there are plugins available.
Copy paste / join / Field calculator

-	**do NOT mess around in the nodes layer or in the results layers!!!**
-	**Make sure your postgres server is running when starting the QGIS project. server sluiten: huilen**


###Drawing new junctions

1.  toggle editing of ... layers
2.  draw new feature
3.  NODEID, sector_ID, ..., ...,
4.  save edits.


###Copy - Paste new junctions:

1.  make source layer active (click)
1.  toggle editing of source layers (nodig?)
1.  select features to be copied
1.  click copy button
1.  activate target layer (i.e. junction layer)
1.  toggle editing of target layers
1.  paste features
1.  NODEID, sector_ID, ..., ...,
1.  save edits

Geometrie --> X/Y, niet andersom!
NODEID: handmatig!


##GISWATER: sql as backdoor

When ... insert queries,
ppygis can be helpful

node.node_id, node.top_elev, node.ymax, inp_junction.y0,
	inp_junction.ysur, inp_junction.apond, node.sector_id, node.the_geom

- directly inserting into the database
	- make sure you use v_edit_inp_junction
		- triggers op nieuwe putten
			- wat gebeurt er bij update/delete (en wat met gekoppelde strengen?)

##Conclusions:

much more powerful ways to ... and keep them up-to-date

Initial depth?
Description / TAG missing in GISWATER?
GISWATER introduces the concepts of Sectors
