几何实用工具
==================

本文档描述了创建和操作几何定义对象的各种实用工具。有关几何定义的基础信息，请参阅 :doc:`geo_def`。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

创建区域定义
------------------------

Pyresample 提供了多种创建 :class:`~pyresample.geometry.AreaDefinition` 对象的方法。

从范围和形状创建
^^^^^^^^^^^^^^^^^^^^^

使用 :meth:`~pyresample.geometry.AreaDefinition.from_extent` 类方法可以从区域范围和形状创建区域定义。

从 YAML 配置文件加载
^^^^^^^^^^^^^^^^^^^^^^^^^^^

可以使用 :func:`~pyresample.area_config.load_area` 函数从 YAML 配置文件加载区域定义。

动态区域定义
---------------------------

:class:`~pyresample.geometry.DynamicAreaDefinition` 类允许创建在运行时确定最终形状的区域定义。

堆叠区域定义  
--------------------------

:class:`~pyresample.geometry.StackedAreaDefinition` 类允许将多个区域定义堆叠在一起。
