import sys
import socket
import os
import struct

def checksum(source_string):
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count < countTo:
        thisVal = source_string[count + 1]*256 + source_string[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2

    if countTo < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

def sendFirst(dst, fileSize, sock):
    identifier = 0
    dest_addr = socket.gethostbyname(dst)
    checkSum = 0
    # Type(1), Code(1), ICMP Checksum(2), Identifier(2), Sequence Number(2)
    header = struct.pack("bbHHh", 8, 0, checkSum, identifier, 0)
    data = struct.pack("Q", fileSize)
    checkSum = checksum(header + data)
    # htons: Host to Network Short
    header = struct.pack(
        "bbHHh", 8, 0, socket.htons(checkSum), identifier, 0
    )
    # print('H:', header, len(header))
    # print('D:', data, len(data))
    packet = header + data
    # print('P:', packet, len(packet))
    sock.sendto(packet, (dest_addr, 1))

def server(host, file):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
    byteBox = []
    fileSize = 0
    while 1:
        recPacket, addr = s.recvfrom(1024)
        icmpHeader = recPacket[20:28]
        _type, _code, _checksum, _id, seqNumber = struct.unpack("bbHHh", icmpHeader)
        # print('seqNumber:', seqNumber)
        if seqNumber == 0:
            icmpData = recPacket[28:]
            fileSize = struct.unpack("Q", icmpData)[0]
            print('set filesize:', fileSize)
        else:
            # 結尾
            if fileSize < 8:
                icmpData = recPacket[28:28 + fileSize]
                byteBox.append((seqNumber, icmpData))
                byteBox = list(set(byteBox))
                byteBox.sort(key=lambda x: x[0])
                recFile = b''
                for elem in byteBox:
                    recFile += elem[1]
                with open(file, "wb") as f:
                    f.write(recFile)
                break
            # 非結尾
            else:
                icmpData = recPacket[28:]
                fileSize -= 8
                print(f"Data: {icmpData}, seqNumber: {seqNumber}")
                byteBox.append((seqNumber, icmpData))
def client(dst, file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    identifier = 0
    fileSize = os.path.getsize(file)
    file = open(file, "rb")
    sendByte = file.read(8)
    seqNumber = 1
    sendFirst(dst, fileSize, sock)
    while sendByte:
        print(f"Data: {sendByte}, seqNumber: {seqNumber}")
        dest_addr = socket.gethostbyname(dst)
        checkSum = 0
        # Type(1), Code(1), ICMP Checksum(2), Identifier(2), Sequence Number(2)
        header = struct.pack("bbHHh", 8, 0, checkSum, identifier, seqNumber)
        # 讓 sendByte 湊滿 4 bytes
        pad = 8 - len(sendByte)
        data = sendByte + b'\x00' * pad
        checkSum = checksum(header + data)
        # htons: Host to Network Short
        header = struct.pack(
            "bbHHh", 8, 0, socket.htons(checkSum), identifier, seqNumber
        )
        # print('H:', header, len(header))
        # print('D:', data, len(data))
        packet = header + data
        # print('P:', packet, len(packet))
        sock.sendto(packet, (dest_addr, 1))
        sendByte = file.read(8)
        seqNumber += 1
    file.close()
    sock.close()

def main():
    if len(sys.argv) != 4:
        print("Usage: app.py {server|client} host file")
    else:
        host = sys.argv[2]
        file = sys.argv[3]
        if sys.argv[1] == "server":
            server(host, file)
        elif sys.argv[1] == "client":
            client(host, file)
        else:
            print("Usage: app.py {server|client} host file")
main()