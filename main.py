import json
import os

# 数据文件路径
DATA_FILE = "memo.json"

def init_file():
    """初始化json文件，不存在就创建空列表"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

def add_memo(content):
    """添加备忘录"""
    init_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        memo_list = json.load(f)

    memo_list.append({"id": len(memo_list)+1, "content": content})

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(memo_list, f, ensure_ascii=False, indent=2)
        print("✅ 备忘录添加成功！")

def show_memo():
    """查看所有备忘录"""
    init_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        memo_list = json.load(f)
    
    if not memo_list:
        print("📭 暂无备忘录")
        return
    
    print("\n📋 所有备忘录：")
    for item in memo_list:
        print(f"{item['id']}. {item['content']}")
    print()

def delete_memo(memo_id):
    """根据id删除备忘录"""
    init_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        memo_list = json.load(f)
    
    new_list = [item for item in memo_list if item["id"] != memo_id]
    # 重新排序id
    for idx, item in enumerate(new_list):
        item["id"] = idx + 1
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(new_list, f, ensure_ascii=False, indent=2)
    print("🗑️  删除成功！")

def menu():
    """主菜单"""
    while True:
        print("\n===== 备忘录小工具 =====")
        print("1. 添加备忘录")
        print("2. 查看备忘录")
        print("3. 删除备忘录")
        print("4. 退出程序")
        choice = input("请输入选项(1-4)：")

        if choice == "1":
            text = input("请输入备忘录内容：")
            add_memo(text)
        elif choice == "2":
            show_memo()
        elif choice == "3":
            show_memo()
            try:
                mid = int(input("请输入要删除的编号："))
                delete_memo(mid)
            except ValueError:
                print("❌ 请输入正确数字！")
        elif choice == "4":
            print("👋 退出程序，再见！")
            break
        else:
            print("❌ 输入有误，请重新选择！")

if __name__ == "__main__":
    menu()                