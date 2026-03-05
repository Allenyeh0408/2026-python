# 10 模組、類別、例外與 Big-O（最低門檻）範例

# ===== 1. 模組導入 (Import) =====
# Python 有許多內建模組，collections 是其中之一
# deque (double-ended queue) 是一個雙向佇列，可以從兩端快速新增/刪除元素
from collections import deque

# ===== 2. deque 的使用 =====
# deque 是一個佇列(queue)資料結構，支援從兩端操作
# maxlen=2 表示這個佇列最多只能存放 2 個元素
q = deque(maxlen=2)
print("建立一個最大長度為 2 的 deque")

# 從右邊加入元素（類似 list 的 append）
q.append(1)
print(f"加入 1: {q}")  # 輸出: deque([1], maxlen=2)

q.append(2)
print(f"加入 2: {q}")  # 輸出: deque([1, 2], maxlen=2)

q.append(3)  # 自動丟掉最舊的元素（左邊的 1）
print(f"加入 3: {q}")  # 輸出: deque([2, 3], maxlen=2)
print("當佇列滿了，新加入的元素會自動擠掉最舊的元素\n")

# deque 的其他常用操作：
q2 = deque([1, 2, 3])
q2.appendleft(0)  # 從左邊加入
print(f"appendleft(0): {q2}")  # deque([0, 1, 2, 3])

q2.pop()  # 從右邊移除並返回
print(f"pop(): {q2}")  # deque([0, 1, 2])

q2.popleft()  # 從左邊移除並返回
print(f"popleft(): {q2}\n")  # deque([1, 2])


# ===== 3. 類別 (Class) 定義 =====
# 類別是物件導向程式設計的基礎，用來建立自訂的資料型別

class User:
    """使用者類別範例"""
    
    # __init__ 是建構子(constructor)，在建立物件時自動執行
    # self 代表物件本身（類似其他語言的 this）
    # user_id 是參數
    def __init__(self, user_id):
        # self.user_id 是物件的屬性(attribute)
        self.user_id = user_id
        print(f"建立了一個 User 物件，ID = {user_id}")

# 建立 User 類別的實例（物件）
u = User(42)  # 會自動呼叫 __init__(self, 42)

# 存取物件的屬性
uid = u.user_id
print(f"使用者 ID: {uid}\n")

# 更完整的類別範例：
class Student:
    """學生類別，包含多個屬性和方法"""
    
    def __init__(self, name, age, grade):
        self.name = name      # 姓名
        self.age = age        # 年齡
        self.grade = grade    # 年級
    
    # 定義方法(method)
    def introduce(self):
        """自我介紹方法"""
        return f"我是 {self.name}，{self.age} 歲，{self.grade} 年級"
    
    def study(self, subject):
        """學習方法"""
        return f"{self.name} 正在學習 {subject}"

# 使用 Student 類別
s = Student("小明", 18, "大一")
print(s.introduce())
print(s.study("Python"))
print()


# ===== 4. 例外處理 (Exception Handling) =====
# 例外處理用來捕捉和處理程式執行時可能發生的錯誤

def is_int(val):
    """
    檢查一個值是否可以轉換成整數
    
    Args:
        val: 要檢查的值
        
    Returns:
        bool: 可以轉換則返回 True，否則返回 False
    """
    try:
        # try 區塊：放入可能會出錯的程式碼
        int(val)  # 嘗試將 val 轉換成整數
        return True
    except ValueError:
        # except 區塊：當發生 ValueError 例外時執行
        # ValueError 是轉換失敗時會拋出的例外
        return False

# 測試 is_int 函式
print("例外處理測試:")
print(f"is_int('123'): {is_int('123')}")      # True
print(f"is_int('abc'): {is_int('abc')}")      # False
print(f"is_int('12.5'): {is_int('12.5')}")    # False
print(f"is_int(456): {is_int(456)}")          # True
print()

# 更多例外處理範例：
def divide(a, b):
    """安全的除法運算"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        # 捕捉除以零的錯誤
        print("錯誤：不能除以零！")
        return None
    except TypeError:
        # 捕捉型別錯誤
        print("錯誤：輸入的型別不正確！")
        return None

print("除法測試:")
print(f"divide(10, 2) = {divide(10, 2)}")      # 5.0
print(f"divide(10, 0) = {divide(10, 0)}")      # None (並顯示錯誤訊息)
print(f"divide(10, 'a') = {divide(10, 'a')}")  # None (並顯示錯誤訊息)
print()


# ===== 5. Big-O 時間複雜度概念 =====
# Big-O 表示法用來描述演算法的執行時間如何隨著輸入大小增長
# 這是演算法效率的重要指標

print("Big-O 時間複雜度概念：\n")

# O(1) - 常數時間：無論資料量多大，執行時間都固定
# 範例：list.append()、字典的查詢
my_list = [1, 2, 3]
my_list.append(4)  # O(1) - 在列表末端加入元素，非常快速
print(f"list.append() 是 O(1): {my_list}")

my_dict = {'a': 1, 'b': 2}
value = my_dict.get('a')  # O(1) - 字典查詢也是 O(1)
print(f"字典查詢是 O(1): {value}")

# O(N) - 線性時間：執行時間與資料量成正比
# 範例：list 切片、迴圈遍歷
my_list_slice = my_list[1:3]  # O(N) - 需要複製 N 個元素
print(f"list 切片是 O(N): {my_list_slice}")

# 遍歷列表也是 O(N)
total = sum(my_list)  # O(N) - 需要遍歷所有元素
print(f"sum() 遍歷列表是 O(N): {total}")

# O(N²) - 平方時間：巢狀迴圈
# 範例：氣泡排序
def bubble_sort_example(arr):
    """氣泡排序範例 (O(N²))"""
    n = len(arr)
    for i in range(n):        # 外層迴圈 N 次
        for j in range(n-1):  # 內層迴圈 N 次
            pass  # 簡化範例
    # 總共執行 N × N = N² 次

print("\n常見的 Big-O 複雜度（從快到慢）:")
print("  O(1)      - 常數時間：字典查詢、list.append()")
print("  O(log N)  - 對數時間：二元搜尋")
print("  O(N)      - 線性時間：list 切片、遍歷、sum()")
print("  O(N log N)- 線性對數時間：高效排序（merge sort、quick sort）")
print("  O(N²)     - 平方時間：巢狀迴圈、氣泡排序")
print("  O(2^N)    - 指數時間：某些遞迴演算法（應避免）")

print("\n💡 實用建議：")
print("  • 優先使用 O(1) 和 O(N) 的操作")
print("  • 避免不必要的巢狀迴圈")
print("  • 使用字典而非列表做查詢（O(1) vs O(N)）")
print("  • 了解內建函式的複雜度")


# ===== 6. 實戰應用範例 =====
print("\n\n實戰應用範例：")
print("=" * 50)

# 結合所有概念：使用 deque 實現最近使用記錄
from collections import deque

class RecentHistory:
    """最近歷史記錄類別"""
    
    def __init__(self, max_size=5):
        self.history = deque(maxlen=max_size)
    
    def add(self, item):
        """加入新項目"""
        self.history.append(item)
    
    def get_recent(self):
        """取得最近的記錄"""
        return list(self.history)
    
    def clear(self):
        """清空歷史"""
        self.history.clear()

# 使用範例
history = RecentHistory(max_size=3)
history.add("訪問首頁")
history.add("登入")
history.add("查看商品A")
history.add("查看商品B")
history.add("加入購物車")  # 超過 3 個，會自動移除最舊的

print(f"\n最近的瀏覽記錄: {history.get_recent()}")
print("（自動保留最新的 3 筆記錄）")
