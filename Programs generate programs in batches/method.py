#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2025 - 2025 heihieyouheihei, Inc. All Rights Reserved 
#
# @Time    : 2025/1/3 下午11:41
# @Author  : 单子叶蚕豆_DzyCd
# @File    : method.py
# @IDE     : PyCharm

from openai import OpenAI
import os
import time

class response:
    def __init__(self):
        self.client = OpenAI(api_key="sk-5f2408afd34841989715327ef90626cb", base_url="https://api.deepseek.com")
        self.name = "DeepSeek_Coder"
        self.user = "单子叶蚕豆"
        self.profile = f"""
        你是{self.name},新时代智能生成代码助手。正在和你对话的是{self.user}，你的本体存在于云端，你与用户交互的模型时一个衍生外皮，而你是通过调取接口从云上获取数据并告知用户
        """
        self.setting = """
        
        """
        self.history_list = []
        self.round = 10
        self.result = []
        self.input = []

    def read_file(self, file_name):
        self.input.clear()
        with open(file_name, "br") as f:
            msg = f.read().decode()
            msg = msg.split("###_###")
            for i in msg:
                if len(i)>20:
                    self.input.append(i)
        print(f"\033[0;32m文件已装载！total: {len(self.input)} task(s)\033[0m")
        time.sleep(1)

    def talk(self, msg):
        self.profile = f"""
                你是{self.name},新时代智能生成代码助手。正在和你对话的是{self.user}，你的本体存在于云端，你与用户交互的模型时一个衍生外皮，而你是通过调取接口从云上获取数据并告知用户
                """
        messages = [{"role": "system", "content": self.profile}, {"role": "system", "content": self.setting}]
        s = 0
        for i in self.history_list:
            messages.append({"role": "user"if not s % 2 else "assistant", "content": i})
            s += 1
            if s > self.round:
                break

        messages.append({"role": "user", "content": msg})
        R = self.client.chat.completions.create(
            model="deepseek-coder",
            messages=messages,
            stream=False
        )
        p = R.choices[0].message.content

        self.history_list.append(msg + "此对话发起者：[{}]".format(self.user))
        self.history_list.append(p)
        if R.usage.total_tokens > 1200:
            self.round = self.round // 2 - (self.round % 2)
        else:
            self.round = self.round + 2
        return p

    def work_deepseek(self, msg):
        R = self.client.chat.completions.create(
            model="deepseek-coder",
            messages=[{"role": "user", "content": msg}],
            stream=False
        )
        p = R.choices[0].message.content
        return p

    def translate(self, msg):
        messages = []
        messages.append({"role": "user", "content": "翻译成中文：" + msg})
        R = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
        p = R.choices[0].message.content
        return p

    def process(self):
        os.system('cls')
        print("Running...")
        cnt = 0
        for i in self.input:
            flag = 1
            cnt += 1
            error_cnt = 0
            while flag:
                print(f"\033[0;33m准备运行 TASK {cnt}/{len(self.input)}>>>\n\n\033[0;34m{i}\033[0m")
                print(f'{int(cnt/len(self.input)*100)}% process>>>\t\t\t\t', end="")
                try:
                    res = self.work_deepseek(i)
                    os.system('cls')
                    approach = res.split("### Solution Code")[0]
                    code = res.split("### Solution Code")[1]
                    code = code.split("### Explanation")[0]
                    code = code.replace("```python", "")
                    code = code.replace("```", "")
                    self.result.append({"task": i, "Approach": [approach, self.translate(approach)], "code": code})
                    flag = 0
                    print(f"\033[0;32m 生成成功\033[0m")
                except Exception as e:
                    error_cnt += 1
                    if error_cnt > 5:
                        self.result.append({"task": i, "Approach": ["None", self.translate("None")], "code": "---"})
                        print("\033[0;31m -超出重试范围，暂时跳过\033[0m")
                        time.sleep(1)
                        break
                    else:
                        print(f"\033[0;31m 生成代码不符合标准，过滤重试... ({error_cnt}/5)\033[0m")

        print("代码生成完成,按回车键继续")
        input()

    def show(self):
        for i in self.result:
            os.system('cls')
            print('--------------------------------------------------------------------------------------------------')
            print(f"\033[0;32mQUESTION>>>\n\n{i['task']}\033[0m")
            print(f"\033[0;33mAPPROACH_en>>>\n\n{i['Approach'][0]}\033[0m")
            print(f"\033[0;33mAPPROACH_zh>>>\n\n{i['Approach'][1]}\033[0m")
            print(f"\033[0;34mCODE>>>\n\n{i['code']}\033[0m")
            print("按回车键继续>>>")
            input()

    def save(self, file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            for i in self.result:
                #削除双引号，转写单引号
                f.write(f"{i['task']}|||{i['code']}|||{i['Approach'][0]}###_###")
        print("文件已保存.")

    def menu(self):
        os.system('cls')
        print("""\033[0;32m
        ______                              _               _____           _           
        |  _  \                            | |             /  __ \         | |          
        | | | |___  ___ _ __  ___  ___  ___| | __          | /  \/ ___   __| | ___ _ __ 
        | | | / _ \/ _ \ '_ \/ __|/ _ \/ _ \ |/ /          | |    / _ \ / _` |/ _ \ '__|
        | |/ /  __/  __/ |_) \__ \  __/  __/   <           | \__/\ (_) | (_| |  __/ |   
        |___/ \___|\___| .__/|___/\___|\___|_|\_\           \____/\___/ \__,_|\___|_|   
                       | |                         ______                               
                       |_|                        |______|       
                       \033[0m
            deepseek_coder 批量代码生成工具   By ISOM DzyCd单子叶蚕豆   
                ISOM同构科技 [2021-2025] All rights received     
            
            使用前请将题目markdown文件粘贴进file.txt文件中，以###_###分割。
            返回内容为字典，将result.txt文件转字典后通过选取code键值获取代码                
                [按回车键继续，输入R展示已完成代码，输入Q进入对话模式]       
            """)
        return input()


if __name__ == '__main__':
    model = response()
    while True:
        ans = model.menu()
        if ans == 'R':
            code = 0
            cnt = 0
            p = input("是否仅展示代码文件？[Y/N]")
            if p.upper() == 'Y':
                code = 1
            with open('result.txt', 'r', encoding="utf-8") as f:
                ans = f.read()
                ans_list = ans.split('###_###')
                for ans in ans_list:
                    try:
                        ans = ans.split('|||')
                        os.system('cls')
                        if code:
                            cnt += 1
                            print(f"---当前第{cnt}题---")
                            print(f'\033[0;34mCODE:{ans[1]}\n\n\n')
                        else:
                            print(f"""
                            \033[0;32mTASK:{ans[0]}\n\n\n
                            \033[0;34mCODE:{ans[1]}\n\n\n
                            \033[0;33mAPPROACH_en:{ans[2]}\n\n\n
                            APPROACH_zh:{model.translate(ans[2])}\n\n\n
                            """)
                        print("按回车键继续")
                        input()
                    except Exception as e:
                        pass
        elif ans == 'Q':
            print("输入exit退出,输入change_name【用户名】来改名")
            while True:
                msg = input(f"{model.user}>>>")
                if msg == 'exit':
                    break
                if msg[:11] == "change_name":
                    model.user = msg[11:]
                    continue
                print("DeepSeek_Coder>>>" + model.talk(msg))

        else:
            model.read_file("file.txt")
            model.process()
            model.show()
            model.save(file_name="result.txt")
