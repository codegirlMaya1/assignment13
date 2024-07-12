import os

old_path='hi_file.txt'
new_path=os.path.join('subdir','hi_file.txt') 
os.rename(old_path,new_path)
print(" Please make a selection! Enter 1 to see old path or 2 to see this files new path")
user=int(input(" Type 1 or 2: "))
if user==1:
    print(old_path) 
elif  user==2:
    print(new_path)

# Please move hi_file.txt back under "ExploringPython'sOsModule.py (original path) if resetting or starting over"
