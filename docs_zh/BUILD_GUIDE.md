# Pyresample 中文文档构建指南

## 概述

`docs_zh` 目录是 Pyresample 的中文文档系统，完全独立于英文文档 `docs` 目录，可以单独构建和部署。

## 目录结构

```
docs_zh/
├── README.md                 # 简要说明
├── README_ZH.md             # 详细的中文说明
├── Makefile                 # 构建脚本（与原docs相同）
├── areas.cfg                # 区域配置文件
├── areas.yaml               # 区域YAML配置
├── environment.yml          # Python环境依赖
└── source/                  # 文档源文件
    ├── conf.py              # Sphinx配置（语言设置为zh_CN）
    ├── doi_role.py          # DOI引用扩展
    ├── index.rst            # 首页
    ├── reference.rst        # 参考文档
    ├── roadmap.rst          # 路线图
    ├── api/                 # API文档（自动生成）
    ├── concepts/            # 概念文档（已完整翻译）
    │   ├── index.rst
    │   ├── geolocated_data.rst
    │   ├── projections.rst
    │   ├── geometries.rst
    │   └── resampling.rst
    ├── tutorials/           # 教程文档（已完整翻译）
    │   ├── index.rst
    │   └── installation.rst
    ├── howtos/              # 操作指南（部分翻译+占位符）
    │   ├── index.rst
    │   ├── configuration.rst    # 完整翻译
    │   ├── geo_def.rst          # 完整翻译
    │   ├── geometry_utils.rst   # 占位符
    │   ├── geo_filter.rst       # 占位符
    │   ├── grid.rst             # 占位符
    │   ├── swath.rst            # 占位符
    │   ├── multi.rst            # 占位符
    │   ├── preproc.rst          # 占位符
    │   ├── spherical_geometry.rst # 占位符
    │   ├── plot.rst             # 占位符
    │   ├── plot_cartopy_basemap.rst # 占位符
    │   ├── plot_projections.rst # 占位符
    │   └── data_reduce.rst      # 占位符
    ├── dev_guide/           # 开发者指南（已翻译）
    │   └── index.rst
    └── _static/             # 静态资源
        └── images/
```

## 翻译状态

### ✅ 已完成完整翻译

1. **核心配置**
   - conf.py（已设置语言为中文）
   - index.rst（主页）
   - reference.rst（参考）
   - roadmap.rst（路线图）

2. **概念文档** (concepts/)
   - 所有5个文件已完整翻译
   - 涵盖地理定位数据、投影、几何形状、重采样等核心概念

3. **教程文档** (tutorials/)
   - 所有2个文件已完整翻译
   - 包括安装指南

4. **操作指南** (howtos/)
   - configuration.rst - 完整翻译
   - geo_def.rst - 完整翻译
   - 其余11个文件为占位符（包含基本结构和简要说明）

5. **开发者指南** (dev_guide/)
   - 已翻译

### 📝 占位符说明

占位符文件包含：
- 文档标题（已翻译）
- 基本章节结构（已翻译）
- 简要的内容说明（已翻译）
- "本文档正在翻译中"的提示
- 指向英文文档的参考

占位符文件可以正常构建文档，不会影响文档系统的完整性。用户可以看到文档结构，并在需要时参考英文原文。

## 构建文档

### 前提条件

确保已安装必要的依赖：

```bash
pip install sphinx sphinx_rtd_theme sphinx-reredirects sphinx-autodoc-typehints
pip install pyresample  # 需要用于API文档生成
```

或使用环境文件：

```bash
conda env create -f environment.yml
```

### 构建HTML文档

```bash
cd docs_zh
make html
```

构建的文档将位于 `build/html/` 目录中。

### 清理构建

```bash
make clean
```

### 其他构建目标

```bash
make dirhtml    # HTML文件在目录中
make pickle     # Pickle文件
make json       # JSON文件
make latex      # LaTeX文件
make linkcheck  # 检查外部链接
make doctest    # 运行文档测试
```

## 与原英文文档的关系

### 相同点
- 使用相同的Makefile结构
- 使用相同的Sphinx扩展
- 使用相同的主题（sphinx_rtd_theme）
- API文档指向相同的Python代码

### 不同点
- `conf.py` 中设置 `language = 'zh_CN'`
- 所有 .rst 文件内容为中文
- copyright 信息已汉化
- 可独立构建，不依赖英文文档

## 替代英文文档

`docs_zh` 可以完全替代 `docs` 目录用于中文文档构建：

1. **独立性**：不依赖英文docs目录
2. **完整性**：包含所有必要的配置和文件
3. **兼容性**：使用相同的构建系统
4. **可部署性**：可单独部署到文档服务器

要将中文文档作为主文档使用，只需：

```bash
# 将docs_zh作为文档根目录
cd docs_zh
make html

# 或者在项目根目录
sphinx-build -b html docs_zh/source docs_zh/build/html
```

## 后续改进建议

1. **完善占位符文档**
   - 根据需求逐步翻译howtos中的占位符文档
   - 添加更多中文示例和注释

2. **添加中文特定内容**
   - 中文用户常见问题
   - 中文社区资源链接

3. **持续同步**
   - 监控英文文档更新
   - 同步重要的内容变更

4. **优化翻译质量**
   - 统一术语翻译
   - 改进表达的地道性

## 贡献

欢迎贡献改进！可以：
- 完善占位符文档的翻译
- 改进现有翻译质量
- 添加中文示例
- 修正错误

## 测试文档

在提交前测试文档构建：

```bash
cd docs_zh
make clean
make html
```

确保没有警告或错误。

## 许可

遵循 Pyresample 项目的许可协议。
