class PseudoColor_to_Truecolor:
    def __init__(self,path):
        self.path=path

    def toTrue(self,outpath):
        with open(self.path,'rb') as f:
            with open(outpath,'wb') as r:
                f.seek(0)
                self.head=f.read(54);
                r.write(self.head)

                self.bfOffBits=int.from_bytes(self.head[10:14],byteorder='little')
                self.width = int.from_bytes(self.head[18:22], 'little')
                self.height = int.from_bytes(self.head[22:26], 'little')

                row_size = self.width * 3
                if row_size % 4 != 0:
                    row_size = ((row_size // 4) + 1) * 4

                f.seek(54)
                for i in range(self.height):
                    rowData = f.read(row_size)
                    r.write(rowData)

    def convert(self,outpath):
        self.toTrue(outpath)

# main
inputImg = PseudoColor_to_Truecolor('D:/Firost/DMT/多媒体技术/张馨允_实验三/robert_2.bmp')
inputImg.convert('truecolor.bmp')

                    
