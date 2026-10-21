# Problem sets

A problem set is a few small programs and the data file they read. There is one folder per lecture, at the same path as the lecture:

```
lectures/110_python_py_files/100-program-inputs.ipynb      the lecture
problem_sets/110_python_py_files/100-program-inputs/       its problem set
```

Your Canvas assignment says which problem set is due and when. You work on your own laptop, then copy your work to the course server. (The command-line and git sets are the exception: they are done on the server itself, see [the last section](#sets-done-on-the-server).) The steps are the same for every problem set. The commands below use `110_python_py_files/100-program-inputs` as the example: change those two names to the ones in your assignment.

## 1. Get the files

They are in your copy of this repository, in the problem set's folder. Work on them right there.

```bash
# on your laptop, in the folder of your copy of this repository
# get the newest files
git pull

# go to the problem set's folder
cd problem_sets/110_python_py_files/100-program-inputs
```

You are now changing files that git tracks. Expect `git pull` to tell you so from time to time: if a pull brings a new version of a file you have changed, git stops and names the file, or reports a conflict. That is normal and nothing is lost. Keep your own version of a program you have worked on.

## 2. Do the work

Open each program in that folder. The comment at the top says what to do. The docstring of each function says what the function must return, with one example.

## 3. Check it

The comment at the top of each program gives one command to type and the output it should print. Type the command in the program's folder and compare.

This is the only check you are given. Your work is graded with more inputs than this one, so matching output means you are on the right track, not that you are finished.

## 4. Copy it to the server

Your work is collected from the course server, from `~/problem_sets/110_python_py_files/100-program-inputs/` in your home there. Nothing is uploaded to Canvas.

```bash
# on your laptop
# YOUR_USER_NAME@SERVER is what you type after "ssh" to log in to the course server

# make the folder on the server (this runs one command there and comes back)
ssh YOUR_USER_NAME@SERVER mkdir -p problem_sets/110_python_py_files

# go to the folder of your copy of this repository, then copy the problem set's folder to the server;
# -r copies a folder and everything in it
scp -r problem_sets/110_python_py_files/100-program-inputs YOUR_USER_NAME@SERVER:problem_sets/110_python_py_files/
```

If you change a program after this, type the `scp` command again. It replaces the files on the server.

## 5. Make sure it runs on the server

Your work is graded on the server, not on your laptop. Log in and type each program's check command there too.

```bash
# on your laptop: log in to the server
ssh YOUR_USER_NAME@SERVER

# on the server: go to your copy and type the command from the top comment of each program
cd ~/problem_sets/110_python_py_files/100-program-inputs
python p1_last_close.py MSFT
```

A program that works on your laptop can fail on the server: a file was not copied, or your laptop has a package or a version of Python the server does not. If the output differs, fix the program on your laptop and copy it again.

At the deadline, leave the files where they are on the server.

## Sets done on the server

The command-line and git sets have no programs. Each problem is a text file, `p1_....txt`, that says what to make and gives commands to check it, with what they should print. You do them on the course server, not on your laptop, and nothing is copied with `scp`.

```bash
# on your laptop: log in to the server
ssh YOUR_USER_NAME@SERVER

# on the server: read a problem (the same files are in your copy of this repository)
cat /opt/lectures/problem_sets/060_learn_command_line/linux_command_line/p1_backup.txt
```

The files a problem starts from are in `/opt/lectures/problem_sets/...` on the server. You can read and copy them but not change them, so if you make a mess you can always copy them again. What you make goes in `~/problem_sets/<the set's path>/` in your home on the server, and is graded there at the deadline. Leave it where it is.
