# -*- coding: utf-8 -*-
#
# pyresample 中文文档构建配置文件
# 基于 sphinx-quickstart on Tue Jan  5 13:01:32 2010 创建
#
# 此文件在执行时当前目录被设置为其所在目录。
#
# 注意并非所有可能的配置值都出现在这个自动生成的文件中。
#
# 所有配置值都有默认值；被注释掉的值用于显示默认值。
"""Sphinx 文档配置。"""
from __future__ import annotations

import os
import sys
from datetime import datetime

from pyresample import __version__  # noqa

# 添加 `source/` 目录使自定义扩展/插件可导入
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# -- 通用配置 -----------------------------------------------

# sphinxcontrib.apidoc 在 sphinx 8.2.0 中作为 sphinx.etx.apidoc 添加
needs_sphinx = "8.2.0"

# 在此添加任何 Sphinx 扩展模块名称（字符串）。它们可以是
# Sphinx 自带的扩展（名为 'sphinx.ext.*'）或自定义扩展。
extensions = [
    'sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx',
    'sphinx.ext.apidoc', 'sphinx_reredirects', 'doi_role', "sphinx_autodoc_typehints",
]

# DocTest 设置
# 不运行常规 >>> 代码块
doctest_test_doctest_blocks = ''
# 设置导入以便我们可以跳过某些 doctest
doctest_global_setup = '''
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import cartopy
except ImportError:
    cartopy = None

try:
    from mpl_toolkits.basemap import Basemap
except ImportError:
    Basemap = None
'''

# API 文档
apidoc_modules = [
    {
        "path": "../../pyresample",
        "destination": "api/",
        "exclude_patterns": [
            # 优先不记录测试模块。大多数用户如需要会查看源代码，
            # 我们希望避免文档构建因导入时测试数据创建而受影响。
            # 我们希望保留贡献者可能感兴趣的内容，如 satpy.tests.utils。
            "../../pyresample/test/test_*.py",
            "../../pyresample/test/**/test_*.py",
        ],
    },
]
apidoc_separate_modules = True
apidoc_include_private = True

autodoc_mock_imports = ["hashlib._Hash"]
autodoc_type_aliases = {
    "ArrayLike": "numpy.typing.ArrayLike",
    "DTypeLike": "numpy.typing.DTypeLike",
}
autodoc_default_options = {
    "special-members": "__init__, __reduce_ex__",
}
nitpick_ignore_regex: list[tuple[str, str]] = []
autoclass_content = "both"  # 将类 __init__ 文档字符串附加到类文档字符串



# Napoleon 设置（支持 numpy 风格文档）
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True

redirects = {
    "data_reduce": "howtos/data_reduce",
    "geo_def": "howtos/data_reduce",
    "geo_filter": "howtos/data_reduce",
    "geometry_utils": "howtos/data_reduce",
    "grid": "howtos/data_reduce",
    "multi": "howtos/data_reduce",
    "plot": "howtos/data_reduce",
    "plot_cartopy_basemap": "howtos/data_reduce",
    "plot_projections": "howtos/data_reduce",
    "preproc": "howtos/data_reduce",
    "spherical_geometry": "howtos/data_reduce",
    "swath": "howtos/data_reduce",
}

# 在此添加包含模板的路径，相对于此目录。
templates_path = ['_templates']

# 源文件名的后缀。
source_suffix = '.rst'

# 源文件的编码。
# source_encoding = 'utf-8'

# 主 toctree 文档。
master_doc = 'index'

# 项目的一般信息。
project = u'pyresample'
copyright = f"2013-{datetime.utcnow():%Y}, Pyresample 开发者"

# 正在记录的项目的版本信息，作为 |version| 和 |release| 的替换，
# 也用于整个构建文档中的各个其他地方。

version = __version__.split('+')[0]
# 完整版本，包括 alpha/beta/rc 标签。
release = __version__

# Sphinx 自动生成内容的语言。请参阅文档以获取支持的语言列表。
language = 'zh_CN'

# 有两个选项可以替换 |today|：要么设置 today 为某个非 false 值，然后使用它：
# today = ''
# 否则，today_fmt 用作 strftime 调用的格式。
# today_fmt = '%B %d, %Y'

# 不应包含在构建中的文档列表。
# unused_docs = []

# 相对于源目录的目录列表，不应搜索源文件。
exclude_trees: list[str] = []

# 用于所有文档的 reST 默认角色（用于此标记：`text`）。
# default_role = None

# 如果为 true，'()' 将附加到 :func: 等交叉引用文本。
# add_function_parentheses = True

