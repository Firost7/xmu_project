class TrueColor_to_PseudoColor:
    def __init__(self,path):
        self.path = path

    def readHead(self):
        with open(self.path,"rb") as f:
            f.seek(0)
            self.head=f.read(54) #文件头

            self.OffBits = int.from_bytes(self.head[10:14], 'little') #位图数据偏移量
            self.width = int.from_bytes(self.head[18:22], 'little')
            self.height = int.from_bytes(self.head[22:26], 'little')

            self.data=[]
            row_size = self.width * 3
            f.seek(self.OffBits)
            for i in range(self.height):
                self.data.append(f.read(row_size))

    def toGray(self):
        self.grayData=[]
        for row_data in self.data:
            grayData_row = bytearray()
            for i in range(0, len(row_data), 3):
                b = row_data[i]
                g = row_data[i + 1]
                r = row_data[i + 2]
                value = int(0.299 * r + 0.587 * g + 0.114 * b)
                grayData_row.append(value)
            self.grayData.append(grayData_row)
            
    def toPseudo(self,outpath):
        with open(outpath,'wb') as f:
            #文件头
            f.write(b'BM')
            f.write((54 + self.height * self.width).to_bytes(4, byteorder='little'))
            f.write(b'\x00\x00')
            f.write(b'\x00\x00')
            f.write((54).to_bytes(4, byteorder='little'))
            
            #信息头
            f.write(b'\x28\x00\x00\x00')
            f.write(self.width.to_bytes(4, byteorder='little'))
            f.write(self.height.to_bytes(4, byteorder='little'))
            f.write(b'\x01\x00')
            f.write(b'\x08\x00')
            f.write(b'\x00\x00\x00\x00')  
            f.write(b'\x00\x00\x00\x00') 
            f.write(b'\x00\x00\x00\x00')
            f.write(b'\x00\x00\x00\x00')
            f.write(b'\x00\x00\x00\x00')
            f.write(b'\x00\x00\x00\x00')

            #调色板
            for i in range(256):
                f.write(bytes([i, i, i, 0]))

            #位图数据
            for row in self.grayData:
                for pixel in row:
                    f.write(bytes([pixel]))
                padding = 4 - (len(row) % 4) #填充字节
                if padding != 4:
                    f.write(bytes(padding))


    def convert(self,outpath):
        self.readHead()
        self.toGray()
        self.toPseudo(outpath)

# main
inputImg = TrueColor_to_PseudoColor('D:/Firost/DMT/多媒体技术/张馨允_实验三/robert_1.bmp')
inputImg.convert('pseudo.bmp')

                    
