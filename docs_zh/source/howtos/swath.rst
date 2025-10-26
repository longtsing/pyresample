条带重采样
===============

本文档描述如何处理和重采样条带数据。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

条带到网格重采样
----------------------------

将非网格化的条带数据重采样到均匀网格是一个常见任务。

创建条带定义
^^^^^^^^^^^^^^^^^^^^^

首先创建一个条带定义：

.. code-block:: python

    from pyresample.geometry import SwathDefinition
    swath_def = SwathDefinition(lons=lons, lats=lats)

重采样到区域
^^^^^^^^^^^^^^^^^^

然后将条带数据重采样到目标区域：

.. code-block:: python

    from pyresample import create_resampler
    resampler = create_resampler(swath_def, area_def)
    result = resampler.resample(data)
