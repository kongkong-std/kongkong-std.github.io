import os
import datetime
import yaml

# ---------------- 配置 ----------------
category = "sc"                     # 分类名
layout = "archive_by_year_sc"       # 使用的 layout
per_page_years = 3                  # 每页显示多少年份
posts_dir = "_posts/resources/sc"                # Jekyll posts 目录
output_dir = "_pages/navbar/sc"     # 生成的页面目录
# -------------------------------------

# 读取所有文章
posts = []
for fname in os.listdir(posts_dir):
    if fname.endswith(".md") or fname.endswith(".markdown"):
        fpath = os.path.join(posts_dir, fname)
        with open(fpath, "r") as f:
            lines = f.readlines()
        # 解析 front matter
        if lines[0].strip() == "---":
            fm_lines = []
            for line in lines[1:]:
                if line.strip() == "---":
                    break
                fm_lines.append(line)
            fm = yaml.safe_load("".join(fm_lines))
            # 检查分类
            if fm.get("categories") and category in fm.get("categories"):
                # 获取日期
                date_str = fm.get("date")
                if date_str:
                    date_str = str(date_str).replace("/", "-")
                    try:
                        date_obj = datetime.datetime.fromisoformat(date_str)
                    except ValueError:
                        print(f"跳过文章 {fname}：front matter date 格式不正确 -> {date_str}")
                        continue
                else:
                    # 从文件名解析日期 (YYYY-MM-DD-title.md)
                    try:
                        date_obj = datetime.datetime.fromisoformat(fname[:10])
                    except ValueError:
                        print(f"跳过文章 {fname}：无法从文件名解析日期")
                        continue
                posts.append({
                    "title": fm.get("title") or fname,
                    "date": date_obj,
                    "filename": fname
                })

print(f"找到 {len(posts)} 篇 {category} 分类文章")

# 提取年份并倒序
years = sorted({p["date"].year for p in posts}, reverse=True)
total_pages = (len(years) + per_page_years - 1) // per_page_years

print(f"年份列表: {years}, 总页数: {total_pages}")

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 生成每页
for page_num in range(1, total_pages + 1):
    start = (page_num - 1) * per_page_years
    end = start + per_page_years
    page_years = years[start:end]

    # 首页和其他页路径
    if page_num == 1:
        fname = os.path.join(output_dir, "index.md")
        permalink = "/navbar/sc/"
    else:
        page_subdir = os.path.join(output_dir, f"page{page_num}")
        os.makedirs(page_subdir, exist_ok=True)
        fname = os.path.join(page_subdir, "index.md")
        permalink = f"/navbar/sc/page{page_num}/"

    # Front matter
    front_matter = {
        "layout": layout,
        "title": "Scientific Computing",
        "permalink": permalink,
        "page_num": page_num,
        "total_pages": total_pages,
        "years": page_years
    }

    # 写入文件
    with open(fname, "w") as f:
        f.write("---\n")
        yaml.dump(front_matter, f)
        f.write("---\n\n")
        f.write(f"<!-- 自动生成: 页码 {page_num} -->\n")

    print(f"生成页面: {fname}, 对应年份: {page_years}")
