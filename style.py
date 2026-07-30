
# Stop-Process -Name python -Force
# jupyter notebook --no-browser --port=8888
# pkill -f jupyter-notebook
# jupyter notebook list


# ==========================================
# RESET (Crucial to stop color bleeding)
# ==========================================
RESET = "\033[0m"

# ==========================================
# STANDARD FOREGROUND COLORS
# ==========================================
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY ="\033[90m"

# ==========================================
# HIGH INTENSITY (BRIGHT) FOREGROUND COLORS
# ==========================================
BRIGHT_BLACK = "\033[90m"   
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# ==========================================
# STANDARD BACKGROUND COLORS
# ==========================================
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# ==========================================
# HIGH INTENSITY BACKGROUND COLORS
# ==========================================
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

# ==========================================
# TEXT FORMATTING / STYLES
# ==========================================
BOLD = "\033[1m"
DIM = "\033[2m"             # Faint text
ITALIC = "\033[3m"          # Not widely supported in all terminals
UNDERLINE = "\033[4m"
BLINK = "\033[5m"           # Slow blink
REVERSE = "\033[7m"         # Swaps foreground and background colors
HIDDEN = "\033[8m"          # Invisible text (useful for passwords)
STRIKETHROUGH = "\033[9m"   # Not widely supported




