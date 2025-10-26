多进程
======

本文档描述如何在 pyresample 中使用多进程加速计算。

.. note::

   本文档正在翻译中。完整内容请参考英文文档。

并行重采样
-------------------

Pyresample 支持使用多进程和 dask 进行并行重采样。

使用 dask
^^^^^^^^^^

推荐使用 dask 进行并行处理：

.. code-block:: python

    import dask.array as da
    # 使用 dask 数组的重采样会自动并行化
