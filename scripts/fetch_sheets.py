import pandas as pd
from datetime import datetime
import pytz
import subprocess

china_tz = pytz.timezone("Asia/Shanghai")
now = datetime.now(china_tz)
date_time= now.strftime('%Y-%m-%d')
# CSV download URL
CSV_URL = f"https://github.com/mbnspocb/611Study-DataCleaner/releases/download/{date_time}/valid.csv"
# Get current time in UTC+8
current_time=now.strftime("%Y-%m-%d %H:%M:%S")
# Download CSV file using wget
subprocess.run(["wget", "-q", CSV_URL, "-O", "data.csv"], check=True)
# Read CSV file
df = pd.read_csv("data.csv")
num_to_chinese = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
}

# 年级映射
grade_map = {
    **{i: f"小{num_to_chinese[i]}" for i in range(1, 7)},  # 小学1-6年级
    **{i: f"初{num_to_chinese[i - 6]}" for i in range(7, 10)},  # 初中1-3年级
    **{i: f"高{num_to_chinese[i - 9]}" for i in range(10, 13)},  # 高中1-3年级
}

# 替换年级字段
df["年级"] = df["年级"].replace(grade_map)



with open("template.html", "r", encoding="utf-8") as f:
    html_content = f.read()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(
        html_content.replace(
            "{data}",
            df.to_html(
                index=False,
                columns=[
                    "时间戳记",
                    "省份",
                    "城市",
                    "区县",
                    "学校名称",
                    "年级",
                    "每周在校学习小时数",
                    "每月假期天数",
                    "寒假放假天数",
                    "24年学生自杀数",
                    "上学时间",
                    "放学时间\n含晚自习",
                    "寒假补课收费总价格",
                    "学生的评论",
                ],
                classes="table",
                escape=False,
                na_rep="不适用",
                float_format=lambda x: f"{int(x)}"
                if isinstance(x, float) and x.is_integer()
                else f"{x}",
            ).replace("<td>不适用</td>", '<td class="empty">不适用</td>'),
        ).replace("{current_time}", current_time),
    )
