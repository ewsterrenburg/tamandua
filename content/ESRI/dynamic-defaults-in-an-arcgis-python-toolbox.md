date: 2015-03-24
author: Erwin Sterrenburg
title: Dynamic Default Attributes in an ArcGIS Python Toolbox
slug: dynamic-default-attributes-in-arcgis-python-toolbox
tags: Python, ESRI, ArcGIS
summary: This blogpost contains an overview of my struggles trying to create an ArcGIS python toolbox with dynamic default attributes: i.e. the values for these parameters would remain (slight variatons of) the same value for a long time. However, sometimes one or more parameter values would change drastically, which would make the newly supplied value the new default value.

Once upon a time, on a computer not that far away, there was a ArcGIS python toolbox. This python toolbox contained a tool with a set of parameters. The values for these parameters would remain (slight variatons of) the same value for a long time. However, sometimes one or more parameter values would change drastically, which would make the newly supplied value the new default value.

This blogpost contains an overview of my struggles trying to enforce this behavior. The original tool uses a logfile from which the parameter values are read during initialization and to which the parameter values are written when the tool is executed. In this example I will simply use the current time as my "external datasource". The tool will read out the current time, use it as a default value for its only parameter and print the value of this parameter to the message dialog. Using this approach, I can more precisely identify what is happening and an what moment exactly the default value of the tool is being set.

#getParameterInfo
I expected an ArcGIS tool to be constructed when the tool is being opened by a user and to be destroyed after the tool has either been run or has been cancelled by the user. This would imply that the parameters, so my first attempt at "timetool.pyt" looked as follows:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class TimeTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Present time"
        self.description = "Prints a message with the present time"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        present_time = arcpy.Parameter(
            displayName="Present time",
            name="present_time",
            datatype="String",
            parameterType="Required",
            direction="Input"
            )

        # supply a start value for the parameter as suggested value
        # during the initialization of the tool:
        now = datetime.datetime.now()
        present_time.value=unicode(now)

        params = [present_time]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.AddMessage(parameters[0].value)
        return

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox
            is the name of the .pyt file)."""
        self.label = "TimeTool_Toolbox"
        self.alias = "Toolbox with TimeTool"
        self.tools = [TimeTool]
```

The first time I started this tool, it was working as intended. Yet, some further testing showed that its behavior didn't correspond to what it should be:

- **Open the tool, cancel execution, then restart:** our entry box is populated with the value we received when we started the tool for the first time;
- **Running the tool with default input, then restart:** our entry box is populated with the value we received when we started the tool for the first time;
- **Running the tool with modified input value, then restart:** during the first run our modified value is being printed, during the second run our entry box is still populated with the value we received when we started the tool for the first time;
- **Opening an entirely new MXD**: even after opening a new MXD, our entry box is still populated with the value we received when we started the tool for the first time.

A pattern is emerging: the default value of the parameter is set during the first time the tool is being opened the ArcMAP session. The tool appears to be constructed during the first time it is being opened, then kept in memory for future use.

#updateParameters
Conclusion is that we need to find another way capture the event of an user starting up the tool. Unfortunately, the [ArcGIS help pages](http://resources.arcgis.com/en/help/main/10.2/index.html#//001500000024000000) do not provide us with a "InitializeParameters" method. It does however give us the "updateParameters" method, which is being called whenever a parameter has been changed. Apparently one or more parameters do change when a tool is being opened, since execution of the method is triggered when opening a tool.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class TimeTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Present time"
        self.description = "Prints a message with the present time"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        present_time = arcpy.Parameter(
            displayName="Present time",
            name="present_time",
            datatype="String",
            parameterType="Required",
            direction="Input"
            )

        params = [present_time]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        # supply a start value for the parameter as suggested value
        # when the parameter does not yet have a value:
        if not parameters[0].value:
            now = datetime.datetime.now()
            parameters[0].value = unicode(now)
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.AddMessage(parameters[0].value)
        return

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox
            is the name of the .pyt file)."""
        self.label = "TimeTool_Toolbox"
        self.alias = "Toolbox with TimeTool"
        self.tools = [TimeTool]
```
Testing the behavior of the tool now gives the following results:

- **Open the tool, cancel execution, then restart:** our entry box is populated with a new value when we restart the tool;
- **Running the tool with default input, then restart:** our entry box is populated with a new value when we restart the tool;
- **Running the tool with modified input value, then restart:** during the first run our modified value is being printed, during the second run our entry box is populated with a new value;
- **Opening an entirely new MXD**: our entry box is populated with a new value when we restart the tool;
- **Open the tool, delete the contents of our entry box**: our entry box is populated with a new value.

Again, a pattern is emerging: the default value of the parameter is set evertime the users opens the tool. For our original usecase, this approach will do the trick. It still is some kind of work-around though, and has the following drawbacks:

- Deleting the contents from the entry box will result in the entry box being repopulated;
- This approach will only work for required parameters. If it is used for optional parameters, the parameter will be given the value of our suggestion if kept blank.

Using a precondition with a sensible combination of required parameters should be enough to soothen these drawbacks and make the tool usable. A hidden quirk will still persist though, if a user would delete the values for the chosen set of parameters :fa-frown-o:.

In an attempt to remove this quirk, I have been trying to give the tool an extra attribute "self.initialized" and use this attribute as my precondition. Using this approach did not succeed due to the following issues:

1. We might be able to attribute to False in the execution method of the tool. But how-to how to set this to False on cancel?
2. Modifying a tool's attributes outside the initialization method does not seem to work.

#Conclusion
I have not been able to find a way to capture the moment at which the parameters of the tool are being initialized. The updateParameters method does provide sufficient possibilities to come up with an usable work-around.
