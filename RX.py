import os, sys
os.system("git pull")
try:
    __import__("CK").main_menu()
except Exception as e:
    exit(str(e))
