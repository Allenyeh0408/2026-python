# AI_LOG

## 我問 AI 什麼

> 請幫我為 digit_root(n) 寫 unittest 測試，至少 3 個案例，要包含 edge case 與例外案例。

## AI 給了什麼

AI 提供了三個方向：多位數基本案例、單位數 edge case、以及 n < 1 的例外案例，並提醒我例外訊息要對齊題目規格。

## 我改了什麼

我把測試改成直接檢查題目指定的 ValueError("n must be >= 1")，並確認 edge case 用單位數直接回傳；實作檔則用迴圈反覆加總各位數直到剩下一位數，與測試和題目範例一致。