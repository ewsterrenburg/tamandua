date: 2014-09-01
author: Erwin Sterrenburg
title: SWMM GISWATER 1: Installation
slug: swmm-giswater-1-installation
tags: GISWATER, SWMM
status: draft
summary: A short welcome messa


#GISWATER Tutorial 1: Installation:

What do you need? JRE

all-in-one or standalone
since none of these components were yet installed on my pc, easy way: all-in-one
What does this do:

- Install GIS water at c:\program files (not X86!)
- Install ... in c:\users\...\giswater with
    - config
    - log
    - portable (postgresql etc)

SWMM
Postgres + Postgis extensions (portable version in all-in-one installer)
QGIS
SWMM gui (not included in all-in-one installer, but available from ...)

sql files for creating db-schema & sample database

Create sample database, run simulation (write inp file, write report file & create gis project)

Create GIS-project
