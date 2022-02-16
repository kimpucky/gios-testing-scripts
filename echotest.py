""" Echo Server testing """
import socket
import time
import sys

def send_to_server(buf):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 10823))
    s.send(buf)
    # Just do one read, and not any header and payload logic...
    print(s.recv(8192))
    s.close()


if __name__ == "__main__":


    # Which option to test
    option = int(sys.argv[1]) if len(sys.argv)>1 else 2
    print(f"option={option}")

    if option == 1:
        # Option 1.  # Do not send anything.
        # Break this server and the client recv() may ECONNRESET if it is waiting for data.
        pass
    elif option == 2:
        # Option 2. Send the default client message "Hello Summer!!".
        send_to_server(b"-m ")
        time.sleep(1)
        send_to_server(b"Hello Summer!!")
    elif option == 3:
        # Option 3. Send the header, in pieces, with enough time to interrupt. Then send 1 byte payload.
        # Break this server to cause ECONNRESET on the client recv() in the header processing.
        send_to_server(b"-m Hello Summer!! Hello Spring!!")
    else:
        # Serve a random sized file with random-sized buffers of random bytes, and show the SHA1 hash.
        # This can be verified with: sha1sum filename.
        #
        # header is not part of the buffer.
        message = b'-m This is \na test'
        send_to_server(message)