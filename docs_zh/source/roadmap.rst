路线图
=======

迈向 2.0 的路线图！
---------------

Pyresample 经历了一些实实在在的成长阵痛。随着 Pytroll 开发者在 Satpy 上的工作，这些问题变得越来越明显，在 Satpy 中我们有更多的自由从头开始并创建适合我们的接口。这些开发以及 2021 年进行的 Pyresample 用户调查为我们指导了 Pyresample 的新设计，我们希望将其作为 2.0 版本发布。

下面是 Pyresample 组件的各个类别以及我们如何看待它们的存在。在 Pyresample 中现有接口的大多数情况下，我们预期事情将向后兼容，或者在极端情况下，我们希望在现有接口旁边添加新接口，以便更轻松地过渡到新功能。这意味着一些已弃用的接口，以便我们可以使用户体验更加一致，无论重采样算法或其他用例如何。

您可以通过关注 GitHub 上 `v2.0 里程碑 <https://github.com/pytroll/pyresample/milestone/3>`_ 的问题和拉取请求来跟踪 Pyresample 2.0 的进度。

2.0 版本不计划什么？
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 垂直或其他更高维度的重采样：这不是一个简单的问题，考虑到 2.0 计划的其他更改，我们无法研究这个问题。
* 新的重采样算法：2.0 版本的提升不是为了新算法。我们会将这些更多地保留给次要版本发布。版本 2.0 是关于更大的破坏性更改。

几何类
^^^^^^^^^^^^^^^^

Pyresample 中目前有 X 种面向用户的几何对象：

* ~GridDefinition~
* SwathDefinition
* DynamicAreaDefinition
* AreaDefinition
* StackedAreaDefinition

我们已经意识到 ``GridDefinition`` 实际上是 ``AreaDefinition`` 的一个特殊情况，因此它将被弃用。从目的上讲，其他类在某种意义上仍然是需要的，很可能不会消失。对这些类的大多数更改将是内部的，以保持代码整洁。

然而，我们希望这些类更容易创建和使用。我们希望专注于与 Pyresample 的其余部分一起使用这些对象实际需要什么。这意味着将"数字"与元数据分开。AreaDefinitions 将不再需要名称或其他描述性信息。您可以提供它们，但它们不是必需的。

展望未来，我们希望用户专注于使用类方法来创建这些对象。我们希望这将提供从您拥有的信息到可用对象的更容易的连接。例如，而不是：

.. code-block:: python

    area = AreaDefinition(name, description, proj_id, projection, width, height, area_extent)

您将在 pyresample 2.0 中这样做：

.. code-block:: python

    metadata = {"name": name, "description": description}  # 可选
    area = AreaDefinition.from_extent_shape(projection, area_extent, (height, width), metadata)

您还将被允许向条带定义和其他几何类型提供任意元数据。

重采样器
^^^^^^^^^^

目前，Pyresample 中不同重采样选项的调用接口各不相同。有时您调用一个函数，有时您创建一个类并在其上调用"resample"方法，有时如果您想要更精细的控制，您会调用多个函数并必须在它们之间传递内容。在 Pyresample 2.0 中，我们希望将事情归结为几个一致的接口，所有这些都包装在一系列 Resampler 类中。

创建重采样器
*******************

您将通过以下方式创建重采样器类：

.. code-block:: python

    from pyresample import create_resampler
    resampler = create_resampler(src_geom, dst_geom, resampler='some-resampler-name')

Pyresample 2.0 将维护一个可用重采样器类的"注册表"，您可以通过名称引用它们，或者根据传递的几何形状获得默认值。这个重采样器注册表还将使用户或第三方库更容易添加自己的重采样器。

我们希望通过这个基本的创建过程，我们可以更好地控制哪些算法支持哪些特性，并在早期通过清晰的错误消息让用户知道何时不允许某些操作。例如，重采样器支持哪些几何类型的组合，或者可以提供哪些类型的数组（xarray.DataArray、dask 或 numpy）。

使用重采样器
****************

一旦您有了重采样器实例，您可以通过以下方式重采样数据：

.. code-block:: python

    new_data = resampler.resample(data, **kwargs)

就是这样。当然，``**kwargs`` 中隐藏了很多选项，但这些将特定于每个算法。我们希望任何需要进行的优化或转换以使您的数据重采样都可以包含在这些重采样器对象中，并希望对用户的要求更少。

作为 ``.resample`` 调用的替代方案，用户可以首先调用两个方法：

.. code-block:: python

    resampler.precompute()
    new_data = resampler.compute(data, **kwargs)

这个 ``precompute`` 方法将执行任何无需实际"图像"数据即可完成的计算。然后，您可以调用 ``.compute`` 来进行实际的重采样。当我们开始讨论缓存时（见下文），这种分离很重要。

缓存
*******

我们希望通过 Pyresample 2.0 实现的一个主要简化是一组定义的缓存功能，所有这些都封装在"Cache"对象中。这些对象可以传递给 ``create_resampler``，以使重采样器能够存储中间计算结果以供重用。存储的方式和位置取决于特定的缓存对象。它可以仅在内存中，也可以在本地磁盘上的 zarr 数据集中，或者在某个远程存储中。

通过调用 ``.precompute`` 方法，用户将能够在不需要任何图像数据的情况下预先填充此缓存。这对于在实时（时间敏感）处理之前希望手动填充缓存的操作中使用 pyresample 的用户很有用。

索引
^^^^^^^

从我们的调查中，我们了解到很多用户使用 ``get_neighbour_info`` 返回的索引进行自己的自定义分析。我们认识到这种需求，虽然可以编写 Cache 对象来获得相同的结果，但我们认为有更好的方法。我们计划通过单独的"Index"接口实现此功能。与 Resamplers 一样，这些将为您提供一种将源几何形状关联到目标几何形状的方法。但是，这些对象只负责返回索引信息。

我们还没有定义这些的接口，但希望将其与重采样器分开将为更多人服务。

Xarray 和 Geoxarray
^^^^^^^^^^^^^^^^^^^^

我们希望更多地支持使用 xarray 和 dask 库的 pyresample 用户。在过去几年中，我们在幕后通过 Satpy 库向 pyresample 添加了大量基于 dask 的支持。我们慢慢地将该功能移至 Pyresample，上面提到的 Resampler 对象是第一个定义的接口。然而，要完全利用 dask 数组为我们提供的并行特性，还有很多工作要做。

对于在 xarray DataArray 或 Dataset 对象中拥有数据的用户来说，访问 pyresample 功能也应该更容易；即使不知道 pyresample 需要的元数据来进行某些重采样（例如 CRS、范围等）。通常，这类信息已经保存在 xarray 对象的元数据中。正在开发新工具以使此信息更容易访问；主要是 `Geoxarray 项目 <https://geoxarray.github.io/latest/>`_。我们将致力于 Geoxarray 和 Pyresample，以简化 xarray 用户的常见重采样任务。

文档
^^^^^^^^^^^^^

Pyresample 的文档需要大量的关爱。随着 Pyresample 的发展，文档并没有真正重新构建以最好地呈现它所承载的新信息。我们希望作为 Pyresample 2.0 的一部分，我们可以清除蜘蛛网，使您更容易找到所需的信息。
