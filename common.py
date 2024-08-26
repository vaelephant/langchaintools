import os 
import time
#打印环境变量

def printENV():
#获取所有环境变量
    env_vars = os. environ
    # 打印所有环境变量
    print("环境变量:")
    print("-"*20)
    for key, value in env_vars.items():
        
        if key in ["'OPENAI__API_KEY", "TAVILY_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]:
            
            print(f"{key}: {value}")
          
    print("-"*20)

# 计算程序运行时间

def evalEndTime(start_time):
    end_time = time.time() # 获取结束时间
    execution_time = "（程序运行时间：%.2f秒）" % (
        end_time - start_time
    )
    return execution_time