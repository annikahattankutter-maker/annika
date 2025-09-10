# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # integer

b = 1.5
print(b)
print(type(b)) # float

c = 3j
print(c)
print(type(c)) # complex

d = "hello"
print(d)
print(type(d)) # string

e = [1, 2, 3]
print(e)
print(type(e)) # list

f = {"name": "Ellen", "Favorite fruit": "strawberry"}
print(f)
print(type(f)) # dict

g = (1, 2)
print(g)
print(type(g)) # tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # list

i = True
print(i)
print(type(i)) # boolean

j = None
print(j)
print(type(j)) # NoneType

k = [True, "blue", 12]
print(k)
print(type(k)) # list

l = str(14)
print(l)
print(type(l)) # string

m = 1e4
print(m)
print(type(m)) # float

n = range(5)
print(n)
print(type(n))

# --- Booleans ---
print(10 > 9) # true
print(10 == 9) #false
print(10 <= 9) #false
print(bool("abc")) #true
print(bool(123)) #true
print(bool(["apple", "cherry", "banana"])) #true
print(bool(True)) #true
print(bool(False)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool(" ")) #true
print(bool(())) #false
print(bool([])) #false
print(bool({})) #false
print(bool(True and False)) #false
print(bool(True and True)) #true
print(bool(False and False)) #false
print(bool(True or False)) #true
print(bool(True or True)) #true
print(bool(False or False)) #false
print(bool(not(False))) #true
print(bool(not(True))) #false

# --- Operators ---
print(10 + 5) #15
print(10 - 5) #5
print(2*4) #8
print(6/3) #2
print(5%2) #1
print(3 ** 2) #9
print(15 // 2) #7

# --- Comparison Operators ---
print(5 == 2) #false
print(10 !=10) #false
print(2 < 5) #true
print(12 > 5) #true
print(5 <=6) #true
print(1 >= 10) #false

# --- Assignments Operators ---
x = 5
x += 5
print(x) #10
x -= 4
print(x) #6
x *= 3
print(x) #18

# --- Logical Operators ---
# the operator and means that both commands are ran at the same time 
print(bool(True and True))
print(bool(True and False))
# the operator or means that the system will run either command
print(bool(True or False))
print(bool(False or False))
# the operator not means that the system will run the opposite of the command
print(bool(not(False)))
print(bool(not(True)))

# --- Strings ---
my_string = "hello"
print(my_string) #prints hello
print(my_string[0]) #prints h
print(my_string[1]) #prints e
print(my_string[2]) #prints l
print(my_string[3]) # print l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o
print(my_string[1:3]) # prints el
print(my_string[0:5:2]) # prints hlo
print(len(my_string)) # prints 5
print(my_string*7) # prints hello 7 times

name = "oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")

# --- Terminal Commands ---
# cd
# changes directries. Use it to move from one folder to another
# example: cd Desktop

# ls
# lists files in current working directory
# example: ls python_decal_fall25

#ls -a
# shows all files, including hidden ones that start with "." 
# example: .DS_Store

#mkdir
#creates a new foler in the current location
# example: mkdir my_folder

#cat
#prints the contents of a file
#example: cat notes.txt

#pwd
#shows the full path of your current location
#example: pwd would give you users/annika/projects

#cd ..
#moves you up one directory
#example: cd ... (if your in users/annika/projects it takes you to users/annika)

#cd .
# means stay in the current directory your in
# example: cd . (stays in the same place)

#cd ~
# goes to your home directory
#cd ~ (takes you to users/annika)

#cp
# makes a copy of your files
# example: cp notes.txt backup.txt

#mv
# moves or renames files
# example: notes.txt projects/notes.txt (moves notes.txt into projects folder)

#rm
# removes (deletes) files
# example: rm notes.txt (deletes notes.txt)

#clear
#clears the terminal screen without deleting the files
# example: clear

#grep
# finds lines that math a pattern (inside a file)
#example: grep "error" log.txt (shows all lines in log.txt that contain "error")

# touch
# creates an empty file
# touch newfile.txt

# head
# shows the first lines of a file
# head notes.txt (shows last 10 lines as default)

# tail
# shows the last lines of a file
# tail notes.txt (shows last 10 lines as defult)

#ls -t
# sorts files by modification time (newest first)
# example: ls -lt

# grep -n
# shows the line numbers in the output
#grep -n "TODO" notes.txt

# rm -i
# interactive mode, asks before deleting each file
# example: rm -i notes.txt