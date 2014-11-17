date: 2014-10-09
author: Erwin Sterrenburg
title: EPA SWMM / Giswater Tutorial 3: Creating Junctions
slug: swmm-giswater-tutorial-3-creating-junctions
tags: SWMM, Giswater, Water
summary: This is the 3<sup>rd</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episode describes how to create junctions in EPA SWMM, using QGIS and using SQL insert statements.

This is the 3<sup>rd</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episode describes how to create junctions in EPA SWMM, using QGIS and using SQL insert statements. 

The wonderful EPA SWMM help provides us with the following information on junctions:
>   Junctions are drainage system nodes where links join together.
>   Physically they can represent the confluence of natural surface channels,
>   manholes in a sewer system, or pipe connection fittings.
>   External inflows can enter the system at junctions.
>   Excess water at a junction can become partially pressurized while
>   connecting conduits are surcharged and can either be lost from the system
>   or be allowed to pond atop the junction and subsequently drain back into the junction.

>   The principal input parameters for a junction are:

>   * invert elevation;
>   * height to ground surface: maximum depth at the junction (i.e., the distance from the invert to the ground surface) (feet or meters). If zero, then the distance from the invert to the top of the highest connecting link will be used;
>   * ponded surface area when flooded (optional);
>   * external inflow data (optional).

For now, we keep it as simple as possible and leave the two optional attributes for later. However, there are some other attributes that may seem trivial, yet still require attention:

*   Geometry;
*   X-coordinate;
*   Y-coordinate;
*   NodeID.

#EPA SWMM

The graphical user interface of EPA SWMM provides two ways to create a new node:

1. It is possible to draw a new node on the map, in which case the location where you click the map is used to determine the X- and Y-coordinate;
2. The other way around is to navigate to junctions in the tree view in the tree view, select "junctions" by using the left mouse button, followed by pressing the "Add new" button. Using this approach, the location on the map where the junction is placed is determined based on the values supplied for the X- and Y-coordinate.

![SWMM_create_junction](/images/SWMM_create_junction.png "Creating a junction in EPA SWMM.")

In both cases, a NodeID is automatically generated using an autoincrementor, with the prefixes and increment supplied in the project defaults (see [Episode 2: Project Setup](/blog/2014/09/20/swmm-giswater-tutorial-2-project-setup/)).
It is possible to replace this automatically generated NodeID with your own value, yet each node should have an unique ID. This constrained is enforced by the software.

Double-clicking on a node opens it's attribute form in which the attributes can be modified.
The location of a junction can be changed by dragging the junction to a new location, or by changing the X- and Y-attributes. A selected node can be removed by pressing the "Delete" key on your keyboard, or by using the "Delete object" button next to the "Add new" button.

#GISWATER: QGIS AS FRONTDOOR

The Giswater equivalent of drawing a junction in EPA SWMM directly, would be to draw a new feature in in the junction layer of the corresponding GIS-project. This approach offers the following advantages:

- Adding basemaps;[^backdrop_image]
- Adding your own geo-spatial data as a reference, to snap new objects on or to copy-paste the geometry into the SWMM layers;
- Sophisticated drawing tools (cadtools, Autotrace, GPS) availabe as plugins;
- A field calculator to update attributes in bulk.

###Sectors
Giswater introduces the concept of sectors. I haven't found out yet whether using sectors in your data is required or not. I'll ignore them for now and come back to this either when I'll make an episode on the functioning of sectors or when the calculation refuses to run :fa-smile-o:.

###Drawing new junctions

![QGIS_create_junctions](/images/QGIS_create_junctions.png "Creating junctions in QGIS.")

1. Make the Junctions layer (**EPA SWMM DATA** :fa-long-arrow-right: **Hydraulics** :fa-long-arrow-right: **Node** :fa-long-arrow-right: **Junctions** ) active by clicking on this layer in the content tree of the map;
2. Toggle editing (**a**);
3. Add new features (**b**);
4. In the attribute form, supply values for node_id, top_elev, ymax and optionally for the other attributes (**c**);
5. Save layer edits (**d**).

###Copy - Paste new junctions

1. Make the source layer for the junctions to be pasted active;
2. Toggle editing of this layer (**a**);
3. Select the features to be copied using the selection tools provided by QGIS;
4. Click "Copy features" button (**e**);
5. Make the Junctions layer active;
6. Toggle editing (**a**);
7. Paste features (**f**);
8. If attributes with the same name were present in the source layer, they will be transferred over. Otherwise, supply values for node_id, top_elev, ymax and optionally for the other attributes (**c**);
9. Save layer edits (**d**).

###Modify the location of a junction

1. Make the Junctions layer active;
2. Toggle editing (**a**);
3. Move features (**g**);
4. Drag junction to new location;
5. Save layer edits (**d**).

###Modify the attributes of a junction
1. Make the Junctions layer active;
2. Toggle editing (**a**);
3. Open the attribute form using the "Identify Features" button (**i**) or open the attribute table (**j**);
4. Fill in the new attribute values (**c**);    
5. Save layer edits (**d**).

