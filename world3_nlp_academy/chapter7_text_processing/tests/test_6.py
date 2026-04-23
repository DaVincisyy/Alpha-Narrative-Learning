import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tests.test_base import TestRunner
def run_test():
    runner = TestRunner()
    runner.test("测试", True, "")
    return runner.summary()
if __name__ == "__main__":
    sys.exit(0 if run_test() else 1)
