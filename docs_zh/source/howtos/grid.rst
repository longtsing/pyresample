网格重采样
=============

本文档描述如何在网格化数据之间进行重采样。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

区域到区域重采样
------------------------

最常见的重采样任务之一是将一个网格区域的数据重采样到另一个网格区域。

创建重采样器
^^^^^^^^^^^^^^^^^^

首先创建一个重采样器对象：

.. code-block:: python

    from pyresample import create_resampler
    resampler = create_resampler(source_area, target_area)

执行重采样
^^^^^^^^^^^^^^^^^

然后使用重采样器对数据进行重采样：

.. code-block:: python

    result = resampler.resample(data)
