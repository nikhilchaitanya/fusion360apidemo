import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    vector1 = 1
    try:
        if vector1==0 :
            app = adsk.core.Application.get()
            ui = app.userInterface
            
            # Create a document.
            doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    
            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)

            # Get the root component of the active design
            rootComp = design.rootComponent
                    
            # Get extrude features
            extrudes = rootComp.features.extrudeFeatures

            # Important to Note: Default units in Fusion 360 API is cm and it cannot be changed to mm

            # Create sketch     
            sketches = rootComp.sketches   
            sketch = sketches.add(rootComp.xYConstructionPlane)
            sketchCircles = sketch.sketchCurves.sketchCircles
            centerPoint = adsk.core.Point3D.create(0, 0, 0)
            circle = sketchCircles.addByCenterRadius(centerPoint, 10.0)
            
            # Get the profile defined by the circle
            prof = sketch.profiles.item(0)
            
            
            # Extrude Sample 1: A simple way of creating typical extrusions (extrusion that goes from the profile plane the specified distance).
            # Define a distance extent of 5 cm
            distance = adsk.core.ValueInput.createByReal(1.0)
            extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)        
            # Get the extrusion body
            body1 = extrude1.bodies.item(0)
            body1.name = "simple"

            # Get the state of the extrusion
            health = extrude1.healthState
            if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
                message = extrude1.errorOrWarningMessage
            
            # Get the state of timeline object
            timeline = design.timeline
            timelineObj = timeline.item(timeline.count - 1);
            health = timelineObj.healthState
            message = timelineObj.errorOrWarningMessage

        else:
            app = adsk.core.Application.get()
            ui = app.userInterface
            
            # Create a document.
            doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    
            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)

            # Get the root component of the active design
            rootComp = design.rootComponent
                    
            # Get extrude features
            extrudes = rootComp.features.extrudeFeatures

            # Important to Note: Default units in Fusion 360 API is cm and it cannot be changed to mm

            # Create sketch     
            sketches = rootComp.sketches   
            sketch = sketches.add(rootComp.xZConstructionPlane)
            sketchCircles = sketch.sketchCurves.sketchCircles
            centerPoint = adsk.core.Point3D.create(0, 0, 0)
            circle = sketchCircles.addByCenterRadius(centerPoint, 5.0)
            
            # Get the profile defined by the circle
            prof = sketch.profiles.item(0)
            
            
            # Extrude Sample 1: A simple way of creating typical extrusions (extrusion that goes from the profile plane the specified distance).
            # Define a distance extent of 5 cm
            distance = adsk.core.ValueInput.createByReal(10.0)
            extrude1 = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)        
            # Get the extrusion body
            body1 = extrude1.bodies.item(0)
            body1.name = "simple"

            # Get the state of the extrusion
            health = extrude1.healthState
            if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
                message = extrude1.errorOrWarningMessage
            
            # Get the state of timeline object
            timeline = design.timeline
            timelineObj = timeline.item(timeline.count - 1);
            health = timelineObj.healthState
            message = timelineObj.errorOrWarningMessage
        
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
