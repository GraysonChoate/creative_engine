var proj = app.newProject();
var comp = proj.items.addComp("CE_Test", 1920, 1080, 1, 3, 30);
comp.layers.addSolid([0.08, 0.09, 0.11], "BG", 1920, 1080, 1);
var t = comp.layers.addText("CE TEST");
var tp = t.property("Source Text"); var td = tp.value; td.fontSize = 160; td.fillColor = [1, 1, 1]; tp.setValue(td);
t.property("Transform").property("Position").setValue([760, 600]);
var sc = t.property("Transform").property("Scale");
sc.setValueAtTime(0, [80, 80]); sc.setValueAtTime(3, [120, 120]);
proj.save(new File("/PATH/TO/test.aep"));
