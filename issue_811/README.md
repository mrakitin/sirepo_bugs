Original Sirepo issue: https://github.com/radiasoft/sirepo/issues/811

mrakitin/SRW issue: https://github.com/mrakitin/SRW/issues/38

----
NaN values in the `.dat` file:
```
#Intensity [ph/s/.1%bw/mm^2] (C-aligned, inner loop is vs Photon Energy, outer loop vs Vertical Position)
#695.5 #Initial Photon Energy [eV]
#695.5 #Final Photon Energy [eV]
#1 #Number of points vs Photon Energy
#-0.00030591359401204175 #Initial Horizontal Position [m]
#0.0003029721171465414 #Final Horizontal Position [m]
#208 #Number of points vs Horizontal Position
#-0.0005434927538367033 #Initial Vertical Position [m]
#0.0005419830517427124 #Final Vertical Position [m]
#720 #Number of points vs Vertical Position
#1 #Number of components
 0.0
 0.0
 nan
 nan
 nan
.....
```
