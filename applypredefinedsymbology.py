

# import system modules
import arcpy

shape = arcpy.GetParameterAsText(0)

#  Describe evaluates the shape type (polyline, polygon, point) of the users input data and determines which symbology parameters are appropriate
desc = arcpy.Describe(shape)                                

##########
# If user input is a Point Feature Layer, the subsequent symbology settings will be applied: 
if desc.shapeType == "Point":
    p = arcpy.mp.ArcGISProject('current')                   # goes to mp. library and accesses the current project
    m = p.listMaps('Map')[0]                                # gets the first map

    lyr = m.listLayers(shape)[0]                            # gets the first layer 
    sym = lyr.symbology

    sym.renderer.symbol.applySymbolFromGallery("Circle 3")  # applies the symbol "Circle 3" from the Format Point Symbol Gallery 
    sym.renderer.symbol.color = {'RGB' : [200, 161, 60, 80]}   # accesses the symbology of the above selected layer: golden color for circles (opacity 80 %)
    sym.renderer.symbol.size = 5                               # symbol size is set to 5pt
    lyr.symbology = sym                                     

    sym.renderer.symbol                                      # gets renderer when symbol variable is set

# If user input is a Polyline Feature Layer, the subsequent symbology settings will be applied:
elif desc.shapeType == "Polyline":
    p = arcpy.mp.ArcGISProject('current')                   
    m = p.listMaps('Map')[0]                                

    lyr = m.listLayers(shape)[0]                            
    sym = lyr.symbology                                
    sym.renderer.symbol.color = {'RGB' : [100, 100, 100, 100]}   # RGB colors are set to dark grey (opacity 100 %) 
    sym.renderer.symbol.size = 0.5                               # draws rather fine lines 
    lyr.symbology = sym                                     

    sym.renderer.symbol 

# If user input is a Polygon Feature Layer, the subsequent symbology settings will be applied: 
elif desc.shapeType == "Polygon":
    p = arcpy.mp.ArcGISProject('current')                   
    m = p.listMaps('Map')[0]                                

    lyr = m.listLayers(shape)[0]
    sym = lyr.symbology

    sym.renderer.symbol.color = {'RGB' : [27, 116, 167, 30]}         # defining color of polygons as blue with an opacity of 30 %
    sym.renderer.symbol.outlineColor = {'RGB' : [200, 200, 200, 50]} # defining outline color of polygon symbols as light grey (opacity 50 %)

    lyr.symbology = sym

    sym.renderer.symbol
    
else:
    print(shape)

    
##########    
    
# Sources used for the generation of the Symbology Code: 
        # ArcGIS Pro: Python - Describing data. Available under: http://pro.arcgis.com/en/pro-app/arcpy/get-started/describing-data.htm 
        # Esri Events: Map Automation in ArcGIS Pro. Available under: https://www.youtube.com/watch?v=oOcckhgd3Sk 
        # Esri GeoNet: Acpy "if", "elif", and "else" statement (ArcGIS Pro). Available under: https://community.esri.com/thread/206158-acpy-if-elif-and-else-statement-arcgis-pro