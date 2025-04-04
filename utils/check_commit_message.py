import re
import sys

def check_commit_message(file_path):
    with open(file_path, 'r') as f:
        message = f.read().strip()

    # 简单的提交信息规范检查
    # 例如：提交信息必须以 (feat|fix|docs|style|refactor|test|chore) 开头
    pattern = r'^(feat|fix|docs|style|refactor|test|chore)\(.*\): .*$'
    if not re.match(pattern, message):
        print("提交信息不符合规范！")
        print("规范示例：feat(user): add login functionality")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_commit_message.py <commit-msg-file>")
        sys.exit(1)

    check_commit_message(sys.argv[1])
