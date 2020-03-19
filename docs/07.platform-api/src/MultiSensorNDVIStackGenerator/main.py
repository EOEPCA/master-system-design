
import eoepca

# Connect to primary platform - e.g. when running on own desktop
primaryPlatform = eoepca.platform("http://primary.platform.eo") # <1>
primaryPlatform = primaryPlatform.authenticate("bob@home.org", "<<MY-API-KEY>>") # <2>
# Or, use the 'local' hosting platform - e.g. when running in 'cloud' platform
primaryPlatform = eoepca.platform().authenticate("bob@home.org", "<<MY-API-KEY>>") # <2> <3>

# Init supporting platforms
platA = eoepca.platform("http://platform-a.eo") # <1> <4>
platB = eoepca.platform("http://platform-b.eo") # <1> <4>
platC = eoepca.platform("http://platform-c.eo") # <1> <4>

# Specify extent
extent = { "bbox": [ -0.489, 51.28, 0.236, 51.686 ], "time": [ "2018-01-01", "2018-12-31" ] }

# Specify processes
coverage1 = platA.collection("PLAT_A_DATA").coverage(extent) # <5>
proc1 = coverage1.process("MultiSensorNDVI") # <6>
proc2 = platB.collection("PLAT_B_DATA").coverage(extent).process("MultiSensorNDVI") # <5> <6>
proc3 = platC.collection("PLAT_C_DATA").coverage(extent).process("MultiSensorNDVI") # <5> <6>

# Specify workflow
workflow = primaryPlatform.parallel([proc1, proc2, proc3]).process("NDVIStacker") # <7>

# Get result - initiates 'lazy' execution
result = workflow.retrieve(format="geotiff", options={}) # <8>
print(result)
