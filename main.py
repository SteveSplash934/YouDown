#!/usr/bin/python

import os, sys
import time
import pyfiglet as pf
from colorama import Fore, Back, Style
from pytube import *

if sys.platform.startswith("linux"):
	def cls():
		os.system("clear")
elif sys.platform == "darwin":
	def cls():
		os.system("clear")
elif sys.platform == "win32":
	def cls():
		os.system("cls")


def slowprint(string, timing=0.03):
	for c in string:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(timing)


def main_banner():
	print(Fore.GREEN)
	str = pf.figlet_format("YouDown", font="banner3-D")
	slowprint(str, 0.006)
	print(Fore.YELLOW)
	slowprint("\t\t\t\tv2.0 - By Shepherd", 0.03)
	print(Fore.RESET)

def info():
	print(Fore.MAGENTA)
	slowprint("\t\t\t\tEnter G/g to go back", 0.04)
	print(Fore.RESET)

def banner():
        print(Fore.GREEN)
        str = pf.figlet_format("YouDown", font="banner3-D")
        print(str)
        print(Fore.RESET)

def go_back():
        choice = "\n[G/g] Go back\n[E/e] Exit"
        slowprint(choice)
        choice = str(input("\n[?] Option: "))
        if choice == "G" or choice == "g":
                cls()
                main_banner()
                menu()
        else:
                sys.exit()

def go_back2(var):
	if var == "g" or var == "G":
		cls()
		main_banner()
		menu()

def dvideo():
	cls()
	banner()
	print(Fore.RED)
	slowprint("\t\t\t\t[Dowload a Video]", 0.03)
	info()
	print(Fore.YELLOW)
	url = str(input("[?] Enter video URL: "))
	go_back2(url)
	video = YouTube(url)
	print(Fore.CYAN)
	print("[i] Downloading ", video.title, "...")
	stream = video.streams.get_highest_resolution()
	stream.download()

def dmvideos():
	cls()
	banner()
	print(Fore.RED)
	slowprint("\t\t\t\t[Download Multiple Videos]", 0.03)
	info()
	print(Fore.YELLOW)
	url_filename = str(input("[?] Enter file name/path: "))
	go_back2(url_filename)
	url_file = open(url_filename, 'r')
	if url_file == None:
		print(Fore.RED)
		print("[!] File doesn't exist")
		sys.exit()
	else:
		for every_line_url in url_file.readlines():
			every_line_url = every_line_url.strip('\n')
			if every_line_url.startswith("#"):
				pass
			else:
				print(Fore.CYAN)
				print("[-] Please Wait...")
				video = YouTube(every_line_url)
				print("[i] Dowloading...", video.title)
				stream = video.streams.get_highest_resolution()
				stream.download()


def dplaylist():
	cls()
	banner()
	print(Fore.RED)
	slowprint("\t\t\t\tDownload Playlists", 0.03)
	info()
	print(Fore.YELLOW)
	url = str(input("[?] Enter Playlist URL: "))
	go_back2(url)
	playlist = Playlist(url)
	print(Fore.CYAN)
	print("[i] Please wait while fetching playlist details...")
	dir_name = playlist.title

	# create a folder to group playlists
	os.mkdir(dir_name)
	os.chdir("./"+dir_name)

	# download the videos into the folder
	print(Fore.CYAN)
	print(f"\n[i] Now Downloading...{playlist.title} videos")
	for video in playlist.videos:
		print(f"\n[i] Now Downloading...{video.title}")
		stream = video.streams.get_highest_resolution()
		stream.download()
	print(Fore.GREEN)
	slowprint("[i] Done\n")
	os.chdir("..")
	print(Fore.RESET)
	print(Fore.YELLOW)
	print("[??] Do you want to download any other playlist?")
	print(Fore.BLUE)
	choice = "\n[Y/y] Yes\n[N/n] No"
	slowprint(choice)
	choice = str(input("\n[?]: "))
	print(Fore.RESET)
	if choice == str("Y") or choice == str("y"):
		cls()
		dplaylist()
	else:
		menu()

def dmplaylist():
	cls()
	banner()
	print(Fore.RED)
	slowprint("\t\t\t\t[Download Multiple Playlists]", 0.03)
	info()
	print(Fore.YELLOW)
	url_filename = str(input("[?] Enter Playlist File: "))
	go_back2(url_filename)
	url_file = open(url_filename, 'r')
	if url_file is None:
		print(Fore.RED)
		print("[?] File doesn't exist")
		print(Fore.RESET)
		sys.exit
	else:
		for every_url_line in url_file.readlines():
				every_url_line = every_url_line.strip('\n')
				if every_url_line.startswith("#"):
					pass
				else:
					playlist = Playlist(every_url_line)
					print(Fore.CYAN)
					print("[i] Please wait, Fetching Playlist details...")
					dir_name = playlist.title
					# create a folder to group playlists
					os.mkdir(dir_name)
					os.chdir("./"+dir_name)
					# download the videos into the folder
					print(Fore.YELLOW)
					print(f"[i] Now Downloading...{playlist.title} videos")
					for video in playlist.videos:
						print(f"[i] Now Downloading...{video.title}")
						stream = video.streams.get_highest_resolution()
						stream.download()
						slowprint("Done\n")
		os.chdir("..")
		print(Fore.RESET)


def about():
	cls()
	main_banner()
	slowprint("Version: 2.0 - rA\n")
	str_sh = pf.figlet_format("\nSHEPHERD", font="banner3-D")
	print(Fore.YELLOW, str_sh)
	social_handles = "Google: stevesplash4@gmail.com\nGithub: https://github.com/stevesplash934\nFacebook: https://www.facebook.com/steve.splash.10\nMessenger: m.me/steve.splash.10\nInstagram: stevesplash934"
	slowprint(social_handles)
	about = """
		This tool was built by SHEPHERD (aka. SteveSplash)
	The main purpose of this tool is download videos and/or playlist from youtube
		This version 2 was made on Sat 22, 10, 2022
			For more information kindly reach me through my social handles
				and for more details, kindly go to the help menu. Thanks
				MADE BY PROGRAMMER AND FOR EVERYONE
			REMEMBER, MY CODES ARE NOT FOR EVILS! YOU ARE ON YOUR OWN IF YOU USE ANY OF MY TOOL(S) TO COMMIT CRIME
		"""
	slowprint(about)
	go_back()

def helpme():
	desc = """
Run the program, 
choose what you want from the menu, 
specify a link or file containing multiple links and wait for it to be Downloaded
"""
	slowprint(desc)
	go_back()


def menu():
	print(Fore.MAGENTA)
	menu_str = "\n[1] Download Video\n[2] Download multiple videos\n[3] Download Playlist\n[4] Download multiple playlist\n[5] About\n[6] Help\n[7] Exit\n"
	slowprint(menu_str, 0.01)
	print(Fore.RESET)
	print(Fore.CYAN)
	option = int(input("\n[?] Option: "))
	if option == 1:
		dvideo()
	elif option == 2:
		dmvideos()
	elif option == 3:
		dplaylist()
	elif option == 4:
		dmplaylist()
	elif option == 5:
		about()
	elif option == 6:
		helpme()
	elif option == 7:
		print("Thanks for using me :]")
		sys.exit()
	else:
		print(Fore.YELLOW, "Invalid input!!! Please choose between 1 - 7")
		time.sleep(0.2)
		menu()
cls()
main_banner()
menu()


