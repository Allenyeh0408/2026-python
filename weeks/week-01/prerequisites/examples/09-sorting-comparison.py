# 9 比較、排序與 key 函式範例

# ===== 1. 比較運算（tuple 逐一比較）=====
# Python 的 tuple 比較會從第一個元素開始逐一比較
# 如果第一個元素相同，就比較第二個，以此類推
a = (1, 2)
b = (1, 3)
result = a < b  # True，因為第一個元素相同(1==1)，所以比較第二個元素(2<3)
print(f"a < b = {result}")  # 輸出: True
print(f"比較過程: {a} 和 {b} 的第一個元素相同，第二個元素 2 < 3，所以結果為 True")

# 更多 tuple 比較範例
print("\n更多比較範例:")
print(f"(1, 2) < (2, 0) = {(1, 2) < (2, 0)}")  # True，第一個元素就決定了
print(f"(1, 2) == (1, 2) = {(1, 2) == (1, 2)}")  # True，所有元素都相同
print(f"(1, 2, 3) < (1, 2, 4) = {(1, 2, 3) < (1, 2, 4)}")  # True


# ===== 2. key 排序 =====
# sorted() 函式可以使用 key 參數來指定「根據什麼來排序」
# key 參數接受一個函式，該函式會被套用到每個元素上，返回的值用於比較
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
print("\n原始資料:", rows)

# 使用 lambda 函式作為 key，根據 'uid' 欄位排序
rows_sorted = sorted(rows, key=lambda r: r['uid'])
print("排序後資料:", rows_sorted)  # 輸出: [{'uid': 1}, {'uid': 2}, {'uid': 3}]

# key 的運作原理:
# 1. lambda r: r['uid'] 會對每個元素 r 執行，提取 uid 值
# 2. sorted() 使用這些提取的值進行排序
# 3. 返回排序後的原始字典列表

# 反向排序
rows_sorted_desc = sorted(rows, key=lambda r: r['uid'], reverse=True)
print("反向排序:", rows_sorted_desc)  # 輸出: [{'uid': 3}, {'uid': 2}, {'uid': 1}]


# ===== 3. min/max 搭配 key =====
# min() 和 max() 函式也可以使用 key 參數
# key 指定「根據什麼標準來判斷最小/最大值」
smallest = min(rows, key=lambda r: r['uid'])
print("\nuid 最小的項目:", smallest)  # 輸出: {'uid': 1}

largest = max(rows, key=lambda r: r['uid'])
print("uid 最大的項目:", largest)  # 輸出: {'uid': 3}

# 如果沒有 key，直接對字典列表使用 min/max 會報錯
# 因為字典之間無法直接比較大小

# 更複雜的範例：多個欄位的字典
students = [
    {'name': '小明', 'score': 85, 'age': 20},
    {'name': '小華', 'score': 92, 'age': 19},
    {'name': '小美', 'score': 78, 'age': 21}
]

print("\n學生資料範例:")
# 根據分數排序
by_score = sorted(students, key=lambda s: s['score'])
print("按分數排序:", by_score)

# 根據年齡排序
by_age = sorted(students, key=lambda s: s['age'])
print("按年齡排序:", by_age)

# 找出分數最高的學生
top_student = max(students, key=lambda s: s['score'])
print(f"分數最高的學生: {top_student['name']}，分數: {top_student['score']}")


# ===== 4. 進階：多重排序條件 =====
# 可以使用 tuple 作為 key 的返回值，實現多重排序
# Python 會先比較 tuple 的第一個元素，相同時再比較第二個，以此類推
data = [
    {'dept': 'IT', 'salary': 50000},
    {'dept': 'HR', 'salary': 45000},
    {'dept': 'IT', 'salary': 48000},
    {'dept': 'HR', 'salary': 47000}
]

print("\n多重排序範例:")
# 先按部門排序，部門相同時再按薪水排序
sorted_data = sorted(data, key=lambda x: (x['dept'], x['salary']))
for item in sorted_data:
    print(f"  {item}")

# 先按部門排序，但薪水要降序排列（使用負號）
sorted_data2 = sorted(data, key=lambda x: (x['dept'], -x['salary']))
print("\n部門升序，薪水降序:")
for item in sorted_data2:
    print(f"  {item}")
