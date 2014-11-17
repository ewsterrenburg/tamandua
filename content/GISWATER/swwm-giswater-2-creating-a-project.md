date: 2014-09-20
author: Erwin Sterrenburg
title: EPA SWMM / Giswater Tutorial 2: Project Setup
slug: swmm-giswater-tutorial-2-project-setup
tags: SWMM, Giswater, Water
summary: This is the 2<sup>nd</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episode describes how to create new project in EPA SWMM, how to create a project using Giswater and the initial options that need to be set before we can start creating our network.

This is the 2<sup>nd</sup>  episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episode describes how to create new project in EPA SWMM, how to create a project using Giswater and the initial options that need to be set before we can start creating our network. 

#EPA SWWM
Starting a new project in EPA SWMM is a simple as starting up the program. A new project is opened and you can directly start drawing a sewer network. A project can be saved as a SWMM-input file (**INP-file**). Such an input-file contains both all objects in a project's network and all options set by the user. Since a standard set of default values is provided, we could start drawing the network without further preparation. Most options deal with the look-and-feel of the program and the simulation parameters. For these options, we will keep the default values for now. Some options however do affect the drawing of the network and will need to be set beforehand:

![SWMM_Defaults](/images/SWMM_defaults.png "Default prefixes for EPA SWMM objects.") 

<ol>
<li>Specify whether the automatic computation of conduit lengths and subcatchment areas is turned on or off.</li>
<li>Choose whether the positions of links above the invert of their connecting nodes are expressed as a Depth above the node invert or as the Elevation of the offset.</li>
<li>Select flow units that makes sense (i.e. change the default Cubic Feet per Second to Cubic Metres per Second).
<li>Change the map dimensions and extent to appropriate values (available from the menu: <strong>View <i class="fa fa-long-arrow-right"></i> Dimensions</strong>).
<li>On the ID Labels page of the defaults menu (<strong>Project <i class="fa fa-long-arrow-right"></i> Defaults</strong>), set the ID Prefixes as follows (leave the others blank):
<ul>
<li>Rain Gages: <strong>Gage</strong></li>
<li>Subcatchments: <strong>S</strong></li>
<li>Junctions: <strong>J</strong></li>
<li>Outfalls:  <strong>Out</strong></li>
<li>Conduits: <strong>C</strong></li>
<li>ID Increment: <strong>1</strong></li>
</ul>
</li>
</ol>
This will make EPA SWMM automatically label new objects with consecutive numbers following the 	designated prefix.

# GISWATER

### Software configuration
The software configuration window can be opened from the menu (**Configuration** :fa-long-arrow-right: **Software configuration**). The options that can be set here determine how Giswater deals with inputfiles, outputfiles and the database. For these options, we keep the default values. If you would use your own database, this is the place where you can set up the location of the database administration program (PGADMIN3).

### Database connection
The software configuration window can be opened from the menu (**Configuration** :fa-long-arrow-right: **Database configuration**). If I remember correctly, this was all working correctly without alterations for the included portable postgis database. If you would use your own database, this is the place where you can set up the connection.

### Creating a EPA SWMM project

The easiest way to start a project in Giswater is to load the EPA SWMM DB Sample project.
The corresponding option in the project menu loads a sample project into the db using the sql files in the installation directory. You can do this an play around for a while. The goal for this episode in my tutorial is to create an empty project, so we'll take a different track:

- Open the EPA SWMM window (**Software** :fa-long-arrow-right: **EPA SWMM**):

![Giswater_EPA_SWMM](/images/Giswater_EPA_SWMM.png "Giswater EPA SWMM window.")

- Create a project and supply the following characteristics:
    - Name of the project
    - Title of the project
    - Author of the project
    - Date create
    - SRID of the coordinate system to be used

![Giswater_create_project](/images/Giswater_create_project.png "Giswater create project window.")

- Pressing the options button would open en windows in which we can set a broad array of options. A few of the affect  our system have sensible defaults Options: sensible defaults, so we keep them as is.

### Creating a GIS-project

After we created the project, all necessary tables are present so theoretically we could start filling these tables with information about our system. However, these tables are not yet easy accessible for the GIS superpowers yet. In order to facilitate this, Giswater contains a function to create a GIS-project that can be opened and modified using QGIS. During this process, a QGIS-project is created with the EPA SWMM data (i.e. the objects in the system and input tables) and simulation analysis in its table of contents. 

![Giswater_create_gisproject](/images/Giswater_create_gisproject.png "Giswater create GIS-project window.")

Now I could should you our tutorial project in QGIS, yet that would look somewhat empty in it's current state. Therefore I'll provide a screenshot of the GIS-project created based on the sample project:

![QGIS_sample_epaswmm](/images/QGIS_sample_epaswmm.png "Sample EPA SWMM project in QGIS.")

#CONCLUSIONS:
Starting a new project in Giswater is a little more work than in vanilla EPA SWMM. This amount of work however is still very small. Creating a GIS-project is trivial and gives us the opportunity to visualize and edit our system in a proper GIS-environment with the possibility to add our own data. background maps, web services etc. etc.
