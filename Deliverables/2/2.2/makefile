<<<<<<< HEAD
all:
	sudo apt-get update

	# dash allows the next line to fail without stopping the build, e.g. if Python is already installed

	-sudo apt-get install default-jre
	-sudo apt-get install default-jdk
	chmod u+x run
	echo $PATH
	javac -cp json-simple-1.1.1.jar Runner.java
=======
download-java run:
	wget "https://download.java.net/java/GA/jdk13/5b8a42f3905b406298b72d750b6919f6/33/GPL/openjdk-13_linux-x64_bin.tar.gz"
	
	tar -xf openjdk-13_linux-x64_bin.tar.gz
	
	echo "java binaries are now in ./jdk-13/bin/"
	chmod u+x run
>>>>>>> 0c8b18f594366414bbfde7868be812f4ef06730d
