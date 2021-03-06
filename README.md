Hf
===
/[中文](README_Zh.md)/[English](README.md)/

Python Scripts for ICP-MS Hf data processing,
all code is released under an [MIT open-source license](LICENSE).

__CONTENTS:__

[data](data):Data for testing.

[reference](reference):Spreedsheet doing the same thing.

[gui.py](gui.py): Build the main user interface.

[Napture.py](Napture.py): Reading data from Neptune Plus™ .exp file.
* Model：Neptune Plus™ High Resolution Multicollector ICP-MS
* File type：*.exp

[calculation.py](calculation.py): Doing the calculation.

__DEPENDENCIES:__

1) Python 3.4+ 
* Works on Linux, Windows, Mac OSX, BSD

__USAGE:__

    python main.py

__REFERENCE:__

The formula used in this software can be found in the spreedsheet in the [reference](reference) folder,  more detailed analytical procedures were described in the papers listed below:
- Tsuyoshi Iizuka, Takafumi Hirata, Improvements of precision and accuracy in in situ Hf isotope microanalysis of zircon using the laser ablation-MC-ICPMS technique, Chemical Geology, Volume 220, Issues 1–2, 2005, Pages 121-137, ISSN 0009-2541. [https://doi.org/10.1016/j.chemgeo.2005.03.010](https://doi.org/10.1016/j.chemgeo.2005.03.010)
- Chu, N.C., Taylor, R.N., Chavagnac, V., Nesbitt, R.W., Boella, R.M., Milton, J.A., Germain,
C.R., Bayon, G., Burton, K., 2002. Hf isotope ratio analysis using multi-collector inductively coupled plasma mass spectrometry: An evaluation of isobaric interference corrections. Journal of Analytical Atomic Spectrometry 17, 1567–1574. [http://dx.doi.org/10.1039/B206707B](http://dx.doi.org/10.1039/B206707B)

__CONTACT:__

This software is still under development to support more models and file types. For more information, please contact [yqc@pku.edu.cn](yqc@pku.edu.cn).

__Note:__ In the latest version of this software, the Sr and the Hf programs are combined in the __Isotope__ software, for more infomation, please visit [Isotope]().

Enjoy!
