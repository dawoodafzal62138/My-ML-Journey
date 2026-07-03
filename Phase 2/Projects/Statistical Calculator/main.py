from stat import * 
import numpy as np
from advance_stats import *





stats = Stats()
adv = AdvanceStats()

RESET   = "\033[0m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"



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




# ---------------- COLORS ---------------- #

def line():
    print(f"{BLUE}{'='*95}{RESET}")

def section(title):
    print()
    line()
    print(f"{MAGENTA}{title:^95}{RESET}")
    line()

# -------------------------------------------------
# Analyze every distribution
# -------------------------------------------------
for name, data in distributions.items():

    weights = np.random.randint(1, 6, len(data))

    section(name.upper())

    # ---------------- BASIC ---------------- #
    print(f"{GREEN}Mean                 :{RESET} {stats.mean(data):.4f}")
    print(f"{GREEN}Median               :{RESET} {stats.median(data):.4f}")
    print(f"{GREEN}Mode                 :{RESET} {stats.mode(data):.4f}")
    print(f"{GREEN}Variance             :{RESET} {stats.variance(data):.4f}")
    print(f"{GREEN}Standard Deviation   :{RESET} {stats.std(data):.4f}")

    sample_var, sample_std = stats.sample_variance_std(data)
    print(f"{GREEN}Sample Variance      :{RESET} {sample_var:.4f}")
    print(f"{GREEN}Sample Std Dev       :{RESET} {sample_std:.4f}")

    skew, skew_text = stats.skewness(data)
    print(f"{YELLOW}Skewness             :{RESET} {skew:.4f} ({skew_text})")

    kurt, kurt_text = stats.kurtosis(data)
    print(f"{YELLOW}Kurtosis             :{RESET} {kurt:.4f} ({kurt_text})")

    ci = stats.confidence_interval(data)
    print(f"{GREEN}95% Confidence Int.  :{RESET} [{ci[0]:.4f}, {ci[1]:.4f}]")

    # ---------------- ADVANCED ---------------- #
    print()
    print(f"{CYAN}{'-'*35} Advanced Statistics {'-'*35}{RESET}")

    cov, relation = adv.covariance(data, data)
    print(f"{CYAN}Covariance           :{RESET} {cov:.4f}")
    print(f"{CYAN}Relationship         :{RESET} {relation}")

    print(f"{CYAN}25th Percentile      :{RESET} {adv.percentile_(data,25):.4f}")
    print(f"{CYAN}50th Percentile      :{RESET} {adv.percentile_(data,50):.4f}")
    print(f"{CYAN}75th Percentile      :{RESET} {adv.percentile_(data,75):.4f}")

    q = adv.quartiles(data)

    print(f"{CYAN}Quartiles{RESET}")
    print(f"    Minimum          : {q[0]:.4f}")
    print(f"    Q1               : {q[1]:.4f}")
    print(f"    Median           : {q[2]:.4f}")
    print(f"    Q3               : {q[3]:.4f}")
    print(f"    Maximum          : {q[4]:.4f}")

    print(f"{CYAN}Interquartile Range  :{RESET} {adv.interquantile_range(data):.4f}")

    print(f"{CYAN}Weighted Mean        :{RESET} {adv.weighted_mean(data, weights):.4f}")

    normalized = adv.min_max_normalization(data)

    print(f"{CYAN}Min-Max Normalization (First 10){RESET}")
    print("   ", np.round(normalized[:10], 4))

line()
print(f"{MAGENTA}{'ALL DISTRIBUTIONS TESTED SUCCESSFULLY':^95}{RESET}")
line()

