"""
测试基础类 - 所有测试共享
"""

import sys
import codecs

# 设置Windows控制台编码
if sys.platform == 'win32':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class TestRunner:
    """简单的测试运行器"""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.tests = []

    def test(self, name, condition, error_msg=""):
        """运行单个测试"""
        if condition:
            self.passed += 1
            print(f"✅ {name}")
            self.tests.append((name, True, ""))
        else:
            self.failed += 1
            print(f"❌ {name}")
            if error_msg:
                print(f"   错误: {error_msg}")
            self.tests.append((name, False, error_msg))

    def summary(self):
        """打印测试总结"""
        total = self.passed + self.failed
        print("\n" + "=" * 50)
        print(f"测试结果: {self.passed}/{total} 通过")
        print("=" * 50)

        if self.failed > 0:
            print("\n❌ 失败的测试:")
            for name, passed, error in self.tests:
                if not passed:
                    print(f"  - {name}")
                    if error:
                        print(f"    {error}")
        else:
            print("\n🎉 恭喜！测试通过了！")

        return self.failed == 0
