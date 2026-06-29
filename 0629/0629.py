class BaseWorkflow:
    organization = "NCHU"

    def __init__(self):
        print("步驟 1：初始化基礎流程")

    def execute_core_step(self):
        print("步驟 X：執行核心任務")

    def __del__(self):
        print("最後步驟：釋放資源")


class EnhancedWorkflow(BaseWorkflow):
    current_year = 2026

    def add_extension_step(self):
        print("額外步驟 N：執行擴充任務")


class CustomWorkflow(EnhancedWorkflow):
    def add_extension_step(self):  # 覆寫父類別的方法
        self.execute_core_step()  # 呼叫祖父類別的功能
        print("額外步驟 N-1：自訂前置處理")
        return super().add_extension_step()  # 呼叫父親類別的功能


# ===============================

from datetime import datetime
import math


class ParkingFeeCalculator:
    def __init__(self, time_interval_mins: int, price_per_interval: int):
        """
        :param time_interval_mins: 計費時間區間（分鐘），例如 30 分鐘
        :param price_per_interval: 每個區間的費率（元），例如 10 元
        """
        self.time_interval_mins = time_interval_mins
        self.price_per_interval = price_per_interval
        self.start_time = None
        self.end_time = None

    def _parse_datetime_string(
        self, time_str: str, time_format="%Y/%m/%d %H:%M:%S"
    ) -> datetime:
        """內部工具：將時間字串轉換為 datetime 物件 """
        return datetime.strptime(time_str, time_format)

    def set_start_time(self, time_str: str):
        """設定開始計費時間"""
        self.start_time = self._parse_datetime_string(time_str)

    def set_end_time(self, time_str: str):
        """設定結束計費時間"""
        self.end_time = self._parse_datetime_string(time_str)

    def calculate_total_seconds(self) -> int:
        """計算並回傳兩個時間點之間的總秒數差距 (原 get_time_diff_secs)"""
        if not self.start_time or not self.end_time:
            raise ValueError("請先設定開始與結束時間！")

        # 如果時間順序顛倒，自動調換
        if self.start_time > self.end_time:
            self.start_time, self.end_time = self.end_time, self.start_time

        # 修正原 code 使用 .seconds 跨天會出錯的 Bug，改用 .total_seconds()
        return int((self.end_time - self.start_time).total_seconds())

    def get_total_payment(self) -> int:
        """計算最終應付總金額 (原 get_payment)"""
        total_seconds = self.calculate_total_seconds()
        total_minutes = total_seconds / 60

        # 修正原本混亂的進位邏輯，直接用 math.ceil 實作「不滿一個區間以一個區間計費」
        billable_units = math.ceil(total_minutes / self.time_interval_mins)

        return billable_units * self.price_per_interval


# --- 實際執行測試 ---
# 建立一個「每 30 分鐘 10 元」的收費計算器
fee_calculator = ParkingFeeCalculator(time_interval_mins=30, price_per_interval=10)

# 設定停放時間
fee_calculator.set_start_time("2026/06/29 10:41:00")
fee_calculator.set_end_time("2026/06/29 11:45:00")

# 計算費用並列印
total_fee = fee_calculator.get_total_payment()
print(f"計算完成！總停車費用為：{total_fee} 元")
