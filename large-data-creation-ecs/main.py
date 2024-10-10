import csv
import random
import string
import datetime
import os

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_date(start_date, end_date):
    return start_date + datetime.timedelta(
        days=random.randint(0, (end_date - start_date).days))

# ファイルサイズを指定
target_file_size_mb = 10
target_file_size_bytes = target_file_size_mb * 1000 * 1000
buffer_size_bytes = 1000  # バッファを持たせる

# CSVファイルのフィールド名
fieldnames = ['商品ID', '商品名', 'カテゴリ', '価格', '在庫数', '説明', '発売日']

# サンプルデータの生成
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2023, 12, 31)

# 生成された商品IDを保持するセット
# set()は重複する要素を持たない特性がある
# 重複チェックが簡単にできる
generated_product_ids = set()

# ファイルを開く
with open('product_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    while file.tell() < (target_file_size_bytes - buffer_size_bytes):
        # 重複しない商品IDを生成（5回重複したらエラー終了する）
        duplicate_attempts = 0
        while duplicate_attempts < 5:
            product_id = generate_random_string(20)
            if product_id not in generated_product_ids:
                generated_product_ids.add(product_id)
                break
            duplicate_attempts += 1
        else:
            print("商品IDの重複が5回発生しました。生成を終了します。")
            break

        product_name = generate_random_string(15)
        category = random.choice(categories)
        price = round(random.uniform(10.0, 1000.0), 2)
        stock = random.randint(0, 1000)
        description_length = random.randint(20, 100)
        description = generate_random_string(description_length)
        release_date = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')

        row = {
            '商品ID': product_id,
            '商品名': product_name,
            'カテゴリ': category,
            '価格': price,
            '在庫数': stock,
            '説明': description,
            '発売日': release_date
        }

        # 行のサイズを確認
        row_size = sum(len(str(value)) for value in row.values()) + len(fieldnames) - 1 + 2  # カンマと改行のサイズ
        if file.tell() + row_size > target_file_size_bytes:
            break
        writer.writerow(row)

print("CSVファイルが生成されました: product_data.csv")