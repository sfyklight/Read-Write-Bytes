data=[82, 73, 70, 70, 110, 6, 1, 0, 87, 65, 86, 69, 102, 109, 116, 32, 16, 0, 0, 0, 1, 0, 1, 0, 68, 172, 0, 0, 136, 88, 1, 0, 2, 0, 16, 0, 100, 97, 116, 97, 156, 5, 1, 0, 6, 0, 31, 0, 34, 0, 23, 0, 23, 0, 8, 0, 245, 255, 225, 255, 215, 255, 205, 255, 190, 255, 184, 255, 177, 255, 172, 255, 159, 255, 152, 255, 177, 255, 220, 255, 227, 255, 244, 255, 15, 0, 9, 0, 239, 255, 227, 255, 234, 255, 241, 255, 251, 255, 250, 255, 232, 255, 235, 255, 1, 0, 238, 255, 191, 255, 177, 255, 198, 255, 204, 255, 219, 255, 234, 255, 212, 255, 191, 255, 207, 255, 215, 255, 205, 255, 205, 255, 216, 255, 233, 255, 10, 0, 17, 0, 253, 255, 6, 0, 28, 0, 33, 0, 37, 0, 41, 0, 21, 0, 245, 255, 204, 255, 163, 255, 160, 255, 185, 255, 175, 255, 139, 255, 132, 255, 144, 255, 161, 255, 187, 255, 210, 255, 223, 255, 241, 255, 16, 0, 26, 0, 6, 0, 244, 255, 234, 255, 219, 255, 223, 255, 251, 255, 242, 255, 203, 255, 178, 255, 186, 255, 220, 255, 238, 255, 221, 255, 191, 255, 163, 255, 162, 255, 173, 255, 175, 255, 164, 255, 168, 255, 171, 255, 174, 255, 219, 255, 8, 0, 16, 0, 31, 0, 64, 0, 92, 0, 97, 0, 79, 0, 75, 0, 78, 0, 37, 0, 209, 255, 134, 255, 99, 255, 93, 255, 105, 255, 127, 255, 130, 255, 150, 255, 217, 255, 23, 0, 27, 0, 28, 0, 74, 0, 95, 0, 87, 0, 88, 0, 73, 0, 28, 0, 242, 255, 222, 255, 222, 255, 222, 255, 189, 255, 173, 255, 175, 255, 138, 255, 126, 255, 168, 255, 185, 255, 178, 255, 170, 255, 184, 255, 232, 255, 246, 255, 223, 255, 212, 255, 243, 255, 29, 0, 26, 0, 254, 255, 253, 255, 22, 0, 18, 0, 217, 255, 183, 255, 184, 255, 185, 255, 166, 255, 155, 255, 150, 255, 127, 255, 109, 255, 105, 255, 115, 255, 120, 255, 117, 255, 136, 255, 196, 255, 244, 255, 4, 0, 12, 0, 37, 0, 46, 0, 44,4, 0, 9, 0, 10, 0, 22, 0, 10, 0, 255, 255, 9, 0, 17, 0, 76, 73, 83, 84, 90, 0, 0, 0, 73, 78, 70, 79, 73, 67, 82, 68, 11, 0, 0, 0, 50, 48, 49, 49, 45, 48, 53, 45, 50, 48, 0, 0, 73, 69, 78, 71, 19, 0, 0, 0, 82, 105, 99, 104, 97, 114, 100, 32, 72, 101, 105, 116, 107, 101, 109, 112, 101, 114, 0, 1, 73, 83, 70, 84, 30, 0, 0, 0, 83, 111, 117, 110, 100, 32, 70, 111, 114, 103, 101, 32, 65, 117, 100, 105, 111, 32, 83, 116, 117, 100, 105, 111, 32, 49, 48, 46, 48, 0, 67, 68, 105, 102, 68, 0, 0, 0, 68, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
buffer = bytes(data)
print(buffer)
f = open("output.mp3", "bw")
f.write(buffer)
f.close()
