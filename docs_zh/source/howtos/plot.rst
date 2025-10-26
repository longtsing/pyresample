绘图
====

本文档描述如何使用 pyresample 创建地图和可视化。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

使用 Cartopy 绘图
----------------------

Pyresample 可以与 Cartopy 一起使用来创建地图。

基本绘图
^^^^^^^^^^^

创建一个简单的地图：

.. code-block:: python

    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.coastlines()
    plt.show()

绘制重采样数据
^^^^^^^^^^^^^^^^^^^^^^

在地图上显示重采样的数据。
