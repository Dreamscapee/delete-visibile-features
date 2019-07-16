mapcanvas = iface.mapCanvas()
rect = mapcanvas.extent()
requests = QgsFeatureRequest().setFilterRect(rect)
layers = QgsProject.instance().mapLayers().values()

for l in layers:
    if l.type() == QgsMapLayer.VectorLayer:
        pr = l.dataProvider()
        l.startEditing()
        for f in l.getFeatures(requests):
            l.deleteFeature(f.id())
        l.commitChanges()
   