# Pyresample 中文文档

这是 Pyresample 项目的中文文档目录。此目录完全独立于英文文档，可以单独构建。

## 构建文档

确保已安装 sphinx 和 pyresample 的依赖后，可以通过运行以下命令生成中文文档：

```bash
cd docs_zh
make html
```

生成的 HTML 文档页面位于 `build/html` 目录中。

## 文档结构

中文文档遵循与英文文档相同的结构：

- `source/concepts/` - 核心概念文档
- `source/tutorials/` - 教程文档
- `source/howtos/` - 操作指南文档
- `source/dev_guide/` - 开发者指南
- `source/api/` - API 文档（自动生成）

## 配置

文档配置文件 `source/conf.py` 已设置语言为中文（`language = 'zh_CN'`），其他配置与英文文档保持一致。

## 翻译说明

### 已完成翻译的文件

#### 根目录
- ✅ README.md
- ✅ Makefile
- ✅ areas.cfg（复制）
- ✅ areas.yaml（复制）
- ✅ environment.yml（复制）

#### source 目录
- ✅ conf.py（已汉化并设置语言）
- ✅ doi_role.py（复制）
- ✅ index.rst
- ✅ reference.rst
- ✅ roadmap.rst

#### concepts 目录
- ✅ index.rst
- ✅ geolocated_data.rst
- ✅ projections.rst
- ✅ geometries.rst
- ✅ resampling.rst

#### tutorials 目录
- ✅ index.rst
- ✅ installation.rst

#### howtos 目录
- ✅ index.rst
- ✅ configuration.rst（完整翻译）
- ✅ geo_def.rst（完整翻译）
- ✅ geometry_utils.rst（占位符）
- ✅ geo_filter.rst（占位符）
- ✅ grid.rst（占位符）
- ✅ swath.rst（占位符）
- ✅ multi.rst（占位符）
- ✅ preproc.rst（占位符）
- ✅ spherical_geometry.rst（占位符）
- ✅ plot.rst（占位符）
- ✅ plot_cartopy_basemap.rst（占位符）
- ✅ plot_projections.rst（占位符）
- ✅ data_reduce.rst（占位符）

#### dev_guide 目录
- ✅ index.rst

### 后续改进建议

1. **完善 howtos 文档**：当前大部分 howtos 文档使用占位符，包含基本结构和简要说明。可以根据需要逐步完善这些文档的完整翻译。

2. **添加中文示例**：可以考虑在代码示例中添加中文注释，使其更易于中文用户理解。

3. **更新链接**：某些外部链接仍然指向英文资源，可以在有中文资源时进行更新。

4. **持续同步**：当英文文档更新时，需要同步更新中文文档。

## 使用方法

### 本地构建

```bash
# 进入中文文档目录
cd docs_zh

# 安装依赖（如果尚未安装）
pip install -r ../docs/environment.yml

# 构建 HTML 文档
make html

# 清理构建文件
make clean
```

### 查看文档

构建完成后，可以在浏览器中打开 `build/html/index.html` 查看文档。

## 贡献

欢迎对中文文档进行改进和完善！如果您发现翻译错误或有改进建议，请提交 issue 或 pull request。

## 许可

本中文文档遵循与 Pyresample 项目相同的许可协议。
