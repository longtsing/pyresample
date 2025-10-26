几何定义
====================

:mod:`pyresample.geometry` 模块包含用于描述使用点或像素网格的不同地理区域的类。一些类表示由均匀间隔/大小的像素组成的地理区域，其他类处理区域由非均匀像素描述的情况。描述区域的最佳对象取决于用例和已知的信息。pyresample 中可用的不同类如下所述。

请注意，提供给 :mod:`pyresample.geometry` 类的所有经度和纬度必须以度为单位。此外，经度必须在 [-180;+180[ 有效范围内。

.. versionchanged:: 1.8.0

    几何对象不再检查提供的经度和纬度坐标的有效性以提高性能。经度数组预期在 -180 到 180 度之间，纬度在 -90 到 90 度之间。这也适用于在初始化时提供经度和纬度数组的所有几何定义。使用 :func:`~pyresample.utils.check_and_wrap` 预处理您的数组。

.. _area-definitions:

AreaDefinition
--------------

:class:`~pyresample.geometry.AreaDefinition` 或 ``area`` 是在 pyresample 中指定均匀间隔地理区域的主要方式。它也是唯一理解地理投影的几何对象之一。区域使用 :doc:`PROJ.4 <proj:index>` 方法来描述投影坐标参考系统（CRS）。如果区域的投影不是由经度/纬度坐标描述的，那么它通常以米为单位的 X/Y 坐标描述。有关投影和坐标参考系统的更多信息，请参阅 :doc:`PROJ.4 <proj:index>` 文档。

初始化区域需要以下参数：

* **area_id**：区域的 ID
* **description**：描述
* **proj_id**：投影的 ID（正在弃用）
* **projection**：Proj4 参数，作为字典或字符串
* **width**：网格列数
* **height**：网格行数
* **area_extent**：(lower_left_x, lower_left_y, upper_right_x, upper_right_y)

其中

* **lower_left_x**：左下角像素的左下角的投影 x 坐标
* **lower_left_y**：左下角像素的左下角的投影 y 坐标
* **upper_right_x**：右上角像素的右上角的投影 x 坐标
* **upper_right_y**：右上角像素的右上角的投影 y 坐标

示例：

.. doctest::

 >>> from pyresample.geometry import AreaDefinition
 >>> area_id = 'ease_sh'
 >>> description = 'Antarctic EASE grid'
 >>> proj_id = 'ease_sh'
 >>> projection = {'proj': 'laea', 'lat_0': -90, 'lon_0': 0, 'a': 6371228.0, 'units': 'm'}
 >>> width = 425
 >>> height = 425
 >>> area_extent = (-5326849.0625, -5326849.0625, 5326849.0625, 5326849.0625)
 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)
 >>> area_def
 Area ID: ease_sh
 Description: Antarctic EASE grid
 Projection ID: ease_sh
 Projection: {'R': '6371228', 'lat_0': '-90', 'lon_0': '0', 'no_defs': 'None', 'proj': 'laea', 'type': 'crs', 'units': 'm', 'x_0': '0', 'y_0': '0'}
 Number of columns: 425
 Number of rows: 425
 Area extent: (-5326849.0625, -5326849.0625, 5326849.0625, 5326849.0625)

您也可以使用 PROJ.4 字符串指定投影

.. doctest::

 >>> projection = '+proj=laea +lat_0=-90 +lon_0=0 +a=6371228.0 +units=m'
 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)

或 `EPSG 代码 <https://www.epsg-registry.org/>`_：

.. doctest::

 >>> projection = '+init=EPSG:3409'  # 使用 pyproj 2.0+ 时使用 'EPSG:3409'
 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)

.. note::

  使用 pyproj 2.0+ 时，请使用新的 ``'EPSG:XXXX'`` 语法，因为旧的 ``'+init=EPSG:XXXX'`` 不再受支持。

如果您不了解所描述区域的所有信息，创建 ``AreaDefinition`` 可能会很复杂。Pyresample 提供了多个实用程序来创建区域以及将它们存储在磁盘上以供重复使用。有关更多信息，请参阅 :doc:`geometry_utils` 文档。

GridDefinition
--------------

如果已知区域的经度和纬度值，可以通过使用 :class:`GridDefinition <pyresample.geometry.GridDefinition>` 对象来跳过 ``AreaDefinition`` 的复杂性。请注意，尽管网格定义更容易定义，但对于几乎所有操作，它们的内存和 CPU 使用量都要高得多。传递给 ``GridDefinition`` 的经度和纬度数组预期是均匀间隔的。如果不是，则应使用 ``SwathDefinition``（见下文）。

.. doctest::

 >>> import numpy as np
 >>> from pyresample.geometry import GridDefinition
 >>> lons = np.ones((100, 100))
 >>> lats = np.ones((100, 100))
 >>> grid_def = GridDefinition(lons=lons, lats=lats)

SwathDefinition
---------------

条带由其代表的像素的经度和纬度坐标定义。坐标代表每个像素的中心点。条带不对像素大小和间距的均匀性做任何假设。这意味着使用它们的操作可能需要更长时间，但也能得到准确的表示。

.. doctest::

 >>> import numpy as np
 >>> from pyresample.geometry import SwathDefinition
 >>> lons = np.ones((500, 20))
 >>> lats = np.ones((500, 20))
 >>> swath_def = SwathDefinition(lons=lons, lats=lats)

如果两个条带的列数匹配，可以连接它们

.. doctest::

 >>> lons1 = np.ones((500, 20))
 >>> lats1 = np.ones((500, 20))
 >>> swath_def1 = SwathDefinition(lons=lons1, lats=lats1)
 >>> lons2 = np.ones((300, 20))
 >>> lats2 = np.ones((300, 20))
 >>> swath_def2 = SwathDefinition(lons=lons2, lats=lats2)
 >>> swath_def3 = swath_def1.concatenate(swath_def2)

地理坐标和边界
-------------------------------------

所有几何定义对象都提供对经度和纬度坐标的访问。``get_lonlats()`` 方法可用于获取此数据，并将执行获取坐标所需的任何额外计算。

:class:`AreaDefinition <pyresample.geometry.AreaDefinition>` 通过 **projection_x_coords** 和 **projection_y_coords** 属性公开完整的投影坐标集。请注意，对于经纬度投影（`+proj=latlong`），这些坐标将以经度/纬度度为单位，其中 **projection_x_coords** 将是经度，**projection_y_coords** 将是纬度。

.. versionchanged:: 1.5.1

    将 `proj_x_coords` 重命名为 `projection_x_coords`，将 `proj_y_coords` 重命名为 `projection_y_coords`。

获取经度和纬度数组：

.. doctest::

 >>> area_id = 'ease_sh'
 >>> description = 'Antarctic EASE grid'
 >>> proj_id = 'ease_sh'
 >>> projection = '+proj=laea +lat_0=-90 +lon_0=0 +a=6371228.0 +units=m'
 >>> width = 425
 >>> height = 425
 >>> area_extent = (-5326849.0625,-5326849.0625,5326849.0625,5326849.0625)
 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)
 >>> lons, lats = area_def.get_lonlats()

获取地心 X、Y、Z 坐标：

.. doctest::

 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)
 >>> cart_subset = area_def.get_cartesian_coords()[100:200, 350:]

如果只需要投影坐标的 1D 范围，可以使用地理坐标的 **projection_x_coord** 或 **projection_y_coords** 属性提取它

.. doctest::

 >>> area_def = AreaDefinition(area_id, description, proj_id, projection,
 ...                           width, height, area_extent)
 >>> proj_x_range = area_def.projection_x_coords
