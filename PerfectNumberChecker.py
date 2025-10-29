class PerfectNumberChecker:
    def __init__(self, number):
        """Initialize with given number"""
        self.number = number

    def is_perfect(self):
        """Check if number is perfect"""
        if self.number <= 1:
            return False
        
        divisors_sum = 0
        for i in range(1, self.number):
            if self.number % i == 0:
                divisors_sum += i
        return divisors_sum == self.number

    def show_result(self):
        """Display result"""
        if self.is_perfect():
            print(f"✅ {self.number} is a Perfect Number!")
        else:
            print(f"❌ {self.number} is NOT a Perfect Number.")


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    checker = PerfectNumberChecker(num)
    checker.show_result()
