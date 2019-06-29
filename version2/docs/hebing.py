import os
path = '/Users/young/codes/invest/version2/docs/s15_随便聊聊'
file_list = os.listdir(path)
new_file = 'new2.md'
for item in file_list:
    with open(os.path.join(path, item)) as f:
        with open(new_file, 'a+') as fw:
            fw.write(f.read()+'\n\n')
            print("[正在写入]", item)
