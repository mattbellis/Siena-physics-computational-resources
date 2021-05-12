Open up a terminal. If you are not sure how to do this, ask the instructor or your peers.
  
Where are you?

    pwd 

Who are you?

    whoami

What files are in this directory?

    ls
    ls -l 

------

Download a tar archive (similar to a zip file), with directories and files in it. 

Download the necessary files for this exercise.

```
  wget https://github.com/mattbellis/Siena-physics-computational-resources/raw/master/CLI/linux_hello_world.tgz
```

This should have downloaded the file to whatever directory you are in. Check to see that it's there by running
```
  ls -l
```  

Unpack (actually untar) this file with the following command (hit "Enter" after you type that). 

    tar -zxf linux_hello_world.tgz

What files/directories do you have now?

    ls -ltr 

Your assignment now is to:
* Map out the files and directories under "project".
* Run any python scripts you find. Python scripts usually have a ```.py``` at the end of the filename.

        python FILENAME

* You may or may not get an error when you run one of these files. If so, try to fix the error by editing the file with `nano` or `pico` or the editor of your choice.
* Look inside any data files you find. 
* What is the full path to the data files?
* Where do I need to book travel to?


Once you have run through the above steps, use your "Linux cheat-sheet" to
* Make a copy of some of the files. 
* Delete some of these files. 
* Make a new directory.
* Remove that directory. 
* Edit a file using the [nano editor](http://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/) or the editor of your choice.
