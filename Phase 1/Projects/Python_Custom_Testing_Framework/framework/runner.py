from .decorators import _test_registry
from .exceptions import TestSkipped , TestFailed

class TestRunner():
    def __init__(self):
        self.results = []

    def run_all(self):
        for test in _test_registry:
            self._run_one(test)  
        self.print_report()

    def _run_one(self , test):
        name = test.__name__
        if not test._skip == None:
            self.results.append(("SKIP" , name , test._skip))
        else:
            try:
                test()
                if test._expect_failure:
                    self.results.append(("FAIL" , name , "Expected to fail but passed"))
                else:
                    self.results.append(("PASS" , name , None))
            except TestFailed as e:
                if test._expect_failure:
                    self.results.append(("XFAIL", name, str(e)))
                else:
                    self.results.append(("FAIL", name, str(e)))

            except TestSkipped as e:
                self.results.append(("SKIP", name, str(e)))

            except Exception as e:
                self.results.append(("ERROR", name, f"{type(e).__name__}: {e}"))

    def _print_report(self):
        passed  = 0
        failed  = 0
        skipped = 0
        xfail   = 0
        errors  = 0
        
        for status, name, message in self.results:
            if status == "PASS":
                print(f"✅ PASS   {name}")
                passed+=1

            elif status == "FAIL":
                print(f"❌ FAIL   {name} — {message}")
                failed+=1

            elif status == "SKIP":
                print(f"⏩ SKIP   {name} — {message}")
                skipped+=1

            elif status == "XFAIL":
                print(f"🟡 XFAIL   {name} — {message}")
                xfail+=1
           
            else :
                print(f"💥 ERROR   {name} — {message}")
                errors+=1
        print(f"{passed} passed | {failed} failed | {skipped} skipped | {xfail} xfail | {errors} errors")