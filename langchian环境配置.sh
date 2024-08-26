#!/bin/bash

# 一、创建虚拟环境

# 输出 Python 版本
echo "Checking Python version..."
python -V

# 创建虚拟环境
echo "Creating virtual environment '_pvenv_'..."
python -m venv _pvenv_

# 激活虚拟环境
echo "Activating virtual environment..."
source _pvenv_/bin/activate

# 升级 pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# 二、安装库

echo "Installing required libraries..."
pip install langchain==0.2.7 \
langchain-community==0.2.7 \
langchain-aws==0.1.11 \
langchain-openai==0.1.16 \
langchainhub==0.1.20 \
chromadb==0.5.4 \
wikipedia==1.4.0 \
tavily-python==0.3.5 \
python-dotenv==1.0.1

# 三、生成环境文件

echo "Creating '.env' file..."
cat << EOF > .env
OPENAI_API_KEY=123
TAVILY_API_KEY=456
ANTHROPIC_API_KEY=789
GOOGLE_API_KEY=XYZ
EOF

# 四、编辑程序（此步骤为手动步骤提示）

echo "Edit your Python files 'common.py' and 'main.py' as needed."
echo "You can use the following commands:"
echo "nano common.py"
echo "nano main.py"

# 五、运行程序（此步骤为手动步骤提示）

echo "After editing, you can run your Python program using:"
echo "python main.py"

# 提示脚本完成
echo "Setup script completed. Please edit and run your Python programs as needed."