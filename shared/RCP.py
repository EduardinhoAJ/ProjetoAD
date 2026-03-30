import pickle
import struct


def receive_all(sock, n):
    dados = b""
    while len(dados) < n:
        chunk = sock.recv(n - len(dados))
        if not chunk:
            return None
        dados += chunk
    return dados


def send_message(sock, msg):
    msg_bytes = pickle.dumps(msg)
    msg_size_bytes = struct.pack("!I", len(msg_bytes))
    sock.sendall(msg_size_bytes)
    sock.sendall(msg_bytes)


def receive_message(sock):
    resp_size_bytes = receive_all(sock, 4)
    if resp_size_bytes is None:
        return None
    resp_size = struct.unpack("!I", resp_size_bytes)[0]
    msg = receive_all(sock, resp_size)
    if msg is None:
        return None
    return pickle.loads(msg)