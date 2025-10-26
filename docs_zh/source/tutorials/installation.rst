安装
============

Pyresample 可以通过 pip 从 PyPI 安装，也可以使用 conda-forge 频道在 conda 环境中安装。以下部分将展示安装 Pyresample 的可能方法以及可以进行的自定义。

使用 pip
--------

Pyresample 可从 PyPI 获得，可以使用 pip 安装：

.. code-block:: bash

   pip install pyresample

使用 conda
----------

Pyresample 也可以通过 conda-forge 频道使用 conda 或 mamba 安装：

.. code-block:: bash

   conda install -c conda-forge pyresample

从源代码安装
-----------

您可以从源 tarball（或其他源目录）安装 Pyresample：

.. code-block:: bash

   tar -zxvf pyresample-<version>.tar.gz
   cd pyresample-<version>
   pip install .

您也可以直接从 github 安装：

.. code-block:: bash

   pip install git+https://github.com/pytroll/pyresample.git@main

其中 ``main`` 是主要的 git 分支。可以自定义此分支名称和 URL 中的用户帐户（上面的 ``pytroll``）以安装开发中的 git 分支。

用于开发
---------------

如果您想编辑 Pyresample 并查看更改对当前环境的影响，可以以"可编辑"模式安装它：

.. code-block:: bash

   pip install -e .

请注意，Pyresample 有一些 C 扩展，如果修改必须重新编译。此编译仅在安装/构建时发生，因此需要重新运行上述命令才能看到对这些扩展模块的更改的效果。

运行测试
---------

测试 pyresample 需要安装所有可选包。如果没有所有这些依赖项，某些测试可能会失败。要从本地源目录运行测试：

.. code-block:: bash

    pytest pyresample/test/

或者您可以在已安装的包版本上运行它：

.. code-block:: bash

    pytest --pyargs pyresample.test

如果所有测试都通过，则系统上所有 pyresample 函数的功能已得到验证。

可选依赖项
---------------------

Pyresample 有很多功能可能并非所有用户都需要。这些功能仅在使用时导入其依赖项，因此在安装后可能不明显您需要它们。这些依赖项默认不安装，必须单独安装。

为了使用 Pyresample 绘图功能，必须安装 ``cartopy`` 和 ``matplotlib``。这些包不是使用任何其他 pyresample 功能的先决条件。

此外，对于 ``dask`` 和 ``xarray`` 支持，也必须安装这些库。一些实用函数可能有额外的、希望是显而易见的依赖项。例如，从 ``rasterio`` 库转换对象需要安装 ``rasterio``。

Pyresample 的部分功能提供非 dask 多进程接口，可能有额外的依赖项来完成此操作。例如，当 ``nprocs`` 可用并指定了大于 1 的值时，将使用特殊的 ``Proj_MP``，并且需要来自 ``scipy`` 包的 ``KDTree`` 类。建议在可能的情况下使用较新的 xarray/dask 接口。

pyresample 的某些功能使用 ``pykdtree`` 包中的 ``KDTree`` 对象。此包受益于通过 OpenMP 库构建多线程支持，但默认情况下并不总是内置此支持。有关构建提示和建议，请参阅 `pykdtree README <https://github.com/storpipfugl/pykdtree/blob/master/README.rst>`_。您可能希望使用 ``OMP_NUM_THREADS`` 环境变量控制 pykdtree 使用的线程数。

如果可用，Pyresample 还使用 `numexpr <https://github.com/pydata/numexpr>`_ 包进行一些小的瓶颈优化。
