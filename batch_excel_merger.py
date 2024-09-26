import pandas as pd
import os
import re

# 從環境變數中獲取自訂密碼
custom_password = os.getenv('CUSTOM_BATCH_PASSWORD')

# 獲取所有 Excel 文件
excel_files = [f for f in os.listdir('.') if f.endswith('.xlsx') or f.endswith('.xls')]

merged_data = pd.DataFrame()

for file in excel_files:
    try:
        # 提取文件名前綴
        match = re.match(r'^([^_]+)_', file)
        if not match:
            print(f"警告：文件 '{file}' 名稱格式不正確，將被跳過。")
            continue
        
        prefix = match.group(1)
        
        # 讀取 Excel 文件
        df = pd.read_excel(file)
        
        # 過濾掉範例數據
        df = df[~df.iloc[:, 0].isin(['範例1', '範例2'])]
        
        # 添加自訂密碼列（第五列）
        password_with_prefix = f"{custom_password}{prefix}"
        df.insert(4, "自訂密碼", password_with_prefix)
        
        # 添加批次編號列（第六列）
        batch_numbers = [f"{prefix}-{i:02d}" for i in range(1, len(df) + 1)]
        df.insert(5, "批次編號", batch_numbers)
        
        merged_data = pd.concat([merged_data, df], ignore_index=True)
        print(f"成功處理文件：'{file}'，處理了 {len(df)} 行數據")
        
    except Exception as e:
        print(f"處理文件 '{file}' 時出錯：{str(e)}")

# 保存合併後的數據
if not merged_data.empty:
    merged_data.to_excel('merged_excel_with_custom_password_and_batch.xlsx', index=False)
    print(f"Excel文件已成功合併，總行數：{len(merged_data)}!")
else:
    print("沒有成功處理任何文件，請檢查文件格式和內容。")
