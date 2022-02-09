import sys
from tika import parser   #To convert pdf to text
from gtts import gTTS     #To interact with Google's text-to-speech API

class Audiobook:
    def __init__(self, file):
        self.file = file

    def check_if_file_is_pdf(self):
        return self.file[-3:] == 'pdf'

    def get_filename(self):
        filename = self.file.split('/')[-1][:-4]  #To get the filename I use split to seperate the file path string by '/'. Then I go to the last item in the array (which) is the filename and take out the '.pdf'.
        return filename

    def get_text(self):
        raw = parser.from_file(self.file)
        text = raw['content']
        return text

    def create_audio_file(self, text):
        myobj = gTTS(text=text, lang='en', slow=False)
        return myobj

    def save_audio_file(self, object, filename):
        object.save(f"{filename}.mp3")


# Start of Code
file = sys.argv[1]
audio = Audiobook(file)

if audio.check_if_file_is_pdf():
    try:
        filename = audio.get_filename()
        text = audio.get_text()
        object = audio.create_audio_file(text)
        audio.save_audio_file(object, filename)
    except:
        print("Sorry that file doesn't exist.")

else:
    print('Please select a PDF file.')
