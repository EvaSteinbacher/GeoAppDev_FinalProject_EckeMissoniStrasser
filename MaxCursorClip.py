import arcpy

#define inputs: feature layer and the field in the table that should be selected
#set variables 
input = arcpy.GetParameterAsText (0) #features to be clipped
clip_feature = arcpy.GetParameterAsText (1) #The features used to clip the input features
table_field = arcpy.GetParameterAsText (2) #table field of the clip feature can be chosen 
selection_type = arcpy.GetParameterAsText (3) #Determines the selection type
output_feature_class = arcpy.GetParameterAsText (4) #output feature class to be created

# search cursor that looks for the maximum value in the field of the table of the feature layer
with arcpy.da.SearchCursor(clip_feature, table_field) as cursor:
    max(cursor)

maxvalue = max(cursor)

maxvalue_str = ''.join(map(str, maxvalue)) #converts the list value into string

#get the derived maximum value as message in Arcgis Pro
arcpy.AddMessage("Max value of " + table_field + " = "  + maxvalue_str)

# Create field name with the proper delimiters
whereclause = """{} = {}""".format(arcpy.AddFieldDelimiters(clip_feature, table_field), maxvalue_str)

#implementation of the selection with error handling 
try:
    arcpy.SelectLayerByAttribute_management(clip_feature, selection_type, whereclause)
    
except arcpy.ExecuteError:
    arcpy.AddWarning("Executed without selection! The table field you have chosen is empty.")

xy_tolerance = ""

#implementation of the clipping
arcpy.Clip_analysis(input, clip_feature, output_feature_class, xy_tolerance) 

