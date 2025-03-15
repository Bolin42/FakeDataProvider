from datetime import datetime
import logging
from math import log

# 定义颜色和样式的代码
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"

    # 文字颜色
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # 背景颜色
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


def error(msg):
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Colors.RED + "[-]" + Colors.RESET, end=" ")
    print(" |" + current_time + "| ", end="")
    print(Colors.BOLD + Colors.BG_RED + Colors.WHITE +" ERROR " + Colors.RESET, end=" ")
    print(msg)
    logging.basicConfig(filename= 'Log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.error(msg)
    #print("\n")

def warning(msg):
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Colors.YELLOW + "[!]" + Colors.RESET, end=" ")
    print(" |" + current_time + "| ", end="")
    print(Colors.BOLD + Colors.BG_YELLOW + Colors.WHITE + " WARNING " + Colors.RESET, end=" ")
    print(msg)
    logging.basicConfig(filename= 'Log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning(msg)
    #print("\n")

def info(msg):
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Colors.BLUE + "[*]" + Colors.RESET, end=" ")
    print(" |" + current_time + "| ", end="")
    print(Colors.BOLD + Colors.BG_BLUE + Colors.WHITE + " INFO " + Colors.RESET, end=" ")
    print(msg)
    logging.basicConfig(filename= 'Log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(msg)
    #print("\n")

def success(msg):
    # 获取当前日期和时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Colors.GREEN + "[+]" + Colors.RESET, end=" ")
    print(" |" + current_time + "| ", end="")
    print(Colors.BOLD + Colors.BG_GREEN + Colors.WHITE + " SUCCESS " + Colors.RESET, end=" ")
    print(msg)
    logging.basicConfig(filename= 'Log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(msg)
    #print("\n")

# 示例用法
#error("This is an error message")
#warning("This is a warning message")
#info("This is an info message")
#success("This is a success message")