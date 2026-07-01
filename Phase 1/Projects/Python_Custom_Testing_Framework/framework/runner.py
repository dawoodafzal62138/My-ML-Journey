from .decorators import _test_registry
from .exceptions import TestSkipped , TestFailed
from time import perf_counter

BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
GREY ="\033[90m"
RESET = "\033[0m"



class TestRunner():
    def __init__(self):
        self.results = []


    def run_all(self):
        start_time = perf_counter()
     

        for test in _test_registry:
            self._run_one(test)  
        end_time = perf_counter()
        total_time = end_time -  start_time
        self._print_report(total_time)



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

           

            except Exception as e:
                self.results.append(("ERROR", name, f"{type(e).__name__}: {e}"))

    def _print_report(self ,time):
        passed  = 0
        failed  = 0
        skipped = 0
        xfail   = 0
        errors  = 0
        print("-"*60 +"\n")
        for status, name, message in self.results:
            if status == "PASS":
                print(f"\n✅ {BRIGHT_GREEN}PASS{RESET}   {name}")
                passed+=1

            elif status == "FAIL":
                print(f"\n❌ {BRIGHT_RED}FAIL{RESET}   {name}")
                print(f"  ↳ {BRIGHT_RED}{message}{RESET}")
                failed+=1

            elif status == "SKIP":
                print(f"\n⏩ {BRIGHT_BLUE}SKIP{RESET}   {name}")
                print(f"  ↳ {BRIGHT_BLUE}{message}{RESET}")
                skipped+=1

            elif status == "XFAIL":
                print(f"\n🟡 {BRIGHT_YELLOW}XFAIL{RESET}  {name}")
                print(f"  ↳ {BRIGHT_YELLOW}{message}{RESET}")
                xfail+=1
           
            else :
                print(f"\n💥 {BRIGHT_RED}ERROR{RESET}   {name}")
                print(f"  ↳ {BRIGHT_RED}{message}{RESET}")
                errors+=1
        
        print()
        print("="*60)

        if failed != 0:
            print(f"{BRIGHT_RED}\nFIALURE SUMMARY : {RESET}\n")
            for  status , name , msg in self.results:
                if status == "FAIL":
                    print(f"{name}: {msg}")
        if errors != 0:
            print(f"{BRIGHT_RED}\nERRORS SUMMARY : {RESET}\n")
            for  status , name , msg in self.results:
                if status == "ERROR":
                    print(f"{name}: {msg}")
        print()
        print("="*60)



        print()
        print("-"*60)
        print(f"Run {len(self.results)} in {time:.2f}s")
        print(f"{BRIGHT_GREEN}{passed} Passed {RESET}| {BRIGHT_RED}{failed} Failed {RESET}| {BRIGHT_BLUE}{skipped} skipped {RESET}| {BRIGHT_YELLOW}{xfail} xFail {RESET}| {BRIGHT_RED}{errors} errors{RESET}")
        percent = passed/len(self.results)*100
        print(f"{BRIGHT_GREEN}Success Rate : {GREY}{percent:.2f}%{RESET}")
        