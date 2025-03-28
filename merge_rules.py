import requests
from typing import List
import os
from datetime import datetime

def fetch_raw_content(url: str) -> List[str]:
    """获取 GitHub raw 内容"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        # 按行分割并去除空白行
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"获取内容失败: {url}, 错误: {e}")
        return []

def merge_and_deduplicate(url1: str, url2: str) -> List[str]:
    """合并两个源并去重"""
    # 获取两个源的内容
    content1 = fetch_raw_content(url1)
    content2 = fetch_raw_content(url2)
    
    # 合并并去重
    merged_content = list(set(content1 + content2))
    # 排序以保持一致性
    merged_content.sort()
    
    return merged_content

def save_to_file(content: List[str], output_file: str):
    """保存内容到文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

def main():
    # GitHub raw URLs
    url1 = "https://raw.githubusercontent.com/zimoadmin/adgrule/main/rule/all.txt"
    url2 = "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockdns.txt"
    
    # 输出文件名
    output_file = "merged_rules.txt"
    
    # 合并和去重
    merged_content = merge_and_deduplicate(url1, url2)
    
    # 保存结果
    save_to_file(merged_content, output_file)

if __name__ == "__main__":
    main()