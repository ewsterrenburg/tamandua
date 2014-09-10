date: 2014-08-30
author: Erwin Sterrenburg
title: SWMM / Giswater tutorial 0: Introduction
slug: swmm-giswater-tutorial-0-introduction
tags: GISWATER, SWMM
status: draft
summary: A short welcome message.

This is the first post in a ... tutorial for using 
Currently studying ... on using SWMM .
Since doing the research anyway, documenting in a series of blog post, for myself and all others interested
focus on swmm... for epanet i expect the processes to be similar. ... with hecras ..., yet my ... with hecras is not sufficient to ...
will be finding out along the way ;) Expect to be running into some issues and there is a risk i'll write down stuff that is ...
If you notice, please notify me so I can correct these mistakes. 

- functionally: how to ... 
- what is happening "under the hood"

Though I'm not familiar with JAVA (and currently don't have any intention to change this), I might be able to assist in the
parts SQL and ... functional ...

The EPA Storm Water Management Model (SWMM) is a dynamic rainfall-runoff simulation model used for single event or long-term (continuous) simulation of runoff quantity and quality from primarily urban areas. The runoff component of SWMM operates on a collection of subcatchment areas that receive precipitation and generate runoff and pollutant loads. The routing portion of SWMM transports this runoff through a system of pipes, channels, storage/treatment devices, pumps, and regulators. SWMM tracks the quantity and quality of runoff generated within each subcatchment, and the flow rate, flow depth, and quality of water in each pipe and channel during a simulation period comprised of multiple time steps.



#SWMM

The EPA Storm Water Management Model (SWMM) is a dynamic rainfall-runoff simulation model used for single event or long-term (continuous) simulation of runoff quantity and quality from primarily urban areas. The runoff component of SWMM operates on a collection of subcatchment areas that receive precipitation and generate runoff and pollutant loads. The routing portion of SWMM transports this runoff through a system of pipes, channels, storage/treatment devices, pumps, and regulators. SWMM tracks the quantity and quality of runoff generated within each subcatchment, and the flow rate, flow depth, and quality of water in each pipe and channel during a simulation period comprised of multiple time steps. 

SWMM was first developed in 1971 and has undergone several major upgrades since then. It continues to be widely used throughout the world for planning, analysis and design related to storm water runoff, combined sewers, sanitary sewers, and other drainage systems in urban areas, with many applications in non-urban areas as well. The current edition, Version 5, is a complete re-write of the previous release. Running under Windows, SWMM 5 provides an integrated environment for editing study area input data, running hydrologic, hydraulic and water quality simulations, and viewing the results in a variety of formats. These include color-coded drainage area and conveyance system maps, time series graphs and tables, profile plots, and statistical frequency analyses. 

##Documentation
Extensive help, both on the relation to the physical world and technology

##Development
SWMM really mature, no active development for some years, yet recently new versions are released ...ly

##Shortcomings:
- either write your own tools to ... or draw in the swmm gui
- The sewer system is maintained in "inp-files", which are isolated: not available in other applications
- Other spatial data is not available in the SWMM GUI for spatial reference (Utilizing a Backdrop Image makes you cry)
- easier switching between simulation conditions

#Giswater

Giswater is an open software project which facilitates communication between water simulation programs and  Geographic Information Systems (GIS). Currently supported simulation tools are EPANET and EPA SWMM. In addition it's also possible to create a SDF file (a standard DEM file) which it's possible to use in order to import terrain data from GIS to other GIS tools or analisys tools such as HEC-RAS. In some cases the communication could be bi-directional and by this way, the result data modeled from this programs could be stored, indexed and consulted into the spatial database.

picture
    store .. network in a postgis database
    --> editing from giswater (adminstrative data) and QGIS
    -->

##Documentation
documentation: not complete, yet improving. HTML really annoying: each section is short and there is no table of contents for quick switching. Solution: printable version: http://www.giswater.org/print/book/export/html/17

#Randvoorwaarden
- For data ... I will use QGIS ()
	- recommended, most mature open gis system
	- familiar with this piece of software
	- 
- For data storage I will use postgis
	- (full functionality, Not all capabilities of Giswater are allowed in DBF mode.)
	- familiar with postgis
	- able to inspect logic (constraints, relations, triggers, etc.) in database
	- 

#Structure
Most episodes will have the following structure:

1. Theory + Underlying physical background of the subject
2. How is .. performed in EPANET SWMM
3. What ... differences:
	- what functions in SWMM does giswater not support?
	- what extra functionality does giswater provide?
4. Conclusions & open ends
