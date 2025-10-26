投影
===========

处理地理定位数据时，更复杂的主题之一是地理投影以及投影之间数据的转换或重采样。您可能还会看到投影被称为投影坐标参考系统（CRS）或仅仅是 CRS。以下文档可以看作是入门，但对于这个复杂的主题来说仍然相当有限。

Battersby [#]_ 的《地图投影》一书描述了地图投影：

.. code-block:: text

    地图投影是将角度（球形/椭圆）坐标转换为平面坐标的过程。所有地图投影都会在生成的平面坐标中引入失真（例如，对区域、角度、距离）。了解引入了什么、在哪里以及多少失真是空间计算和空间模式的视觉解释以及任何地图的一般美学的重要考虑因素。

空间投影描述了如何创建我们圆形 3D 地球的平面 2D 版本，这可能比我们数据使用的原始表示更容易使用或描述。

.. image:: http://gistbok.ucgis.org/sites/default/files/figure2-projections.png
   :width: 450px
   :target: http://gistbok.ucgis.org/bok-topics/map-projections

这些投影或坐标参考系统将包含诸如地球模型（基准面/椭球体）、参考或中心经度、参考或中心纬度以及用于在投影之间转换点的形状或算法类型等内容。例如，地球静止投影可能会像这样"看到"地球：

.. image:: https://proj.org/_images/geos.png
   :width: 300px
   :target: https://proj.org/operations/projections/geos.html

或者兰伯特等角圆锥（LCC）投影可能会像这样"看到"它：

.. image:: https://proj.org/_images/lcc.png
   :width: 300px
   :target: https://proj.org/operations/projections/lcc.html

更改特定 CRS 的参数将改变覆盖的地球区域以及与真实地球相比看到的失真水平。

正确定义数据的投影对于正确比较来自多个来源的数据非常重要。如果这些坐标是为不同的 CRS 定义的，则经度 0 和纬度 0 处的两个像素实际上并不代表相同的位置。通常，为了使比较最容易，坐标会被转换或数据被重采样到一个单一的 CRS。例如，来自预报模型的数据可能在经度/纬度投影上定义，坐标以度为单位指定。来自地球静止卫星的数据可能在地球静止投影上，坐标以米为单位。如果您想组合这些数据，您需要将坐标从一个投影转换到另一个投影。

.. [#]

   Battersby, S. (2017). Map Projections. The Geographic Information Science &
   Technology Body of Knowledge (2nd Quarter 2017 Edition), John P. Wilson (ed.). DOI: 10.22224/gistbok/2017.2.7

投影定义
----------------------

Pyresample 中有许多不同类型的投影可用。Pyresample 使用 :doc:`pyproj <pyproj:index>` 库的 ``CRS`` 对象来定义其所有坐标参考系统以及它们之间坐标的转换。Pyproj 依赖于较低级别的 :doc:`PROJ <proj:index>` C++ 库，该库定义了实际的坐标转换算法并维护预定义 CRS 的定义（例如 EPSG 代码）。您可以在 :doc:`此处 <proj:operations/projections/index>` 找到支持的 PROJ 定义列表。

在 Pyresample 中定义 CRS 的任何地方，都应该支持来自 ``pyproj`` 的 :class:`~pyproj.crs.CRS` 对象。这意味着有许多不同形式的定义 CRS 对象可用。有关选项的一些示例，请参阅 pyproj 的 :doc:`入门 <pyproj:examples>` 文档。

最后，投影并不是描述数据在地球上位置所需的唯一内容。有关如何将像素大小和地理范围与 CRS 结合以定义这些位置的信息，请参阅下一节 :doc:`geometries`。
