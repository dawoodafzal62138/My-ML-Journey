from stat import * 




import numpy as np
from stats import Stats      # Import your Stats class

stats = Stats()

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"


np.random.seed(42)

distributions = {
    "Normal Distribution": np.random.normal(0, 1, 1000),

    "Uniform Distribution": np.random.uniform(0, 1, 1000),

    "Exponential Distribution": np.random.exponential(1, 1000),

    "Binomial Distribution": np.random.binomial(10, 0.5, 1000),

    "Poisson Distribution": np.random.poisson(4, 1000),

    "Chi-Square Distribution": np.random.chisquare(4, 1000),

    "Gamma Distribution": np.random.gamma(2, 2, 1000),

    "Beta Distribution": np.random.beta(2, 5, 1000),

    "Log-Normal Distribution": np.random.lognormal(0, 0.5, 1000),

    "Triangular Distribution": np.random.triangular(0, 5, 10, 1000),
}


def line():
    print(f"{BLUE}{'='*80}{RESET}")

line()
print(f"{MAGENTA}{'STATISTICAL FUNCTIONS TEST':^80}{RESET}")
line()

for name, data in distributions.items():

    skew_value, skew_text = stats.skewness(data)
    kurt_value, kurt_text = stats.kurtosis(data)
    ci = stats.confidence_interval(data)

    print(f"\n{CYAN}{name:^80}{RESET}")
    print("-"*80)

    print(f"{GREEN}Mean                :{RESET} {stats.mean(data):10.4f}")
    print(f"{GREEN}Median              :{RESET} {stats.median(data):10.4f}")
    print(f"{GREEN}Mode                :{RESET} {stats.mode(data):10.4f}")
    print(f"{GREEN}Standard Deviation  :{RESET} {stats.std(data):10.4f}")
    print(f"{GREEN}Variance            :{RESET} {stats.variance(data):10.4f}")

    print(f"{YELLOW}Skewness            :{RESET} {skew_value:10.2f}   ({skew_text})")
    print(f"{YELLOW}Kurtosis            :{RESET} {kurt_value:10.2f}   ({kurt_text})")

    print(
        f"{GREEN}95% Confidence Int. :{RESET} "
        f"\t[{ci[0]:.4f}, {ci[1]:.4f}]"
    )

line()
print(f"{MAGENTA}{'ALL TESTS COMPLETED':^80}{RESET}")
line()

