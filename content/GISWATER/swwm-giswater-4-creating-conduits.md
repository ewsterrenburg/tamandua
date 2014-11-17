date: 2014-11-11
author: Erwin Sterrenburg
title: EPA SWMM / Giswater Tutorial 4: Creating Conduits
slug: swmm-giswater-tutorial-4-creating-conduits
tags: SWMM, Giswater, Water
summary: This is the 4<sup>th</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episodes describes how to create conduits in EPA SWMM, using QGIS and using SQL insert statements.

This is the 4<sup>th</sup> episode in my tutorial on using EPA Storm Water Management Model (EPA SWMM) and Giswater for rainfall-runoff modeling for an urban drainage network system. This episodes describes how to create conduits in EPA SWMM, using QGIS and using SQL insert statements.

The wonderful EPA SWMM help provides us with the following information on conduits:
>   Conduits are pipes or channels that move water from one node to another in the conveyance system.
>   Their cross-sectional shapes can be selected from a variety of standard open and closed geometries.
>   Irregular natural cross-section shapes are also supported, as are user-defined closed shapes.

>   The principal input parameters for conduits are:

>   * Names of the inlet and outlet nodes;
>   * Offset depth or elevation of the conduit above the inlet and outlet node inverts;
>   * Conduit length;
>   * Manning's roughness;
>   * Cross-sectional geometry	(profile describing parameters and the number of barrels);
>   * Loss coefficients (headloss coefficients for the entrance, exit and average along the length of the conduit);
>   * Presence of a flap gate to prevent reverse flow;
>   * Inlet geometry code number if conduit acts as a culvert.
>
>   Conduits designated as culverts are checked continuously during dynamic wave flow routing
>   to see if they operate under Inlet Control as defined in the Federal Highway Administration's
>   publication Hydraulic Design of Highway Culverts (Publication No. FHWA-NHI-01-020, May 2005).

Attributes that can be supplied, yet not mentioned as principal input parameters are:

*	Initial flow in the conduit at the start of the simulation;
*	Maximum flow allowed in the conduit (use 0 or leave blank if not applicable);
*	Maximum depth of the conduit's cross section;
*	Culvert code number of inlet geometry if conduit is a culvert subject to possible inlet flow control (leave blank otherwise).

Similar to the junctions, there are some other attributes that may seem trivial, yet still require attention:

*   Geometry;
*   ArcID.

#ARC-NODE TOPOLOGY

EPA SWMM is modelling the drainage system using an Arc-Node Topological Model. Such a topology exerts some rules of the objects in order to maintain network integrity.

> 1. A node is an intersection point where two or more arcs meet. Can also occur at the end of a “dangling” arc (i.e. an arc that is not connected to another arc);

> 2. An arc is defined as a line vector that start and end at a node. Arcs can either be straight line vectors between two nodes or consist of multiple segments that together form the connection between two nodes. The (optional) points along an arc that define its shape are called Vertices;

> 3. Every Arc has a direction (which may or may not be the same as the hydraulic direction).

The rules described above, result in the following behavior of the objects:

* A new arc can only be constructed as a connection between 2 separate existing nodes;
* If an arc is deleted, nodes that were previously connected are not affected;
* If a node is deleted, arcs that were previously connected are deleted as well;
* If the geometry of an arc is modified, the new geometry should also connect two separate existing nodes.
* If a node is moved to a new position, geometry of the connected arcs is updated accordingly.

#EPA SWMM

The graphical user interface of EPA SWMM provides two ways to create a new conduit:

1. It is possible to draw a new conduit on the map. In this case the inlet node, outlet node and direction on how the conduit is drawn. These conduits can either be straight lines or contain additional vertices.
2. The other way around is to usting the "Add new" button. Using this approach, a conduit is drawn as a straight line between the last two junctions that have been drawn.

In both cases, an ArcID is automatically generated using an autoincrementor, with the prefixes and increment supplied in the project defaults (see [Episode 2: Project Setup](/blog/2014/09/20/swmm-giswater-tutorial-2-project-setup/)). It is possible to replace this automatically generated ArcID with your own value, yet each node should have an unique ID. This constrained is enforced by the software.

Double-clicking on a conduit opens it's attribute form in which the attributes can be modified. elected reaches can be removed by pressing the "Delete" key on your keyboard, or by using the "Delete object" button next to the "Add new" button. Pressing the right mouse button on a conduit, opens a context menu with the following options:

* Copy / paste: transfer attributes from one conduit to another;
* Delete: delete the conduit;
* Reverse: reverse the direction of the conduit (i.e. exchange inlet node and outlet node properties);
* Convert to: convert the object type to one of the other object types that can form an arc (pump, orifice, weir & outlet);
* Vertices: start editing the vertices of the conduit;
* Properties: open the attribute form for the conduit.

![SWMM_create_conduit](/images/SWMM_create_conduit.png "Creating a conduit in EPA SWMM.")

