import os
import sys
import time
import platform
import traceback


class ConsoleTool(object):
    def __init__(self):
        pass

    @staticmethod
    def check_platform():
        check_result = platform.system()
        if "indows" in check_result:
            return "W"
        elif "inux" in check_result:
            return "L"

    def console_clear(self):
        sysinfo = self.check_platform()
        if sysinfo == "W":
            os.system("cls")
            return
        elif sysinfo == "L":
            os.system("clear")
            return
        os.system("cls")


class Adb(object):
    def __init__(self):
        print("[+] 初始化……")

    def press(self, _key):
        sys.stdout.write(_key)
        sys.stdout.flush()
        if _key == "\n":
            time.sleep(sleeptime_line)
        elif _key == " ":
            time.sleep(sleeptime_blank)
        elif _key == "-":
            time.sleep(sleeptime_cust)
        elif _key == "1":
            self.tap_1()
        elif _key == "2":
            self.tap_2()
        elif _key == "3":
            self.tap_3()
        elif _key == "4":
            self.tap_4()
        elif _key == "5":
            self.tap_5()
        elif _key == "6":
            self.tap_6()
        elif _key == "7":
            self.tap_7()
        elif _key == "8":
            self.tap_high_1()
        elif _key == "9":
            self.tap_high_2()
        elif _key == "*":
            self.tap_high_3()
        elif _key == "0":
            self.tap_high_4()
        elif _key == "#":
            self.tap_high_5()
        else:
            pass

    @staticmethod
    def restart_server():
        os.system("adb kill-server")
        os.system("adb start-server")
        time.sleep(1)
        Tool.console_clear()

    @staticmethod
    def check_device():
        os.system("adb devices")
        input("[+] 确保列表中有你的设备\n    然后按下 Enter键 继续……:")

    @staticmethod
    def tap_1():
        os.system("adb shell input tap 185 1000")

    @staticmethod
    def tap_2():
        os.system("adb shell input tap 550 1000")

    @staticmethod
    def tap_3():
        os.system("adb shell input tap 900 1000")

    @staticmethod
    def tap_4():
        os.system("adb shell input tap 185 1200")

    @staticmethod
    def tap_5():
        os.system("adb shell input tap 540 1200")

    @staticmethod
    def tap_6():
        os.system("adb shell input tap 900 1200")

    @staticmethod
    def tap_7():
        os.system("adb shell input tap 180 1380")

    @staticmethod
    def tap_high_1():
        # 拨号键 8
        os.system("adb shell input tap 540 1380")

    @staticmethod
    def tap_high_2():
        # 拨号键 9
        os.system("adb shell input tap 900 1380")

    @staticmethod
    def tap_high_3():
        # 拨号键 *
        os.system("adb shell input tap 180 1590")

    @staticmethod
    def tap_high_4():
        # 拨号键 0
        os.system("adb shell input tap 540 1590")

    @staticmethod
    def tap_high_5():
        # 拨号键 #
        os.system("adb shell input tap 900 1590")


def read_from_file():
    global sheet
    if os.path.exists("./sheet.txt"):
        with open("./sheet.txt", "r") as file_sheet:
            text = file_sheet.read()
        sheet = list(text)
        print("[+] 从文件加载成功\n")
        return
    else:
        print("[#] 未发现 sheet.txt")
        return


def check_adb_port():
    sysinfo = Tool.check_platform()
    print("[+] 检查端口占用情况……：")
    if sysinfo == "W":
        os.system('netstat -ano |findstr "5037"')
    elif sysinfo == "L":
        os.system("lsof -i :5037")
    else:
        os.system('netstat -ano |findstr "5037"')
    input("\n[+] 建议结束占用5037端口的进程（通常是手机助手）\n    然后按 Enter键 继续:")
    Tool.console_clear()


def run():
    os.chdir(sys.path[0])
    read_from_file()  # 从文本文档中读取“乐谱”，赋值给 sheet
    check_adb_port()
    os.chdir(sys.path[0] + "/adb-tools")
    Adb.restart_server()
    Adb.check_device()
    for key in sheet:
        Adb.press(key)
        time.sleep(sleeptime_two)


if __name__ == '__main__':
    # Some variables
    sheet = list("89*#9 6789*0* *9*#9 6787653 89*#9 6789*0* *88*9 7876")
    sleeptime_two = 0.06  # 相邻两个音符之间的时间间隔
    sleeptime_blank = 0.5  # 一个空格代表的时间间隔
    sleeptime_line = 1.5  # 两行“乐谱”之间的时间间隔
    sleeptime_cust = 0.02  # 自定义间隔，在“乐谱”中用 - 表示
    try:
        Tool = ConsoleTool()
        Adb = Adb()
        run()
    except KeyboardInterrupt:
        print("\n\n[!] Raised KeyboardInterrupt , Exit!")
        sys.exit()
    except Exception:
        print("\n\n[!] Error !\n")
        traceback.print_exc()