###Delete a junction
1. Make the Junctions layer active;
2. Toggle editing (**a**);
3. Select features;
4. Delete selected using the "Delete selected" button (**h**) or pressing the "Delete" key;
5. Save layer edits (**d**).


###Important DON'Ts

-   Do ***NOT*** mess around in the nodes layer or in the results layers!!! Drawing in these layers will not activate the required database functions to create new objects correctly.
-   Make sure your Postgres server is running when starting the QGIS project (i.e. do not close the command prompt window of the portable Postgres). If the server stops with your GIS-project open, QGIS will spit out a endless loop of pop-ups stating that it is not able to reach the server. QGIS can now only be stopped with violence.

#GISWATER: SQL AS BACKDOOR
When you are drawing a drainage system from scratch, QGIS (or other GIS software configured for editing the correct tables) would be the way to go. However, in many cases information is already available from other sources (CAD-drawings, geodatabases, Excel-files, etc.). In these cases, you could also use scripting to interpret this information and insert it into the database. These insert queries could directly be executed from your code, yet I like to keep insight in what is happening. Therefore, my approach was to use python scripts which write the insert queries to a SQL-script. 

If X- and Y-coordinates are available, the value to be inserted in the geometry field can be generated using [PPyGIS](http://www.fabianowski.eu/projects/ppygis/). Although in the documentation is stated that PPyGIS is young and has several limitations, it does this job really well. The following python code generates insert statements for 4 junctions in a strictly random street somewhere in the east of the Netherlands:

```python
import ppygis
import psycopg2

SRID = 28992
schema = 'tutorial'
junction_view = 'v_inp_edit_junction'
junction_fields = '(node_id, top_elev, ymax, y0, ysur, apond, sector_id, the_geom)'
junction_query = r'INSERT INTO "{0}"."{1}" {2} VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'.format(schema, junction_view, junction_fields)

class junction():
    '''
    This is a junction
    '''
    def __init__(self,NodeID,X,Y,Z):
        '''
        Constructor
        '''
        self.NodeID = NodeID
        self.X = X
        self.Y = Y
        self.Z = Z
        self.MaxDepth = 0           # take values from connected reaches
        self.InitDepth = 0          # 0 for now, to be examined later
        self.SurchargeDepth = 0     # optional, to be examined later
        self.PondingArea = 0        # optional, to be examined later
        self.SectorID = None        # ignore for now, to be examined later
        self.Geometry = ppygis.Point(self.X,self.Y,srid=SRID)

    @property
    def InsertValues(self):
        return (self.NodeID, self.Z, self.MaxDepth, self.InitDepth, \
                self.SurchargeDepth, self.PondingArea, self.SectorID, \
                self.Geometry.write_ewkb())


conn = psycopg2.connect('dbname=giswater_ddb user=postgres port=5431')
cur = conn.cursor()

# Here you can put the logic that reads out the files/databases
# that contain locations and/or attributes of your junctions
node_ids = ['J1', 'J2', 'J3', 'J4']
x = [255320.35, 255347.98, 255365.84, 255375.21]
y = [472276.25, 472302.63, 472319.22, 472328.19]
z = [33.11, 33.03, 32.76, 32.89]

for i in xrange(4):
    example_junction = junction(node_ids[i], x[i], y[i], z[i])
    junction_values =  example_junction.InsertValues

    # and write the resulting query to a file, not stdout
    print cur.mogrify(junction_query, junction_values)

conn.close()

```

Which results in the following SQL-statement:

```SQL
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J1', 33.11, 0, 0, 0, 0, None, '010100002040710000cdccccccc22a0f410000000051d31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J2', 33.03, 0, 0, 0, 0, None, '010100002040710000713d0ad79f2b0f4152b81e85bad31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J3', 32.76, 0, 0, 0, 0, None, '01010000204071000085eb51b82e2c0f4114ae47e1fcd31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J4', 32.89, 0, 0, 0, 0, None, '010100002040710000e17a14ae792c0f41295c8fc220d41c41');

```

As you can see, this insert query should also executed on the view that contains the junctions, not directly on the node table. Update and delete queries should also be performed on this view.

#CONCLUSIONS:

QGIS provides much more powerful tools to draw and modify your objects than using EPA SWMM directly. 
No incremental IDs are handed out automatically, yet the field calculator provides a powerful tool ot generate them in bulk. Data integrity is maintained by the database trigger and constraints. This works works well, however you need to be ***really*** careful to make your edits to the correct layer.

###Open ends:

- The description and TAG attributes of the junctions are not present in Giswater. Within a GIS-environment, there is less need for this functionality. However including the description attribute would be a minor development effort. Supporting the use of tags might need more effort;
- Giswater introduces the concepts of sectors. It is not yet clear to me what their function is and whether it is required to use them;
- The initial depth does not seem to be explicitly mentioned in the EPA SWMM help. This attribute will need to be examined further.

[^backdrop_image]: It is possible to add a street map, utility map, topographic map, site development plan, or any other relevant picture or drawing as a backdrop image in EPA SWMM.This can be useful, yet ... to a proper GIS-environment.

