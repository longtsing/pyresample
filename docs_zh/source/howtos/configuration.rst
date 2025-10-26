配置
=============

Pyresample 允许在全局级别控制某些功能。这允许用户快速修改可能在 pyresample 非常低级的行为，而无需在整个代码中指定新参数。配置通过中央 ``config`` 对象控制，并允许通过以下三种方式之一设置参数：

1. 环境变量
2. YAML 文件
3. 在运行时使用 ``pyresample.config``

此功能由 :doc:`donfig <donfig:configuration>` 库提供。当前可用的设置如下所述。每个选项都可以从所有三种方法中获得。如果指定为环境变量或在磁盘上的 YAML 文件中指定，则必须在导入 Pyresample **之前**设置。

**YAML 配置**

包含这些参数的 YAML 文件可以位于以下任何位置：

1. ``<python environment prefix>/etc/pyresample/pyresample.yaml``
2. ``<user_config_dir>/pyresample.yaml``（见下文）
3. ``~/.pyresample/pyresample.yaml``

上述 ``user_config_dir`` 由 ``platformdirs`` 包提供，根据操作系统而异。典型的用户配置目录是：

* Mac OSX：``~/Library/Preferences/pyresample``
* Unix/Linux：``~/.config/pyresample``
* Windows：``C:\\Users\\<username>\\AppData\\Local\\pytroll\\pyresample``

从上述路径找到的所有 YAML 文件将合并到一个配置对象中（通过 ``pyresample.config`` 访问）。YAML 内容应该是配置键到其值的简单映射。例如：

.. code-block:: yaml

    some_key: "some_value"

在某些情况下，键可能被分组到子字典中：

.. code-block:: yaml

    features:
        future_geometries: true

最后，可以通过设置环境变量 ``PYRESAMPLE_CONFIG`` 来指定上述选项之外的额外配置路径。使用此环境变量指定的文件将在合并了上述所有路径后最后添加。

**在运行时**

导入后，可以在运行时通过以下方式自定义值：

.. code-block:: python

    import pyresample
    pyresamle.config.set(some_key="some_value")
    # ... 正常的 pyresample 代码 ...

或者对于特定的代码块：

.. code-block:: python

    import pyresample
    with pyresample.config.set(some_key="some_value):
        # ... 一些 pyresample 代码 ...
    # ... 使用原始 'some_key' 设置的代码

类似地，如果您需要访问其中一个值，可以使用 ``pyresample.config.get`` 方法。

缓存目录
^^^^^^^^^^^^^^^

* **环境变量**：``PYRESAMPLE_CACHE_DIR``
* **YAML/配置键**：``cache_dir``
* **默认值**：见下文

Pyresample 缓存的任何文件将存储在的目录。此目录不一定由 Pyresample 清除，但很少在没有用户明确启用的情况下使用。这默认为根据操作系统遵循 `platformdirs <https://github.com/platformdirs/platformdirs#example-output>`_ "用户缓存目录"的不同路径。

.. note::

   一些重采样算法在用户提供要缓存到的目录时提供缓存功能。这些重采样器当前不使用此配置选项。

.. _config_cache_sensor_angles_setting:

缓存几何切片
^^^^^^^^^^^^^^^^^^^^^

* **环境变量**：``PYRESAMPLE_CACHE_GEOMETRY_SLICES``
* **YAML/配置键**：``cache_geometry_slices``
* **默认值**：``False``

是否将为几何对象生成的切片缓存到磁盘。这些切片在 Pyresample 的各个部分使用，例如裁剪或重叠计算，包括在某些重采样算法中执行的那些。在撰写本文时，这仅在 ``AreaDefinition`` 对象上通过其 :meth:`~pyresample.geometry.AreaDefinition.get_area_slices` 方法执行。切片存储在 ``cache_dir`` 中（见上文）。与 Pyresample 中执行的其他缓存不同，在这些缓存中可能会缓存大型数组，此选项保存一对 ``slice`` 对象，每个对象仅包含 3 个整数。这使得许多缓存结果在缓存中使用的空间非常小。

Pyresample 中的切片操作通常涉及查找两个几何形状之间的交集。这需要为几何形状生成边界多边形，并进行可以处理投影反子午线的多边形交集计算。在撰写本文时，根据边界多边形中使用的顶点数，这些计算可能需要长达 15 秒。这些切片的一个用例是将输入数据减少到仅目标区域的重叠。这可以在重采样之前或期间作为算法的一部分或作为第三方重采样接口（例如 Satpy）的一部分完成。将来，随着对多边形交集逻辑进行优化，希望不需要此缓存选项。

将其设置为环境变量时，应使用 Python 布尔值的字符串等效值 ``="True"`` 或 ``="False"`` 进行设置。

.. warning::

    此缓存不限制条目数，也不会使旧条目过期。由用户管理缓存目录的内容。

功能标志
-------------

以下配置选项控制某些功能是否可用或默认使用或覆盖现有行为。在大多数情况下，这些用于 pyresample 的未来更改或可能稍后更改的实验性功能。这些标志都在 ``features`` 子字典下，这需要一些额外的工作来识别子结构。例如：

.. code-block:: python

    import pyresample
    pyresample.config.set({"features.future_geometries": True})

如果使用环境变量，请注意变量名称部分中使用双下划线 ``__``。

未来几何形状
^^^^^^^^^^^^^^^^^

* **环境变量**：``PYRESAMPLE_FEATURES__FUTURE_GEOMETRIES``
* **YAML/配置键**：``features: future_geometries``
* **默认值**：False

启用未来几何对象（``AreaDefinition``、``SwathDefinition`` 等）的使用，并覆盖任何内部使用的旧几何对象。此标志旨在简化在使用 ``create_area_def`` 等实用方法时在用户代码中切换到未来 pyresample 的过程。启用后，返回的几何实例将是未来几何类。可以从以下位置访问这些类：

.. code-block:: python

    from pyresample.future.geometry import AreaDefinition, SwathDefinition

最终，这些类将成为 Pyresample 2.0 中的默认值，此标志将不起作用。
