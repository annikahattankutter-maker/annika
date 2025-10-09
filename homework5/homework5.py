# ---- Vocabulary Review ---- 
# 1) Git = Tracks and manages code changes on your computer
#    Github = Hosts and shares code repositories on your internet
# 2) Terminal = Program that opens a text window and displays your input/output
#    Command Line = An interface inside the terminal where you can type out commands
# 3) Local Repository = A git repository stored on your own computer only accessable to yourself
#    Remote Repository = online git repository that can be shared with others
# 4) Version Control = tool to help track and manage changes to files and code over time
# 5) Staging Area = is a place to stick your changes to your code before offically saving them
# 6) git add = moves your files into the staging area (knows which files you are planning on saving)
# 7) git commit = takes what's in your staging area and saves it to your project's local repository
# 8) git push = sends your committed changes from your local repository to your remote repository, like github
# 9) git status = shows what has changed in your working directory and staging area
# 10) git pull = downloads and merges the changes from your remote repository into your local repository
# 11) pwd = tells you when you are in your working diretory
# 12) ls = lists the contents in your current directory
# 13) cd = moves you into a working directory in your current directory
# 14) nano = edits a text file
# 15) touch = creates an empty file or updates an existing one
# 16) mv = moves or renames a file
# 17) rm = deletes a file
# 18) cat = looks at a file or combines files without opening a full editor

# ---- A Directory Tree ----
# 1) pwd
# 2) ls
# 3) git status
#    git pull origin main
# 4) mv homework.py homework/
# 5) cd ..
#    cd judy_decal/
#    cd homework/
# 6) python3 homework.py
# 7) cd ..
#    cd ..
#    git add .
#    git commit -m "done with hw"
#    git push origin main
# 8) git pull origin main
#    git pull origin main
# 9) cd ..

# ---- Data Types ----
def check_data_type(x):
    print(x)
    return type(x).__name__
print(check_data_type(3))

# ---- Conditionals ----
number = 2
def even_or_odd(num):
    num / 2
    if num  == type(int):
        print('Even')
    else:
        print('Odd')
even_or_odd(5)

# ---- Loops ----
numbers = [1, 2, 3, 4, 5]

def sum_with_loop(number):
    total = 0
    for num in number:
        total += num
    return total
print(sum_with_loop(numbers))

# ---- Lists ----
list1 = ['a', 'b', 'c']
def duplicated_list(list1):
    new_list = []
    for letter in list1:
        new_list.append(letter)
        new_list.append(letter)
    return new_list
print(duplicated_list(list1))

# ---- Debugging ----
def square(num):
    new_num = num * num
    return new_num
print(square(3))
