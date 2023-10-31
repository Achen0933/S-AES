import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from encryption import encryption
from decryption import decryption
from ASCII import encryption_ascii, decryption_ascii


# 创建主窗口
# 验证输入的函数
def validate_input1():
    # 获取密钥的输入内容
    input_text1 = plain_entry.get()
    input_text2 = cipher_entry.get()

    # 检查输入是否为二进制且长度为16
    if not is_binary(input_text2) or len(input_text2) != 16:
        messagebox.showerror("错误", "请输入一个长度为16的二进制密钥")
    elif len(input_text1) != 0:
        if not is_binary(input_text1) or len(input_text1) != 16:
            messagebox.showerror("错误", "请输入一个长度为16的二进制明文")
        else:
            output_text.delete(1.0, tk.END)
            result = encryption(plain_entry.get(), cipher_entry.get())
            result = "加密结果:" + result
            output_text.insert(tk.END, result + "\n")
            result1 = encryption_ascii(asc_plain.get(), cipher_entry.get())
            result1 = "ASCII加密结果：" + result1
            output_text.insert(tk.END, result1 + "\n")

    else:
        output_text.delete(1.0, tk.END)
        result1 = encryption_ascii(asc_plain.get(), cipher_entry.get())
        result1 = "ASCII加密结果：" + result1
        output_text.insert(tk.END, result1 + "\n")

def validate_input2():
    # 获取密钥的输入内容
    input_text3 = key_entry1.get()
    input_text4 = plain_entry1.get()

    # 检查输入是否为二进制且长度为16
    if not is_binary(input_text3) or len(input_text3) != 16:
        messagebox.showerror("错误", "请输入一个长度为16的二进制密钥")
    # 检查输入是否为二进制且长度为16
    elif len(input_text4) != 0:
        if not is_binary(input_text4) or len(input_text4) != 16:
            messagebox.showerror("错误", "请输入一个长度为16的二进制密文")
        else:
            output_text1.delete(1.0, tk.END)
            result = decryption(plain_entry1.get(), key_entry1.get())
            result = "解密结果:" + result
            output_text1.insert(tk.END, result + "\n")
            result1 = decryption_ascii(asc_cipher.get(), key_entry1.get())
            result1 = "ASCII解密结果：" + result1
            output_text1.insert(tk.END, result1 + "\n")
    else:
        output_text1.delete(1.0, tk.END)
        result1 = decryption_ascii(asc_cipher.get(), key_entry1.get())
        result1 = "ASCII解密结果：" + result1
        output_text1.insert(tk.END, result1 + "\n")

# 检查字符串是否为二进制
def is_binary(s):
    return all(bit == '0' or bit == '1' for bit in s)


root = tk.Tk()
root.title("S-AES")
root.geometry("400x300+450+180")
root.configure(background="lightblue")

# 创建选项卡控件
notebook = ttk.Notebook(root)

# 创建选项卡1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="加密")
# 在选项卡1中添加内容
label1 = tk.Label(tab1, text="请输入16位二进制密钥，如：1111111111111111")
label1.pack()
cipher_entry = tk.Entry(tab1)
cipher_entry.pack()
label2 = tk.Label(tab1, text="请输入16位二进制明文，如：1111111111111111")
label2.pack()
plain_entry = tk.Entry(tab1)
plain_entry.pack()
label5 = tk.Label(tab1, text="请输入ASCII编码字符串明文，如：abc")
label5.pack()
asc_plain = tk.Entry(tab1)
asc_plain.pack()
# 确定按钮
button1 = tk.Button(tab1, text="加密", command=validate_input1)
button1.pack()
# 创建一个输出文本框
output_text = tk.Text(tab1, wrap=tk.WORD, width=40, height=6)
output_text.pack()


# 创建选项卡2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="解密")

# 在选项卡2中添加内容
label3 = tk.Label(tab2, text="请输入16位二进制密钥，如：1111111111111111")
label3.pack()
key_entry1 = tk.Entry(tab2)
key_entry1.pack()
label4 = tk.Label(tab2, text="请输入16位二进制密文，如：1111111111111111")
label4.pack()
plain_entry1 = tk.Entry(tab2)
plain_entry1.pack()
label6 = tk.Label(tab2, text="请输入ASCII编码字符串密文，如：abc")
label6.pack()
asc_cipher = tk.Entry(tab2)
asc_cipher.pack()
# 确定按钮
button2 = tk.Button(tab2, text="解密", command=validate_input2)
button2.pack()
# 创建一个输出文本框
output_text1 = tk.Text(tab2, wrap=tk.WORD, width=40, height=6)
output_text1.pack()

# 将选项卡控件放入主窗口
notebook.pack()

# 进入事件循环
root.mainloop()
