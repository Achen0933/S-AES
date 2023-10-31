# S-AES
TiMi小组S-AES实现
# TiMi小组S-AES1-5关测试结果

成员：戴静、陈晓阳

## **第1关：基本测试**

本小组GUI主界面如下：

![image1](https://github.com/Achen0933/S-AES/assets/147233663/ce85ff45-6b50-487e-803c-1dd3bb48fcfd)

![image2](https://github.com/Achen0933/S-AES/assets/147233663/e2ab8750-bda9-4568-849e-2cab4f0a467b)

输入部分：加密选项卡输入16-bit的密钥、16-bit的明文（ASCII编码明文详见第3关）；

解密选项卡输入加密选项卡输入16-bit的密钥、16-bit的密文（和ASCII编码密文）。

输出结果：加密选项卡输入密钥和明文后点击加密，文本框显示加密后的密文；解密选项卡输入密钥和密文后点击解密，文本框显示解密后的明文。

![image3](https://github.com/Achen0933/S-AES/assets/147233663/7abe2b05-d50d-48ab-969f-2fddcb0f6380)

![image4](https://github.com/Achen0933/S-AES/assets/147233663/bfba722c-dfa7-4550-85b3-1af547916483)


由上两图可见，加密前的明文和解密后的明文保持一致，说明加解密过程无误。第1关测试完成。

## **第2关：交叉测试**

本小组与窦一冉组、鲁梦瑶组、唐豪组进行交叉测试。

测试明文：1111000011110000

测试密钥：1100111101011100

本组结果：

<img width="302" alt="image5" src="https://github.com/Achen0933/S-AES/assets/147233663/b1faed47-32e2-4374-9f93-49fae4c854dd">


<img width="301" alt="image6" src="https://github.com/Achen0933/S-AES/assets/147233663/a5fc615a-0e69-4575-9295-21b990107a68">


窦一冉组结果（加密）：

![image7](https://github.com/Achen0933/S-AES/assets/147233663/5f2361df-c3b0-4739-b6c9-a412ad284dc2)


鲁梦瑶组结果（解密）：

![image8](https://github.com/Achen0933/S-AES/assets/147233663/76465b81-d0d6-408b-bd71-259cc4a83696)


唐豪组结果（加密）：

![image9](https://github.com/Achen0933/S-AES/assets/147233663/3c162225-ed11-4c0e-a3ea-bb830628d9e9)


由上面四组加密结果截图可见，加密后密文均为1001000101100100，解密后明文仍为1111000011110000，符合交叉测试的通过要求。第2关测试完成。

## **第3关：扩展功能**

考虑到向实用性扩展，加密算法的数据输入可以是ASII编码字符串(分组为2
Bytes)，对应地输出也可以是ASCII字符串(很可能是乱码)。本组成功实现了该扩展功能，具体方法如下：将ASCII字符串转化为二进制字符串，并以2
Bytes为一组对该二进制字符串进行循环加密，得到加密后的二进制字符串密文。随后将二进制字符串密文重新转化为ASCII字符串输出。解密同理。

输入部分：加密选项卡输入16-bit的密钥和ASCII编码明文；

解密选项卡输入加密选项卡输入16-bit的密钥和ASCII编码密文。

输出结果：加密选项卡输入密钥和ASCII明文后点击加密，文本框显示加密后的ASCII密文；解密选项卡输入密钥和ASCII密文后点击解密，文本框显示解密后的ASCII明文。

![image10](https://github.com/Achen0933/S-AES/assets/147233663/49858eec-6bcb-4f2c-b606-1c676fe8318c)


![image11](https://github.com/Achen0933/S-AES/assets/147233663/5a7dffbc-8784-4fd5-a79d-224938db8385)


由上两图可见，加密前的明文和解密后的明文保持一致，说明加解密过程无误。第3关测试完成。

**综合第1关和第3关，本组的GUI实现了普通16-bit二进制字符串和ASCII编码字符串的同时加\\解密，并可以同时显示加\\解密结果。效果如下：**

![image12](https://github.com/Achen0933/S-AES/assets/147233663/343d8ea0-ff83-4c1a-ba97-824f304ae244)


![image13](https://github.com/Achen0933/S-AES/assets/147233663/7cc468e5-4878-413e-92d7-321525b24b9e)


## **第4关：多重加密**

**4.1 双重加密**

将S-AES算法通过双重加密进行扩展，分组长度仍然是16 bits，但密钥长度为32
bits。

本组使用Key(K1+K2)的32-bit密钥，使用两重encryption函数进行双重加密，效果如下：

<img width="399" alt="image14" src="https://github.com/Achen0933/S-AES/assets/147233663/1b24e154-63f9-4c6e-8af2-2214fbc45b40">


**4.2 中间相遇攻击**

我们使用已知的使用相同密钥的明、密文对(一个或多个)，使用中间相遇攻击的方法进行暴力破解，找到所有正确的密钥Key(K1+K2)。以下是一个示例：

已知明文known_plaintext = \"0000111100001111\"\
已知密文known_ciphertext = \"1001110100000000\"

由截图可见中间相遇攻击可以找到多个可能的密钥，截图为暴力破解运行部分截图：

<img width="907" alt="image15" src="https://github.com/Achen0933/S-AES/assets/147233663/7bfd64c6-6db6-4ff2-b498-83286a5141be">


<img width="863" alt="image16" src="https://github.com/Achen0933/S-AES/assets/147233663/d4eb0706-6b40-41ae-bded-cc2d04b9d89a">


由图可见，k1外循环进行到一半左右，已生成276个可能的密钥。完整密钥过于冗余，此处不进行展示。

任选一个可能的密钥进行验证，加解密成功。

![image17](https://github.com/Achen0933/S-AES/assets/147233663/baec2244-34c0-4504-8f94-224ec1aa1eca)


**4.3 三重加密**

将S-AES算法通过三重加密进行扩展，本组选择"按照32
bits密钥Key(K1+K2)的模式进行三重加密解密"的模式进行加解密，原理如下：

<img width="229" alt="image18" src="https://github.com/Achen0933/S-AES/assets/147233663/1b3e22c5-a4d3-4e65-a80e-95bb3ed1e4d2">


加解密效果如下：

<img width="320" alt="image19" src="https://github.com/Achen0933/S-AES/assets/147233663/f1dc78bf-7bc1-4a62-89b6-a31d3f0492e1">


第4关测试完成。

## **第5关：工作模式**

本组编写了在CBC模式下进行加解密的算法，并尝试对密文分组进行替换或修改，然后进行解密。

加解密效果如下：

<img width="317" alt="image20" src="https://github.com/Achen0933/S-AES/assets/147233663/d88b8709-3a07-4658-90d3-7bcdf272ada3">


对比篡改密文前后的解密结果可以发现并不相同。第5关测试完成。

# TiMi小组关于S-AES加解密项目开发手册

## **一、概述**

本项目可通过GUI界面实现对二进制、ASCII编码的数据进行加/解密，此外还可以实现双重加密、三重加密以及CBC加/解密，中间相遇攻击（即暴力破解）。

## **二、GUI界面**

**2.1 相关代码**

GUI界面相关代码可参考代码项目中GUI.py相关文件。

**2.2 具体界面及操作解释**

用户可以通过运行GUI.py文件可得：

<img width="306" alt="image21" src="https://github.com/Achen0933/S-AES/assets/147233663/e7e875bb-3393-4112-ad8a-ef9d15b4c07d">


用户输入16位二进制的明/密文以及ASCII码值，可进行加/解密：

<img width="304" alt="image22" src="https://github.com/Achen0933/S-AES/assets/147233663/36e77e19-661a-43c2-8b9d-a0aa46705378">


<img width="305" alt="image23" src="https://github.com/Achen0933/S-AES/assets/147233663/4865b861-d4ab-43dc-a42d-ff1e545a0a84">


若输入密钥或者明文的长度、格式不对（比如密钥长度不为16，二进制明文长度不为16，或者格式不为二进制），会有相关提醒：

<img width="301" alt="image24" src="https://github.com/Achen0933/S-AES/assets/147233663/c3e4ea0e-9011-4816-a70c-a6364a997024">

<img width="299" alt="image25" src="https://github.com/Achen0933/S-AES/assets/147233663/dc664000-692a-4c20-900c-b0d7483051f4">

<img width="302" alt="image26" src="https://github.com/Achen0933/S-AES/assets/147233663/5d0560b8-0584-4a1e-9435-6c9ebcba7ea9">


双重加密/三重加密：

双重加密采用ppt上第一种加/解密方式：

<img width="399" alt="image27" src="https://github.com/Achen0933/S-AES/assets/147233663/14c81fe0-68c8-40c2-baa9-e4085f882d1c">


三重加密采用{k1, k2}模式：

<img width="320" alt="image28" src="https://github.com/Achen0933/S-AES/assets/147233663/4f7ded64-2b4f-4601-bd4d-394d94675488">


CBC加/解密：其中可发现小小的篡改密文后引来变化也是很大

<img width="317" alt="image29" src="https://github.com/Achen0933/S-AES/assets/147233663/ffd2acce-90be-439a-afae-1af595bdd744">


中间相遇攻击：

选定一对明密文，进行中间相遇攻击，虽运行速度较慢，但最终仍可找到相应的密钥

<img width="907" alt="image30" src="https://github.com/Achen0933/S-AES/assets/147233663/2c0e992b-64f1-4f9b-9a83-8c88ac42179d">


## **三、项目代码部分相关介绍**

<img width="235" alt="image31" src="https://github.com/Achen0933/S-AES/assets/147233663/48a1a992-ba7b-4e1b-9b61-844e09972347">


其中GUI.py主要关于界面与函数接口等的融合；function.py主要设计轮密钥加、行位移、列混淆、S-box等的设计；key.py主要设计了密钥扩展；encryption.py主要完成加密过程；decryption.py主要完成解密过程；ASCII.py完成了对于ASCII编码的加/解密；mid-meet-attack.py完成了中间相遇攻击；tribble_aes.py，double_aes.py，cbc_aes.py分别是关于三重加/解密、双重加/解密、CBC对长明/密文加/解密。

可运行文件为：GUI.py；tribble_aes.py，double_aes.py，cbc_aes.py，mid-meet-attack.py文件

## **四、项目背景介绍**

S-AES算法加/解密原理流程图如下：

<img width="385" alt="image32" src="https://github.com/Achen0933/S-AES/assets/147233663/f9070f31-90c3-418b-9153-9d7436f19b9e">


S-AES流程如下：

<img width="289" alt="image33" src="https://github.com/Achen0933/S-AES/assets/147233663/d85c34a0-c0b8-4fa2-873f-321f919b149a">


密钥扩展：

<img width="227" alt="image34" src="https://github.com/Achen0933/S-AES/assets/147233663/2c651f90-e811-4f5b-b77c-635e42e0c4f6">


## **五、实验步骤**

●运行GUI.py文件

●可选择"加密"或者"解密"选项

●输入相应的密钥，二进制明/密文（可选），ASCII编码的明/密文（可选），选择加/解密

●若进行双重/三重/CBC加/解密，可运行tribble_aes.py，double_aes.py，cbc_aes.py，mid-meet-attack.py文件

●运行mid-meet-attack.py文件即可进行中间相遇攻击（但注意暴力破解由于是十六进制，运行时间较长，请谨慎使用）

## **六、其他帮助**

TiMi小组是一个优秀的团队，且热情负责。若您在使用过程中出现任何困惑不解，[[可发送邮件至891073279@qq.com]{.underline}](mailto:可发送邮件至891073279@qq.com)或者3416924346@qq.com。

