#Create and display a table
#Creating a table from a script is easier than plots as 
# there is less to do. Like plots, you retrieve the data, 
# add the data to a Vector, create a table and set the data, 
# and then show the table.
from hec.script import Plot, MessageBox
from hec.dataTable import HecDataTableFrame
from hec.heclib.dss import HecDss
import java
import sys
#  Open the file and get the data
try:  
  dssFile = HecDss.open(sys.argv[1] + "\\sample.dss", "10MAR2006 2400, 09APR2006 2400")
  precip = dssFile.get("/AMERICAN/FOLSOM/PRECIP-BASIN/01JAN2006/1DAY/OBS/")
  stor = dssFile.get("/AMERICAN/FOLSOM/ STOR-RES EOP/01JAN2006/1DAY/OBS/")
  topcon = dssFile.get("/AMERICAN/FOLSOM/TOP CON STOR/01JAN2006/1DAY/OBS/")
  sagca = dssFile.get("/AMERICAN/FOLSOM-SAGCA/TOP CON STOR/01JAN2006/1DAY/OBS/")
  inflow = dssFile.get("/AMERICAN/FOLSOM/FLOW-RES IN/01JAN2006/1DAY/OBS/")
  outflow = dssFile.get("/AMERICAN/FOLSOM/FLOW-RES OUT/01JAN2006/1DAY/OBS/")
except java.lang.Exception, e :
  #  Take care of any missing data or errors
   MessageBox.showError(e.getMessage(), "Error reading data")


table = HecDataTableFrame.newTable("Folsom - American River Basin")

#  Add Data
table.addData(precip)
table.addData(stor)
table.addData(topcon)
table.addData(sagca)
table.addData(inflow)
table.addData(outflow)

table.showTable()
