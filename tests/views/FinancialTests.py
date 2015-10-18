from mmse15project.model.Account import AccountType
from mmse15project.views.Financial import Financial
from tests.views.FrameTests import FrameTests


class FinancialTests:
    def __init__(self):
        self.root = FrameTests(Financial, AccountType(3).name, "name@test.com")

FinancialTests().root.mainloop()
