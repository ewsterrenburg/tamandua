date: 2014-09-03
author: Erwin Sterrenburg
title: EPA SWMM / Giswater Tutorial 3: Creating Junctions
slug: swmm-giswater-tutorial-3-creating-junctions
status: draft
tags: SWMM, Giswater, Water
summary: This is the 1<sup>st</sup> episode in my tutorial on the using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episodes describes the installation process.

This is the 3<sup>rd</sup> episode in my tutorial on the using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episodes describes how to create junctions in EPA SWMM, using QGIS and using SQL insert statements. 

The (... elaborate) SWMM help provides us with the following information on junctions:
>   Junctions are drainage system nodes where links join together.
>   Physically they can represent the confluence of natural surface channels,
>   manholes in a sewer system, or pipe connection fittings.
>   External inflows can enter the system at junctions.
>   Excess water at a junction can become partially pressurized while
>   connecting conduits are surcharged and can either be lost from the system
>   or be allowed to pond atop the junction and subsequently drain back into the junction.

>   The principal input parameters for a junction are:

>   * invert elevation.
>   * height to ground surface (Maximum depth at the junction (i.e., the distance from the invert to the ground surface) (feet or meters). If zero, then the distance from the invert to the top of the highest connecting link will be used. ).
>   - ponded surface area when flooded (optional).
>   - external inflow data (optional).

For now, we keep it as simple as possible and leave the two optional attributes for later. However, there are some other attributes that may seem trivial, yet still require attention:

*   Geometry
*   X-coordinate
*   Y-coordinate
*   NodeID

#EPA SWMM

The graphical user interface of EPA SWMM prodides two ways to create a new node.
It is possible to draw a new node on the map, in which case the location where you click the map is used to determine the X- and Y-coordinate.
The other way around is to ..., in which case the location on the map where the junction is placed is determined based on the values supplied for the X- and Y-coordinate.
In both cases, a nodeID is automatically generated using an autoincrementor, with the prefixes and increment supplied in the project defaults (zie deel 2!). 
It is possible to replace the automatically generated NodeID with your own value, yet each node should have an unique ID. This constrained is enforced by the software.

#GISWATER: QGIS AS FRONTDOOR

The Giswater equivalent of drawing a junction in EPA SWMM directly, would be to draw a new feature in in the junction layer of the corresponding GIS-project.
advantages over ...:

- Possibility to add basemaps (voetnoot: EPA basemaps make you cry);
- Possibility to add your own geospatial data as a reference, snap new objects on these features and paste the geometry of these features in your SWMM layers;
- More power full drawing tools. Standard already ..., for more CAD-like functionality, tracing etc, there are plugins available;
- A field calculator to update attributes in bulk.

[PLAATJE?]

###Sectors

***SECTORS***

1.  toggle editing of ... layers
2.  draw new feature
3.  NODEID, sector_ID, ..., ..., handmatig (or field calculator :))
4.  save edits.

###Drawing new junctions

[plaatje?]

1.  toggle editing of ... layers
2.  draw new feature
3.  NODEID, sector_ID, ..., ..., handmatig (or field calculator :))
4.  save edits.

###Copy - Paste new junctions:

[plaatje?]

1.  make source layer active (click)
1.  toggle editing of source layers (nodig?)
1.  select features to be copied
1.  click copy button
1.  activate target layer (i.e. junction layer)
1.  toggle editing of target layers
1.  paste features
1.  NODEID, sector_ID, ..., ...,
1.  save edits

###Important DON'Ts

-   **do *++NOT++* mess around in the nodes layer or in the results layers!!! Drawing in these layers will not activate the required database functions to ... the new objects in the correct way.**
-   **Make sure your Postgres server is running when starting the QGIS project (i.e. do not close the ... of the portable postgres). server sluiten: huilen**

#GISWATER: SQL AS BACKDOOR
Drawing a new system: QGIS (or other GIS software configured for editing the correct tables). However, in many cases information already available from other sources (CAD-drawings, geodatabases, ..., etc.). In these case, you could use scripting to .. this information and ... into the database. The insert queries could directly be executed by your code, yet I like to keep insight in what is happening. Therefore, my approach was to use python scripts which write the insert queries to a file. 

For the geometry: ppygis can be helpful

node.node_id, node.top_elev, node.ymax, inp_junction.y0,
    inp_junction.ysur, inp_junction.apond, node.sector_id, node.the_geom


```SQL
INSERT INTO "test_zanderij_31121"."v_inp_edit_junction" VALUES ('C3422736', 2.23, 0, 0, 0, 0, 'sector_01', '010100002091790000f853e3655a0f2141ec51b81ebbbb2341');
```


- directly inserting into the database
- make sure you use v_edit_inp_junction
- triggers op nieuwe putten
- wat gebeurt er bij update/delete (en wat met gekoppelde strengen?)


#Conclusions:

much more powerful ways to ... and keep them up-to-date

###Open ends:
Geometrie --> X/Y, niet andersom! (wat bedoel ik hier in vredesnaam mee?)

Description / TAG missing in GISWATER?
GISWATER introduces the concepts of Sectors
Initial depth is not explicitly mentioned, what to do with this?
ponded surface area when flooded (optional).
external inflow data (optional).