The inlet node and outlet node of a conduit can only be changed using the attribute form. If one of these values is changed, the geometry of the conduit is updated accordingly. If the inlet node is changed, the segment that connects the original inlet node with the second vertex (second-to-last for the outlet node) is replaced with a straight segment from this vertex to the new inlet node.

#GISWATER: QGIS AS FRONTDOOR

The Giswater equivalent of drawing a conduit in EPA SWMM directly, would be to draw a new feature in in the conduit layer of the corresponding GIS-project. However, whereas in EPA SWMM the cross-sectional geometry and roughness coefficient are attributes of each reach, GISWATER uses a different approach. GISWATER is using lookup tables for the profile definitions and materials (with their manning roughness coefficient as an attribute). The profile definition and material are not mandatory attributes of a conduit, yet conduits without a cross-section geometry do not make sense. Therefore, we need at least one profile definition and material definition to choose before we can create a conduit.

###Material & pipe profile definitions
Material and profile definitions could be created and modified by editing the administrative tables in QGIS or by executing SQL-statements. The developers of GISWATER have been so kind to provide a functionality for managing material (**Data** :fa-long-arrow-right: **Materials catalog**) and profile definitions (**Data** :fa-long-arrow-right: **Arc catalog**).

Using these catalogs to manage material definitions is straight-forward[^cat_mat].
Only thing to only thing is one has to realize that "n" is the Manning's roughness coefficient. For profile definitions however, we have an issue: how do we know the meaning of the editable fields? When a shape is selected in th cross-section editor of EPA SWMM, an appropriate set of edit fields appears for describing the dimensions of that shape. However, with GISWATER, only the field names of the underlying database fields are visible as labels. With names like "Geom1", "Geom2", "Geom3" & "Geom4", this does not provide much help. Only way I managed to create correct profiles is to create the profiles in the EPA SWMM interface and reverse engineer the meaning of the parameters for the different shapes from the resulting INP-file.

![Giswater_cat_arc](/images/Giswater_cat_arc.png "Arc catalogue in GISWATER.")

###Drawing conduits

The drawing process for the conduits is very similar to the process described for [junctions](/blog/2014/10/09/swmm-giswater-tutorial-3-creating-junctions).

![QGIS_create_conduits](/images/QGIS_create_conduits.png "Creating a conduit in QGIS.")

Notable differences are:

* The conduits are directional lines. An arrow is showing the direction on the map;
* Material definitions and profile definitions have to be created in the corresponding lookup tables;
* Whereas junctions can be located freely, conduits should always connect two separate existing nodes. If this requirement is not met, trying to save the conduit will result in a commit error.

![QGIS_conduit_commit_error](/images/QGIS_conduit_commit_error.png "Commit error for unconnected arc.")

#GISWATER: SQL AS BACKDOOR
The same recipe as used for the junctions, will also work for the conduits. The following python code generates insert statements for 3 conduits that connect the junctions that were placed in a strictly random street somewhere in the east of the Netherlands during [Episode 3: Creating Junctions](/blog/2014/10/09/swmm-giswater-tutorial-3-creating-junctions):

```python
import ppygis
import psycopg2

SRID = 28992
schema = 'tutorial'
junction_view = 'v_inp_edit_junction'
junction_fields = '(node_id, top_elev, ymax, y0, ysur, apond, sector_id, the_geom)'
junction_query = r'INSERT INTO "{0}"."{1}" {2} VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'.format(schema, junction_view, junction_fields)
conduit_view = 'v_inp_edit_conduit'
conduit_fields = '(arc_id, z1, z2, arccat_id, matcat_id, barrels, culvert, kentry, kexit, kavg, flap, q0, qmax, sector_id, the_geom)'
conduit_query = r'INSERT INTO "{0}"."{1}" {2} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s);'.format(schema, conduit_view, conduit_fields)


class Junction():
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


class Conduit():
    '''
    This is a conduit
    '''
    def __init__(self,ArcID,StartNode,EndNode,InletOffset,OutletOffset):
        '''
        Constructor
        '''
        self.ArcID = ArcID
        self.InletOffset = InletOffset
        self.OutletOffset = OutletOffset
        self.ArcCat_ID = "ROUND500"    # Profile definition created previously
        self.MatCat_ID = "CONCRETE"    # Material created previously
        self.Barrels = 1               # 1 for now, to be examined later
        self.Culvert = None            # ignore for now, to be examined later
        self.Kentry = 0                # 0 for now, to be examined later
        self.Kexit = 0                 # 0 for now, to be examined later
        self.Kavg = 0                  # 0 for now, to be examined later
        self.Flap = 'NO'               # NO for now, to be examined later
        self.Q0 = 0                    # 0 for now, to be examined later
        self.Qmax = 0                  # 0 for now, to be examined later
        self.SectorID = None           # ignore for now, to be examined later
        self.StartNode = StartNode
        self.EndNode = EndNode
        self.Geometry = ppygis.LineString((self.StartNode.Geometry, \
                                          self.EndNode.Geometry,), srid=SRID)

    @property
    def InsertValues(self):
        return (self.ArcID, self.InletOffset, self.OutletOffset, \
                self.ArcCat_ID, self.MatCat_ID, self.Barrels, \
                self.Culvert, self.Kentry, self.Kexit, self.Kavg, \
                self.Flap, self.Q0, self.Qmax, self.SectorID, \
                self.Geometry.write_ewkb())


conn = psycopg2.connect('dbname=giswater_ddb user=postgres port=5431')
cur = conn.cursor()

# Here you can put the logic that reads out the files/databases
# that contain locations and/or attributes of your objects
node_ids = ['J1', 'J2', 'J3', 'J4']
x = [255320.35, 255347.98, 255365.84, 255375.21]
y = [472276.25, 472302.63, 472319.22, 472328.19]
z = [33.11, 33.03, 32.76, 32.89]
arc_ids = ['C1','C2','C3']
junction_list = []


# insert queries for the junctions
for i in xrange(4):
    example_junction = Junction(node_ids[i], x[i], y[i], z[i])
    junction_values =  example_junction.InsertValues

    # and write the resulting query to a file, not stdout
    print cur.mogrify(junction_query, junction_values)
    junction_list.append(example_junction)


# insert queries for the conduits
for i in xrange(3):
    start_node = junction_list[i]
    end_node = junction_list[i+1]
    inlet_offset = 0.5
    outlet_offset = 0.5
    example_conduit = Conduit(arc_ids[i], start_node, end_node, \
                              inlet_offset, outlet_offset)
    conduit_values =  example_conduit.InsertValues

    # and write the resulting query to a file, not stdout
    print cur.mogrify(conduit_query, conduit_values)


conn.close()

```

