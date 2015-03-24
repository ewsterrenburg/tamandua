date: 2014-11-11
author: Erwin Sterrenburg
title: EPA SWMM / Giswater Tutorial 5: Outfalls
slug: swmm-giswater-tutorial-5-outfalls
tags: SWMM, Giswater, Water
summary: This is the 5<sup>th</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system.

This is the 5<sup>th</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system.

> Outfalls are terminal nodes of the drainage system used to define final downstream boundaries under Dynamic Wave flow routing. For other types of flow routing they behave as a junction. Only a single link can be connected to an outfall node.
>
> The boundary conditions at an outfall can be described by any one of the following stage relationships: 
> * the critical or normal flow depth in the connecting conduit  
>
> * a fixed stage elevation  
>
> * a tidal stage described in a table of tide height versus hour of the day  
>
> * a user-defined time series of stage versus time.  
>
> The principal input parameters for outfalls include: 
>
> * invert elevation  
>
> * boundary condition type and stage description  
>
> * presence of a flap gate to prevent backflow through the outfall.  


Name 
 User-assigned outfall name. 
 
X-Coordinate 
 Horizontal location of the outfall on the Study Area Map. If left blank then the outfall will not appear on the map. 
 
Y-Coordinate 
 Vertical location of the outfall on the Study Area Map. If left blank then the outfall will not appear on the map. 
 
Description 
 Click the ellipsis button (or press Enter) to edit an optional description of the outfall. 
 
Tag 
 Optional label used to categorize or classify the outfall. 
 
Inflows 
 Click the ellipsis button (or press Enter) to assign external direct, dry weather or RDII inflows to the outfall. 
 
Treatment 
 Click the ellipsis button (or press Enter) to edit a set of treatment functions for pollutants entering the node. 
 
Invert El. 
 Invert elevation of the outfall (feet or meters). 
 
Tide Gate 
 YES - tide gate present to prevent backflow 
NO - no tide gate present 
 
Type 
 Type of outfall boundary condition: 
FREE: outfall stage determined by minimum of critical flow depth and normal flow depth in the connecting conduit 
NORMAL: outfall stage based on normal flow depth in the connecting conduit 
FIXED: outfall stage set to a fixed value 
TIDAL: outfall stage given by a table of tide elevation versus time of day 
TIMESERIES: outfall stage supplied from a time series of elevations 
 
Fixed Stage 
 Water elevation for a FIXED type of outfall (feet or meters). 
 
Tidal Curve Name 
 Name of the Tidal Curve relating water elevation to hour of the day for a TIDAL outfall (double-click to edit the curve). 
 
Time Series Name 
 Name of time series containing time history of outfall stage for a TIMESERIES outfall (double-click to edit the series). 
 
 
Only thing required before running the model is possible is to create an outfall.

Create outfall
Run EPA SWMM (not that the results make any sense without inflows)

GISWATER: run not possilbe


#CONCLUSIONS:

Convert - absent in GISWATER

Sectors are relevant :)