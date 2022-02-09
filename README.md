# PDFtoAudiobook

This program allows the user to take a pdf file and create an mp3 file (aka 'Audiobook') that recites the text found in the pdf file.

# How it Works

In order for the program to run, you will need to have Python3 installed.  I suggest downloading the latest version at https://www.python.org/downloads/.

Assuming that the user has python installed, the first thing would be to download the code off of GitHub.  After it is finished downloading, I recommend putting the project
folder on the Desktop just to make finding it easier.

Next open a Terminal window and open the project folder.  If I saved the file on my Desktop then I would enter the following commands:

    cd Desktop
    cd PDFtoAudiobook-master
    
When the project folder is open on the Terminal, now would be a good time to make sure the appropriate modules are installed.  The two modules I use are the tika module, which returns the text from the PDF file as a string and the gtts module, which interacts with the Google Translate's Text-to-Speech API and returns the audio file.  The following commands will install both modules:

    pip3 install tika
    pip3 install gtts
    
After the modules are installed then the program can be run by entering the following command:

    python3 main.py <insert pdf>
    
Where it says 'insert pdf' is where the file name for the pdf should go.  An easy way to get the full filename is to copy the pdf link and then paste it into the terminal.  After entering the command, the program should run.  If the entered file is a PDF and the filename is correct then the mp3 file should be created inside of the project folder.
    