# 如果为 true，当前模块名称将前置到所有描述单元标题（如 .. function::）。
# add_module_names = True

# 如果为 true，sectionauthor 和 moduleauthor 指令将显示在输出中。
# 默认情况下它们被忽略。
# show_authors = False

# Pygments（语法高亮）样式的名称。
pygments_style = 'sphinx'

# 用于模块索引排序的被忽略前缀列表。
# modindex_common_prefix = []


# -- HTML 输出选项 ---------------------------------------------

# 用于 HTML 和 HTML Help 页面的主题。Sphinx 自带的主要主题目前是
# 'default' 和 'sphinxdoc'。
html_theme = 'sphinx_rtd_theme'

# 主题选项是特定于主题的，并进一步自定义主题的外观和感觉。
# 有关每个主题可用选项的信息，请参阅文档。
# html_theme_options = {}

# 在此添加包含自定义主题的路径，相对于此目录。
# html_theme_path = []

# 此 Sphinx 文档集的名称。如果为 None，则默认为
# "<project> v<release> documentation"。
# html_title = None

# 导航栏的较短标题。默认与 html_title 相同。
# html_short_title = None

# 要放置在侧边栏顶部的图像文件（相对于此目录）的名称。
# html_logo = None

# 要用作文档图标的图像文件（在静态路径内）的名称。
# 此文件应该是 Windows 图标文件（.ico），大小为 16x16 或 32x32 像素。
# html_favicon = None

# 在此添加包含自定义静态文件（如样式表）的路径，相对于此目录。
# 它们在内置静态文件之后复制，因此名为 "default.css" 的文件将覆盖
# 内置的 "default.css"。
html_static_path = ['_static']

# 如果不是 ''，则在每个页面底部插入 'Last updated on:' 时间戳，
# 使用给定的 strftime 格式。
# html_last_updated_fmt = '%b %d, %Y'

# 如果为 true，SmartyPants 将用于将引号和破折号转换为
# 排版正确的实体。
# html_use_smartypants = True

# 自定义侧边栏模板，将文档名称映射到模板名称。
# html_sidebars = {}

# 应呈现到页面的其他模板，将页面名称映射到模板名称。
# html_additional_pages = {}

# 如果为 false，则不生成模块索引。
# html_use_modindex = True

# 如果为 false，则不生成索引。
# html_use_index = True

# 如果为 true，索引将拆分为每个字母的单独页面。
# html_split_index = False

# 如果为 true，则向页面添加 reST 源的链接。
# html_show_sourcelink = True

# 如果为 true，将输出 OpenSearch 描述文件，所有页面将
# 包含引用它的 <link> 标记。此选项的值必须是
# 从中提供完成的 HTML 的基本 URL。
# html_use_opensearch = ''

# 如果非空，这是 HTML 文件的文件名后缀（例如 ".xhtml"）。
# html_file_suffix = ''

# HTML 帮助构建器的输出文件基本名称。
htmlhelp_basename = 'pyresampledoc'


# -- LaTeX 输出选项 --------------------------------------------

# 纸张大小（'letter' 或 'a4'）。
# latex_paper_size = 'letter'

# 字体大小（'10pt'、'11pt' 或 '12pt'）。
# latex_font_size = '10pt'

# 将文档树分组到 LaTeX 文件中。元组列表
# (源起始文件、目标名称、标题、作者、文档类 [howto/manual])。
latex_documents = [
    ('index', 'pyresample.tex', u'pyresample 文档',
     u'Esben S. Nielsen', 'manual'),
]

# 要放置在标题页顶部的图像文件（相对于此目录）的名称。
# latex_logo = None

# 对于 "manual" 文档，如果这是 true，则顶级标题是部分，而不是章节。
# latex_use_parts = False

# LaTeX 前言的附加内容。
# latex_preamble = ''

# 要作为附录附加到所有手册的文档。
# latex_appendices = []

# 如果为 false，则不生成模块索引。
# latex_use_modindex = True

# Intersphinx 扩展
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy', None),
    'xarray': ('https://docs.xarray.dev/en/stable', None),
    'dask': ('https://docs.dask.org/en/latest', None),
    'pandas': ('https://pandas.pydata.org/docs', None),
    'trollsift': ('https://trollsift.readthedocs.io/en/stable', None),
    'trollimage': ('https://trollimage.readthedocs.io/en/stable', None),
    'pyproj': ('https://pyproj4.github.io/pyproj/dev/', None),
    'proj': ('https://proj.org/en/stable', None),
    'satpy': ('https://satpy.readthedocs.io/en/stable', None),
    'donfig': ('https://donfig.readthedocs.io/en/latest', None),
}