Which results in the following SQL-statement with some very long lines:

```SQL
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J1', 33.11, 0, 0, 0, 0, None, '010100002040710000cdccccccc22a0f410000000051d31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J2', 33.03, 0, 0, 0, 0, None, '010100002040710000713d0ad79f2b0f4152b81e85bad31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J3', 32.76, 0, 0, 0, 0, None, '01010000204071000085eb51b82e2c0f4114ae47e1fcd31c41');
INSERT INTO "tutorial"."v_inp_edit_junction" VALUES ('J4', 32.89, 0, 0, 0, 0, None, '010100002040710000e17a14ae792c0f41295c8fc220d41c41');

INSERT INTO "tutorial"."v_inp_edit_conduit" (arc_id, z1, z2, arccat_id, matcat_id, barrels, culvert, kentry, kexit, kavg, flap, q0, qmax, sector_id, the_geom) VALUES ('C1', 0.5, 0.5, 'ROUND500', 'CONCRETE', 1, NULL, 0, 0, 0, 'NO', 0,0, NULL, '01020000204071000002000000cdccccccc22a0f410000000051d31c41713d0ad79f2b0f4152b81e85bad31c41');
INSERT INTO "tutorial"."v_inp_edit_conduit" (arc_id, z1, z2, arccat_id, matcat_id, barrels, culvert, kentry, kexit, kavg, flap, q0, qmax, sector_id, the_geom) VALUES ('C2', 0.5, 0.5, 'ROUND500', 'CONCRETE', 1, NULL, 0, 0, 0, 'NO', 0,0, NULL, '01020000204071000002000000713d0ad79f2b0f4152b81e85bad31c4185eb51b82e2c0f4114ae47e1fcd31c41');
INSERT INTO "tutorial"."v_inp_edit_conduit" (arc_id, z1, z2, arccat_id, matcat_id, barrels, culvert, kentry, kexit, kavg, flap, q0, qmax, sector_id, the_geom) VALUES ('C3', 0.5, 0.5, 'ROUND500', 'CONCRETE', 1, NULL, 0, 0, 0, 'NO', 0,0, NULL, '0102000020407100000200000085eb51b82e2c0f4114ae47e1fcd31c41e17a14ae792c0f41295c8fc220d41c41');

```

#CONCLUSIONS:

Although it took a while to grasp the behavior that was going on, the use of Arc-Node topology makes sense for an urban drainage network and does a good job maintaining network integrity.
GISWATER mimics the network behavior of plain SWMM really well. The addition of directional arrows communicates that the objects form a network and provide insight in the direction of the arcs. However, without proper instruction, this may result in confusion when users are under the impression that the arrows are showing hydraulic direction.

GISWATER introduces a system of material definitions and profile definitions for the reaches. This approach appeals to me conceptually. However, in its current form, the profile catalog is far from user-friendly: the meaning of the input parameters is unclear for the various shapes.

[^cat_mat]: Although there seems to be a little bug in the version of GISWATER I'm running (v1,0.186), since trying to save a material resulted in the following message: "The column name roughness was not found in this ResultSet". Adding records to the material definition table from QGIS worked correctly.