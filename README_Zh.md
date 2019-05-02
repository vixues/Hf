Hf
===
/[中文](README_Zh.md)/[English](README.md)/

Python脚本，用来处理ICP-MS数据。

__内容:__

[data](data):测试数据

[reference](reference):excel文件，完成同样任务

[gui.py](gui.py): 构建用户主界面

[Napture.py](Napture.py): 从 Neptune Plus™ .exp 文件中读取数据
* 仪器型号：Neptune Plus™ High Resolution Multicollector ICP-MS
* 文件类型：*.exp

[calculation.py](calculation.py): 完成主要计算任务.

__依赖:__

1) Python 3.4+ 
* Works on Linux, Windows, Mac OSX, BSD

__使用方法:__

    python main.py

数据处理方法详见reference文件夹中的excel文件，参考论文如下。
- Tsuyoshi Iizuka, Takafumi Hirata, Improvements of precision and accuracy in in situ Hf isotope microanalysis of zircon using the laser ablation-MC-ICPMS technique, Chemical Geology, Volume 220, Issues 1–2, 2005, Pages 121-137, ISSN 0009-2541. [https://doi.org/10.1016/j.chemgeo.2005.03.010](https://doi.org/10.1016/j.chemgeo.2005.03.010)
- Chu, N.C., Taylor, R.N., Chavagnac, V., Nesbitt, R.W., Boella, R.M., Milton, J.A., Germain,
C.R., Bayon, G., Burton, K., 2002. Hf isotope ratio analysis using multi-collector inductively coupled plasma mass spectrometry: An evaluation of isobaric interference corrections. Journal of Analytical Atomic Spectrometry 17, 1567–1574. [http://dx.doi.org/10.1039/B206707B](http://dx.doi.org/10.1039/B206707B)

更多型号支持还在开发当中，请联系 [yqc@pku.edu.cn](yqc@pku.edu.cn) 获得更多信息。

在新的一版中，Hf和Sr的处理程序被统一整合到Isotop软件中，具体请访问 [Isotope]()。

谢谢！