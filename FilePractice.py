import os
with open('/home/jason/python/helloFlask.py', 'r') as f:
    print(f.name)
    print(os.path.dirname(f.name))
    print(os.path.exists(f.name))
    # for line in f:
    #     print(line)

# with open('/home/jason/python/filePractice.py', 'w') as wf:
#     wf.write('print(hello world)')


