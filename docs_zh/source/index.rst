Pyresample
==========

Pyresample 是一个用于重采样地理空间图像数据的 Python 包。它是 `SatPy <https://github.com/pytroll/satpy>`_ 库中重采样的主要方法，但也可以作为独立库使用。

您可以使用 pyresample 将一个坐标系中的数据转换到另一个坐标系（例如墨卡托投影），使用可用的重采样算法之一。有关如何重采样数据的更多信息，请参阅我们的 :doc:`howtos/index` 部分。如果重采样对您来说是一个新概念，那么您可能会发现 :doc:`concepts/index` 部分有助于在不涉及代码的情况下解释重采样，或者参阅 :doc:`tutorials/index` 通过一些人工数据引导您完成这个过程。

为了能够重采样数据，Pyresample 必须很好地理解这些像素所代表区域的几何形状。要重采样的数据可以由均匀间隔/网格化的像素或可变间隔的像素"条带"组成。Pyresample 使用"几何"对象来描述这些地理定位数据集的不同属性。如果投影、像素分辨率或在球体或椭球体上表示数据等概念对您来说是新的，建议您从 :doc:`concepts/index` 部分开始了解更多信息，而不必过多担心实际代码。之后，:doc:`tutorials/index` 和 :doc:`howtos/index` 部分将能够向您展示将这些概念应用于数据所需的代码。

在整个文档中，您将找到有关 Pyresample 提供的各种实用程序的信息，以完成诸如使用 Cartopy 制作图表或描述来自 NetCDF 或 GeoTIFF 文件的数据等任务。Pyresample 通常能够处理表示为 numpy 数组、numpy 掩码数组的数据，在某些部分还能处理 Xarray DataArray 对象和 dask 数组。除了这些库之外，Pyresample 还受益于 `pykdtree <https://github.com/storpipfugl/pykdtree>`_ 和 `shapely <https://shapely.readthedocs.io/en/stable/>`_ 库的成果。Pyresample 在库的性能关键部分包含用 `Cython <https://cython.org/>`_ 编写的 Python 扩展代码。

.. warning::

   此文档仍在积极重新设计和重写中。某些信息可能不在您期望的位置，或者可能无法根据其他文档的质量和方法满足您的期望。欢迎以 GitHub issue 的形式提供反馈，但请知道我们正在努力改进此文档和库。

获取帮助
------------

在安装或使用 Pyresample 时遇到问题？请随时在 Pytroll 组的任何联系方式中提问，详见 `这里 <https://pytroll.github.io/#getting-in-touch>`_，或在 `Pyresample 的 GitHub 页面 <https://github.com/pytroll/pyresample/issues>`_ 上提交问题。

文档
-------------

.. toctree::
   :maxdepth: 2

   concepts/index
   tutorials/index
   howtos/index
   reference
