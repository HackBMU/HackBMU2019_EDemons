import serial
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')
engine.setProperty('rate', 101)

arduinosedata = serial.Serial('Com5', 9600)
while(1==1):
                if(arduinosedata.inWaiting()>0):
                                emdata = arduinosedata.readline()
                                print(emdata)
                                engine.say(emdata)
                                engine.runAndWait()
                                
