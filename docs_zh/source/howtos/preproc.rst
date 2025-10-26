数据预处理
============

本文档描述如何为重采样准备数据。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

数据准备
--------------

在重采样之前，可能需要对数据进行预处理。

坐标检查和包装
^^^^^^^^^^^^^^^^^^^^^

使用 :func:`~pyresample.utils.check_and_wrap` 函数检查和包装坐标：

.. code-block:: python

    from pyresample.utils import check_and_wrap
    lons, lats = check_and_wrap(lons, lats)
