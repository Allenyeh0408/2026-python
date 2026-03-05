# 8 容器操作、推導式與生成器範例

# ===== 1) List Comprehension（串列推導式） =====
# 目標：從 nums 中「篩選出正數」
nums = [1, -2, 3, -4]

# 語法： [運算式 for 變數 in 可迭代物件 if 條件]
# 這裡的意思是：遍歷 nums，把大於 0 的 n 收集成新串列
positives = [n for n in nums if n > 0]

# 等價的傳統 for 迴圈寫法（方便理解）：
# positives = []
# for n in nums:
#     if n > 0:
#         positives.append(n)


# ===== 2) Dict Comprehension（字典推導式） =====
# 目標：把 (key, value) 配對資料轉成字典
pairs = [('a', 1), ('b', 2)]

# 語法： {key_expr: value_expr for ...}
lookup = {k: v for k, v in pairs}

# 等價的傳統寫法：
# lookup = {}
# for k, v in pairs:
#     lookup[k] = v


# ===== 3) Generator Expression（生成器表達式） =====
# 目標：計算 nums 每個元素平方後的總和

# 這裡 n * n for n in nums 是「生成器表達式」
# 它不會先建立完整串列，而是邊產生邊被 sum() 消費
squares_sum = sum(n * n for n in nums)

# 若寫成 list comprehension：sum([n * n for n in nums])
# 會先建立整個串列，通常比較耗記憶體


# ===== 4) 輸出結果（方便觀察） =====
print(f"原始資料 nums: {nums}")
print(f"篩選後的正數 positives: {positives}")
print(f"pairs 轉成字典 lookup: {lookup}")
print(f"平方總和 squares_sum: {squares_sum}")
