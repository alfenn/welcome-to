all:
	sudo apt-get update

	# dash allows the next line to fail without stopping the build, e.g. if Python is already installed

	-sudo apt-get install default-jre
	-sudo apt-get install default-jdk
	chmod u+x run
	echo $PATH
	javac -cp json-simple-1.1.1.jar Runner.java