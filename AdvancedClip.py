# Import system modules
import arcpy

# Set local variables
in_features = arcpy.GetParameterAsText(0) #features to be clipped
clip_features = arcpy.GetParameterAsText(1) #The features used to clip the input features
selection_type = arcpy.GetParameterAsText(2) #Determines the selection type 
sql_expression = arcpy.GetParameterAsText(3) #SQL expression, to select specific features by attributes 
out_feature_class = arcpy.GetParameterAsText(4) #defines name and path where the output feature class should be created
tol_value = arcpy.GetParameterAsText(5) #defines the xy tolerance

arcpy.SelectLayerByAttribute_management(clip_features, selection_type, sql_expression) #implementation of the selection

xy_tolerance = tol_value

arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance) #implementation of the clipping operation

#Prints the expression as message in ArcGIS Pro, when running the tool 
if sql_expression == "":
    arcpy.AddMessage("Finished clipping without using an expression")
    
else:
    arcpy.AddMessage("Finished clipping using the expression(s): " + sql_expression)


        
