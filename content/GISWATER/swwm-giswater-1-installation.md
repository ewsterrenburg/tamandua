date: 2014-09-10
author: Erwin Sterrenburg
title: SWMM / Giswater tutorial 1: Installation
slug: swmm-giswater-tutorial-1-installation
tags: SWMM, Giswater, Water
status:
summary: This is the 1<sup>st</sup> episode in my tutorial on the using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage system network. This episodes describes the installation process.

The instructions in the [Giswater documentation](http://www.giswater.org/print/book/export/html/17) provided sufficient information for installing this software. To install you must download the installer package and execute it. Remember you can choose the [Giswater stand-alone install package](http://download.giswater.org/giswater_stand-alone.exe) or the [all-in-one install package](http://download.giswater.org/giswater_all-in-one.exe). The all-in-one installer package is designed with a portable version of PostgreSQL+PostGIS 2.1. Remember you need to have installed an updated Java Runtime Environment (JRE) on your computer.

I took the easy road and used the all-in-one installer. Installation using the installation wizard proved to be straight-forward. When the dust had settled, the following had taken place:

1. Giswater had been placed in it's standard installation path (__C:\Program Files\Giswater\\__, so apparently it's a 64-bit application) with the following sub-folders:
    -  __epa__ - EPANET & EPA SWMM command line executables;
    -  __gis__ - templates for gisproject export(?);
    -  __images__ - images used in the Giswater graphical user interface;
    -  __inp__ - sqlite-databases used in the information exchange between the database and the input / output files of the simulation tools & templates for these files;
    -  __legal__ - GPL v3 license;
    -  __lib__ - java libraries used by the Giswater application;
    -  __samples__ - SQL-scripts containing data for sample projects;
    -  __sql__ - SQL-scripts containing database logic.
2. Some additional folders had been placed in __C:\Users\&lt;username&gt;\Giswater\\__:
    - __config__ - some general configuration files;
    - __log__ - logging directory for giswater application;
    - __portable__ - portable installation of postgresql + postgis + pgadmin3.

##EPA SWWM
Since on of my objectives is to make a comparison between using SWMM toghether with Giswater and a vanilla EPA SWMM setup, I also need to have EPA SWMM 5.0.022 installed (the only version supported by Giswater). However, this version is not available anymore from the [EPA website](http://www2.epa.gov/water-research/storm-water-management-model-swmm). After about 3 years of sleep, the EPA SWMM model is actively developed again. Usually this is good news, but when other products depend on older versions that have been taken offline, it is bad news as well...

For this tutorial, it won't be a problem, since I already had version 5.0.022 installed on my computer. Yet, there is a bigger issue here: a lot of functionality with regard to the visualization of the simulation results (charts, profiles, animations, etc.) is not possible without the EPA SWMM graphical user interface. Following could be done to make this functionality also available to Giswater users (in order of personal preference):

1. Giswater developers keep their software compatible with the most recent version of EPA SWMM;
2. EPA also makes version 5.0.022 available for download, since this has been the stable version for almost 3 years;
3. Giswater developers also supply a download for the full version of EPA SWMM 5.0.022, not just the command line version.

Let's hope one of the parties involved reads this and takes action to solve this issue :fa-smile-o:.
